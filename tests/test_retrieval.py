"""Offline behavior tests. Synthetic vectors are fixtures, never API results."""
import importlib.util
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

SPEC = importlib.util.spec_from_file_location("retrieval", Path(__file__).resolve().parents[1] / "tools/retrieval.py")
retrieval = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(retrieval)


class RetrievalTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        (self.root / "sources/source-01").mkdir(parents=True)
        self.work = retrieval.source_workspace("source-01", self.root)
        self.config = {"embedding_model": "text-embedding-3-small", "embedding_dimensions": 3,
                       "embedding_batch_size": 1, "top_k": 2,
                       "max_chunk_characters": 2000, "max_chunks_per_source": 500}
        docs, records = [], []
        for number, text in enumerate(("Current limit is USD 85.", "Historic limit was USD 60.")):
            doc = {"document_id": f"doc-{number}", "source_id": "source-01",
                   "source_file": f"sources/source-01/policy-{number}.md", "text": text,
                   "metadata": {"version": str(number), "owner": None}}
            docs.append(doc)
            records.append({**doc, "chunk_id": f"chunk-{number}", "section": "Policy",
                            "start": 0, "end": len(text)})
        self.docs_path = self.work / "knowledge/documents.json"
        retrieval.write_new(self.docs_path, docs)
        retrieval.write_new(self.work / "knowledge/validation.json", {
            "passed": True, "documents_sha256": retrieval.sha(self.docs_path)})
        self.records_path = self.work / "chunks/records.json"
        retrieval.write_new(self.records_path, records)

    def tearDown(self):
        self.temp.cleanup()

    def embed_fixture(self):
        with patch.object(retrieval, "embed_texts", side_effect=[([[1., 0., 0.]], 7), ([[0., 1., 0.]], 8)]) as call:
            retrieval.embed(self.work, "source-01", self.config)
            self.assertEqual(call.call_count, 2)

    def test_separate_embedding_index_and_ranking(self):
        self.embed_fixture()
        self.assertFalse((self.work / "index/knowledge.sqlite3").exists())
        payload = retrieval.read_json(self.work / "embeddings/embeddings.json")
        self.assertEqual(payload["usage_total_tokens"], 15)
        retrieval.build_index(self.work, "source-01", self.config)
        results = retrieval.rank(self.work, "source-01", self.config, [1., 0., 0.])
        self.assertEqual(results[0]["chunk_id"], "chunk-0")
        self.assertAlmostEqual(results[0]["score"], 1.)
        self.assertEqual(results[0]["source_file"], "sources/source-01/policy-0.md")
        with self.assertRaises(ValueError):
            retrieval.build_index(self.work, "source-01", self.config)

    def test_changed_knowledge_blocks_embedding(self):
        self.docs_path.write_text("[]", encoding="utf-8")
        with patch.object(retrieval, "embed_texts") as call, self.assertRaisesRegex(ValueError, "stale"):
            retrieval.embed(self.work, "source-01", self.config)
        call.assert_not_called()

    def test_wrong_source_and_metadata_block_embedding(self):
        records = retrieval.read_json(self.records_path)
        records[0]["metadata"]["version"] = "invented"
        self.records_path.write_text(json.dumps(records), encoding="utf-8")
        with self.assertRaisesRegex(ValueError, "metadata"):
            retrieval.load_records(self.work, "source-01", self.config)
        records[0]["source_id"] = "source-02"
        self.records_path.write_text(json.dumps(records), encoding="utf-8")
        with self.assertRaisesRegex(ValueError, "source"):
            retrieval.load_records(self.work, "source-01", self.config)

    def test_stale_index_rejected_before_paid_query(self):
        self.embed_fixture()
        retrieval.build_index(self.work, "source-01", self.config)
        records = retrieval.read_json(self.records_path)
        records[0]["section"] = "Renamed section"
        self.records_path.write_text(json.dumps(records), encoding="utf-8")
        with patch.object(retrieval, "embed_texts") as call, self.assertRaisesRegex(ValueError, "stale"):
            retrieval.search(self.work, "source-01", self.config, "What is the limit?")
        call.assert_not_called()

    def test_failed_api_writes_no_embedding_artifact(self):
        with patch.object(retrieval, "embed_texts", side_effect=RuntimeError("fixture failure")), self.assertRaises(RuntimeError):
            retrieval.embed(self.work, "source-01", self.config)
        self.assertFalse((self.work / "embeddings/embeddings.json").exists())

    def test_search_persists_evidence(self):
        self.embed_fixture()
        retrieval.build_index(self.work, "source-01", self.config)
        with patch.object(retrieval, "embed_texts", return_value=([[1., 0., 0.]], 3)):
            retrieval.search(self.work, "source-01", self.config, "Current limit?")
        paths = list((self.work / "evaluation").glob("search-*.json"))
        self.assertEqual(len(paths), 1)
        saved = retrieval.read_json(paths[0])
        self.assertEqual(saved["query_tokens"], 3)
        self.assertEqual(saved["results"][0]["text"], "Current limit is USD 85.")

    def test_path_and_vector_guards(self):
        for source in ("../source-01", "source-01/../../", "source-99"):
            with self.assertRaises(ValueError):
                retrieval.source_workspace(source, self.root)
        for vector in ([0., 0., 0.], [1., float("nan"), 0.], [1., 0.], [True, 1., 0.]):
            with self.assertRaises(ValueError):
                retrieval.validate_vector(vector, 3)


if __name__ == "__main__":
    unittest.main()
