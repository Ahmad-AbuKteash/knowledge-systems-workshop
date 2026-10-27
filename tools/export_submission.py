"""Export one completed source for review/commit; never execute a workshop step."""
import argparse
import json
from pathlib import Path
import shutil
import tempfile
from retrieval import ROOT, read_json, sha, source_workspace, load_records, validate_vector


def export(source):
    work = source_workspace(source, ROOT)
    config = read_json(ROOT / "workshop.json")
    progress = read_json(work / "progress.json")
    for command in config["commands"]:
        if progress.get("steps", {}).get(command["name"], {}).get("status") != "complete":
            raise ValueError(f"Complete and inspect {command['name']} before exporting.")
    records, digest = load_records(work, source, config)
    payload = read_json(work / "embeddings/embeddings.json")
    if payload.get("records_sha256") != digest or payload.get("source_id") != source:
        raise ValueError("Embeddings do not match current chunks.")
    if payload.get("model") != config["embedding_model"] or payload.get("dimensions") != config["embedding_dimensions"]:
        raise ValueError("Embedding settings changed.")
    items = payload["items"]
    vectors = {item["chunk_id"]: item["vector"] for item in items}
    if len(vectors) != len(items) or set(vectors) != {r["chunk_id"] for r in records}:
        raise ValueError("Embedding IDs do not match chunks.")
    for value in vectors.values():
        validate_vector(value, config["embedding_dimensions"])
    # Reuse the index preflight without making an API request or recording results.
    from retrieval import rank
    rank(work, source, config, [1.0] + [0.0] * (config["embedding_dimensions"]-1))
    review = work / "evaluation/review.md"
    if not review.is_file() or not review.read_text(encoding="utf-8-sig").strip():
        raise ValueError("Retrieval review is missing.")
    output = ROOT / "submissions" / source
    if output.exists():
        raise ValueError("Submission already exists. Review/preserve it before a deliberate replacement.")
    output.parent.mkdir(parents=True, exist_ok=True)
    temporary = Path(tempfile.mkdtemp(prefix=".export-", dir=output.parent))
    try:
        bundle = {"schema_version": 1, "source_id": source,
                  "embedding_model": payload["model"], "dimensions": payload["dimensions"],
                  "records_sha256": digest,
                  "records": [{**r, "vector": vectors[r["chunk_id"]]} for r in records]}
        (temporary / "bundle.json").write_text(json.dumps(bundle, ensure_ascii=False, allow_nan=False), encoding="utf-8")
        shutil.copyfile(review, temporary / "review.md")
        temporary.rename(output)
    except Exception:
        # Only remove this function's own temporary directory, not a submission.
        shutil.rmtree(temporary)
        raise
    print(f"Exported {len(records)} passages to {output}.")
    print("Review bundle.json and review.md for accuracy and secrets before staging only this source folder.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("source")
    args = parser.parse_args()
    try:
        export(args.source)
    except (ValueError, OSError, KeyError, TypeError) as error:
        parser.exit(1, f"Export stopped: {error}\n")
