"""Submission handoff checks using temporary synthetic fixtures only."""
import json
import sys
from pathlib import Path
import unittest
from unittest.mock import patch
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "tools"))
import export_submission
import test_retrieval as fixtures
retrieval = fixtures.retrieval


class ExportTests(unittest.TestCase):
    def setUp(self):
        self.fixture = fixtures.RetrievalTests()
        self.fixture.setUp()
        self.addCleanup(self.fixture.tearDown)
        f = self.fixture
        f.config["commands"] = [{"name": name} for name in ["collect", "test-retrieval"]]
        retrieval.write_new(f.root / "workshop.json", f.config)
        retrieval.write_new(f.work / "progress.json", {"steps": {name: {"status": "complete"} for name in ["collect", "test-retrieval"]}})
        (f.work / "evaluation").mkdir()
        (f.work / "evaluation/review.md").write_text("Synthetic fixture review.", encoding="utf-8")
        f.embed_fixture()
        retrieval.build_index(f.work, "source-01", f.config)

    def test_export_preserves_vectors_and_review_without_api(self):
        f = self.fixture
        with patch.object(export_submission, "ROOT", f.root):
            export_submission.export("source-01")
            with self.assertRaisesRegex(ValueError, "already exists"):
                export_submission.export("source-01")
        data = json.loads((f.root / "submissions/source-01/bundle.json").read_text())
        self.assertEqual(data["records"][0]["vector"], [1, 0, 0])
        self.assertTrue((f.root / "submissions/source-01/review.md").is_file())
        self.assertFalse((f.root / "submissions/source-01/progress.json").exists())

    def test_incomplete_work_does_not_export(self):
        f = self.fixture
        (f.work / "progress.json").write_text('{"steps":{}}')
        with patch.object(export_submission, "ROOT", f.root), self.assertRaisesRegex(ValueError, "Complete"):
            export_submission.export("source-01")
        self.assertFalse((f.root / "submissions/source-01").exists())
