"""Small, explicit embedding/index/search operations. Never runs the full workflow."""
import argparse
from contextlib import closing
import hashlib
import json
import math
import os
from pathlib import Path
import re
import sqlite3
import tempfile
import uuid

ROOT = Path(__file__).resolve().parents[1]


def read_json(path):
    return json.loads(path.read_text(encoding="utf-8-sig"))


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def write_new(path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("x", encoding="utf-8") as stream:
        json.dump(value, stream, ensure_ascii=False, indent=2, allow_nan=False)


def source_workspace(source, root=ROOT):
    if not re.fullmatch(r"source-\d{2,}", source):
        raise ValueError("Use a source identifier such as source-01.")
    original = root / "sources" / source
    if not original.is_dir() or not original.resolve().is_relative_to((root / "sources").resolve()):
        raise ValueError("Assigned source is missing or outside sources/.")
    work = root / "workspace" / source
    if not work.resolve().is_relative_to((root / "workspace").resolve()):
        raise ValueError("Workspace must stay inside workspace/.")
    return work


def validate_vector(vector, dimensions):
    if not isinstance(vector, list) or len(vector) != dimensions:
        raise ValueError("Embedding dimension mismatch.")
    if any(isinstance(v, bool) or not isinstance(v, (int, float)) or not math.isfinite(v) for v in vector):
        raise ValueError("Embedding contains invalid numbers.")
    if not any(v != 0 for v in vector):
        raise ValueError("Zero vector is not a valid searchable embedding.")


def load_records(work, source, config):
    documents_path = work / "knowledge/documents.json"
    validation = read_json(work / "knowledge/validation.json")
    if validation.get("passed") is not True or validation.get("documents_sha256") != sha(documents_path):
        raise ValueError("Knowledge validation is missing, failed, or stale. Run validate.")
    documents = read_json(documents_path)
    # Prepared knowledge is a dict with a "documents" list (see enrich.py); a bare list is also accepted.
    if isinstance(documents, dict):
        documents = documents.get("documents")
    if not isinstance(documents, list):
        raise ValueError("documents.json must contain a list.")
    by_id = {doc["document_id"]: doc for doc in documents}
    if len(by_id) != len(documents):
        raise ValueError("Duplicate document IDs.")
    path = work / "chunks/records.json"
    records = read_json(path)
    if not isinstance(records, list) or not 1 <= len(records) <= config["max_chunks_per_source"]:
        raise ValueError("Invalid chunk count for the workshop.")
    seen = set()
    for record in records:
        if record.get("source_id") != source or record.get("chunk_id") in seen or not record.get("chunk_id"):
            raise ValueError("Wrong source or duplicate/missing chunk ID.")
        seen.add(record["chunk_id"])
        text = record.get("text", "")
        if not isinstance(text, str) or not text.strip() or len(text) > config["max_chunk_characters"]:
            raise ValueError("Empty or oversized chunk.")
        doc = by_id.get(record.get("document_id"))
        if not doc or doc.get("source_id") != source:
            raise ValueError("Chunk points to an unknown document/source.")
        start, end = record.get("start"), record.get("end")
        if type(start) is not int or type(end) is not int or not 0 <= start < end <= len(doc["text"]):
            raise ValueError("Invalid chunk offsets.")
        if doc["text"][start:end] != text:
            raise ValueError("Chunk text no longer matches validated knowledge.")
        if not isinstance(record.get("metadata"), dict) or record["metadata"] != doc.get("metadata"):
            raise ValueError("Chunk metadata differs from its source document.")
        if record.get("source_file") != doc.get("source_file"):
            raise ValueError("Chunk source filename differs from its document.")
    return records, sha(path)


def embed_texts(texts, model, dimensions):
    # Imports/key loading are deferred: indexing and offline tests need no API key.
    from dotenv import load_dotenv
    from openai import OpenAI
    load_dotenv(ROOT / ".env", override=False)
    if not os.environ.get("OPENAI_API_KEY", "").strip():
        raise ValueError("OPENAI_API_KEY is missing. Enter it privately in .env or the environment.")
    client = OpenAI(base_url="https://api.openai.com/v1", timeout=60, max_retries=0)
    try:
        response = client.embeddings.create(model=model, dimensions=dimensions, input=texts, encoding_format="float")
    except Exception as error:
        # Do not expose response bodies or credentials in participant logs.
        raise RuntimeError(f"OpenAI embedding request failed ({type(error).__name__}). Check account access, quota, and network; no automatic retry.") from None
    ordered = sorted(response.data, key=lambda item: item.index)
    if [item.index for item in ordered] != list(range(len(texts))):
        raise ValueError("API response did not match input ordering/count.")
    vectors = [item.embedding for item in ordered]
    for vector in vectors:
        validate_vector(vector, dimensions)
    return vectors, response.usage.total_tokens


def embed(work, source, config):
    output = work / "embeddings/embeddings.json"
    if output.exists():
        raise ValueError("Embeddings already exist. Review progress and history before a deliberate rerun.")
    records, digest = load_records(work, source, config)
    model, dimensions = config["embedding_model"], config["embedding_dimensions"]
    vectors, total_tokens = [], 0
    batch_size = config["embedding_batch_size"]
    print(f"Sending {len(records)} chunks to OpenAI using {model}, {dimensions} dimensions.")
    for start in range(0, len(records), batch_size):
        batch = records[start:start + batch_size]
        batch_vectors, tokens = embed_texts([r["text"] for r in batch], model, dimensions)
        vectors.extend(batch_vectors)
        total_tokens += tokens
        print(f"Embedded {len(vectors)}/{len(records)} chunks; reported tokens so far: {total_tokens}")
    payload = {"source_id": source, "model": model, "dimensions": dimensions,
               "records_sha256": digest, "usage_total_tokens": total_tokens,
               "items": [{"chunk_id": r["chunk_id"], "vector": v} for r, v in zip(records, vectors)]}
    write_new(output, payload)
    print(f"Saved {output}")


def build_index(work, source, config):
    output = work / "index/knowledge.sqlite3"
    if output.exists():
        raise ValueError("Index exists. Preserve it under history before a deliberate rerun.")
    records, digest = load_records(work, source, config)
    payload = read_json(work / "embeddings/embeddings.json")
    if payload.get("source_id") != source or payload.get("records_sha256") != digest:
        raise ValueError("Embeddings are stale or belong to another source.")
    if payload.get("model") != config["embedding_model"] or payload.get("dimensions") != config["embedding_dimensions"]:
        raise ValueError("Embedding configuration changed. Regenerate embeddings explicitly.")
    items = payload["items"]
    vectors = {item["chunk_id"]: item["vector"] for item in items}
    if len(vectors) != len(items) or set(vectors) != {r["chunk_id"] for r in records}:
        raise ValueError("Embedding IDs do not match chunks.")
    for vector in vectors.values():
        validate_vector(vector, payload["dimensions"])
    output.parent.mkdir(parents=True, exist_ok=True)
    handle, temporary = tempfile.mkstemp(prefix="index-", suffix=".tmp", dir=output.parent)
    os.close(handle)
    try:
        with closing(sqlite3.connect(temporary)) as connection, connection:
            connection.execute("CREATE TABLE config (key TEXT PRIMARY KEY, value TEXT NOT NULL)")
            connection.execute("CREATE TABLE chunks (id TEXT PRIMARY KEY, record_json TEXT NOT NULL, vector_json TEXT NOT NULL)")
            settings = {key: payload[key] for key in ("source_id", "model", "dimensions", "records_sha256")}
            connection.executemany("INSERT INTO config VALUES (?, ?)", [(key, json.dumps(value)) for key, value in settings.items()])
            connection.executemany("INSERT INTO chunks VALUES (?, ?, ?)",
                                   [(r["chunk_id"], json.dumps(r, ensure_ascii=False), json.dumps(vectors[r["chunk_id"]])) for r in records])
        os.replace(temporary, output)
    finally:
        if os.path.exists(temporary):
            os.unlink(temporary)
    print(f"Stored {len(records)} chunks in {output}. Retrieval uses exact cosine ranking.")


def cosine(left, right):
    if len(left) != len(right):
        raise ValueError("Query and stored vector dimensions differ.")
    denominator = math.sqrt(sum(x*x for x in left)) * math.sqrt(sum(y*y for y in right))
    if denominator == 0:
        raise ValueError("Cannot compare zero vectors.")
    return sum(x*y for x, y in zip(left, right)) / denominator


def rank(work, source, config, query_vector):
    _, digest = load_records(work, source, config)
    database = work / "index/knowledge.sqlite3"
    connection = sqlite3.connect(database.resolve().as_uri() + "?mode=ro", uri=True)
    try:
        settings = {key: json.loads(value) for key, value in connection.execute("SELECT key, value FROM config")}
        if settings["source_id"] != source or settings["records_sha256"] != digest:
            raise ValueError("Index is stale or belongs to another source.")
        if settings["model"] != config["embedding_model"] or settings["dimensions"] != config["embedding_dimensions"]:
            raise ValueError("Index configuration differs from workshop.json.")
        validate_vector(query_vector, settings["dimensions"])
        results = []
        for record_json, vector_json in connection.execute("SELECT record_json, vector_json FROM chunks"):
            record, vector = json.loads(record_json), json.loads(vector_json)
            validate_vector(vector, settings["dimensions"])
            results.append({"score": cosine(query_vector, vector), **record})
        return sorted(results, key=lambda r: (-r["score"], r["chunk_id"]))[:config["top_k"]]
    finally:
        connection.close()


def search(work, source, config, question):
    if not question.strip() or len(question) > 2000:
        raise ValueError("Use a nonempty question of at most 2000 characters.")
    # Preflight the index before making a paid request.
    probe = [1.0] + [0.0] * (config["embedding_dimensions"] - 1)
    rank(work, source, config, probe)
    print("Sending the query to OpenAI for embedding; answer generation remains in your AI session.")
    vectors, tokens = embed_texts([question], config["embedding_model"], config["embedding_dimensions"])
    results = rank(work, source, config, vectors[0])
    output = work / "evaluation" / f"search-{uuid.uuid4().hex[:12]}.json"
    write_new(output, {"question": question, "source_id": source, "model": config["embedding_model"],
                       "query_tokens": tokens, "results": results})
    for i, result in enumerate(results, 1):
        print(f"{i}. {result['chunk_id']} | cosine={result['score']:.4f} | {result['source_file']}")
        print(result["text"][:300])
    print(f"Saved complete evidence: {output}. Similarity is not answer confidence.")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("operation", choices=("embed", "index", "search"))
    parser.add_argument("source")
    parser.add_argument("question", nargs="?")
    args = parser.parse_args()
    try:
        config = read_json(ROOT / "workshop.json")
        work = source_workspace(args.source)
        if args.operation == "embed":
            embed(work, args.source, config)
        elif args.operation == "index":
            build_index(work, args.source, config)
        elif args.question is None:
            parser.error("search requires a quoted question")
        else:
            search(work, args.source, config, args.question)
    except (ValueError, RuntimeError, OSError, KeyError, TypeError, sqlite3.Error) as error:
        parser.exit(1, f"Step stopped: {error}\n")


if __name__ == "__main__":
    main()
