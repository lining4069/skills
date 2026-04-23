import json
import subprocess
import sys
import tempfile
from pathlib import Path
import unittest


REPO_ROOT = Path(__file__).resolve().parents[1]
SCRIPT = REPO_ROOT / "skills" / "second-brain" / "scripts" / "second_brain.py"


class SecondBrainCliTests(unittest.TestCase):
    def run_cli(self, *args, expect_code=0):
        result = subprocess.run(
            [sys.executable, str(SCRIPT), *args],
            capture_output=True,
            text=True,
            check=False,
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
                "wiki/log.md",
                "wiki/backlog.md",
                "schema/wiki-page.md",
            ]:
                self.assertTrue((root / relative).is_file(), relative)

            self.assertIn("/second-brain-ingest", (root / "AGENTS.md").read_text())
            self.assertIn("/second-brain-ingest", (root / "CLAUDE.md").read_text())
            self.assertIn("# Second Brain Index", (root / "wiki/index.md").read_text())

    def test_health_reports_missing_required_file(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            self.run_cli("init", "--root", str(root))
            (root / "wiki" / "index.md").unlink()

            result = self.run_cli("health", "--root", str(root), "--json", expect_code=1)
            report = json.loads(result.stdout)

            self.assertTrue(
                any(
                    issue["severity"] == "error"
                    and issue["code"] == "missing-required-file"
                    and issue["path"] == "wiki/index.md"
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
