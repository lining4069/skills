import json
import subprocess
import sys
import tempfile
from pathlib import Path
import unittest


REPO_ROOT = Path(__file__).resolve().parents[1]
SCRIPT = REPO_ROOT / "skills" / "second-brain" / "scripts" / "second_brain.py"


class SecondBrainCliTests(unittest.TestCase):
    def run_cli(self, *args, expect_code=0, cwd=None):
        result = subprocess.run(
            [sys.executable, str(SCRIPT), *args],
            capture_output=True,
            text=True,
            check=False,
            cwd=cwd,
        )
        self.assertEqual(
            result.returncode,
            expect_code,
            msg=f"stdout:\n{result.stdout}\nstderr:\n{result.stderr}",
        )
        return result

    def test_init_creates_agent_files_and_wiki_skeleton(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)

            self.run_cli("init", "--root", str(root))

            for relative in [
                "raw/inbox",
                "raw/archive",
                "wiki/entities",
                "wiki/concepts",
                "wiki/projects",
                "wiki/questions",
                "wiki/sources",
                "schema",
                "logs",
            ]:
                self.assertTrue((root / relative).is_dir(), relative)

            for relative in [
                "AGENTS.md",
                "CLAUDE.md",
                "second-brain.yaml",
                "wiki/index.md",
                "logs/events.jsonl",
                "logs/backlog.md",
                "schema/wiki-page.md",
            ]:
                self.assertTrue((root / relative).is_file(), relative)

            self.assertIn("/second-brain-ingest", (root / "AGENTS.md").read_text())
            self.assertIn("/second-brain-ingest", (root / "CLAUDE.md").read_text())
            self.assertIn("# Second Brain Index", (root / "wiki/index.md").read_text())

    def test_init_and_health_default_to_current_directory(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)

            self.run_cli("init", cwd=root)
            result = self.run_cli("health", "--json", cwd=root)
            report = json.loads(result.stdout)

            self.assertTrue((root / "wiki" / "index.md").is_file())
            self.assertTrue(report["ok"])
            self.assertEqual(report["summary"]["errors"], 0)


    def test_register_source_appends_to_logs_events_jsonl(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            source = root / "My Note.md"
            source.write_text("# My Note\n\nA useful observation.\n")

            self.run_cli("register-source", str(source), "--root", str(root))

            events = (root / "logs" / "events.jsonl").read_text().strip().splitlines()
            self.assertEqual(len(events), 1)
            event = json.loads(events[0])
            self.assertEqual(event["event"], "ingest-registered")
            self.assertEqual(event["subject"], "My Note")
            self.assertTrue(event["source"].startswith("raw/inbox/"))
            self.assertFalse((root / "wiki" / "log.md").exists())

    def test_health_reports_missing_required_file(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            self.run_cli("init", "--root", str(root))
            (root / "logs" / "backlog.md").unlink()

            result = self.run_cli("health", "--root", str(root), "--json", expect_code=1)
            report = json.loads(result.stdout)

            self.assertTrue(
                any(
                    issue["severity"] == "error"
                    and issue["code"] == "missing-required-file"
                    and issue["path"] == "logs/backlog.md"
                    for issue in report["issues"]
                )
            )

    def test_health_passes_after_fresh_init(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            self.run_cli("init", "--root", str(root))

            result = self.run_cli("health", "--root", str(root), "--json")
            report = json.loads(result.stdout)

            self.assertTrue(report["ok"])
            self.assertEqual(report["summary"]["errors"], 0)

    def test_health_detects_broken_wikilink(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            self.run_cli("init", "--root", str(root))
            page = root / "wiki" / "concepts" / "foo.md"
            page.write_text(
                "---\n"
                "title: Foo\n"
                "type: concept\n"
                "updated: 2026-04-23\n"
                "confidence: medium\n"
                "sources: []\n"
                "---\n\n"
                "# Foo\n\n"
                "This points to [[missing-page]].\n"
            )

            result = self.run_cli("health", "--root", str(root), "--json", expect_code=1)
            report = json.loads(result.stdout)

            self.assertTrue(
                any(
                    issue["severity"] == "error"
                    and issue["code"] == "broken-wikilink"
                    and issue["target"] == "missing-page"
                    for issue in report["issues"]
                )
            )


if __name__ == "__main__":
    unittest.main()
