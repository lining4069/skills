import re
from pathlib import Path
import unittest


REPO_ROOT = Path(__file__).resolve().parents[1]
SKILLS_DIR = REPO_ROOT / "skills"
SKILL_DIR = SKILLS_DIR / "second-brain"


class SkillPackageTests(unittest.TestCase):
    def test_skill_frontmatter_is_portable_and_valid(self):
        content = (SKILL_DIR / "SKILL.md").read_text()
        match = re.match(r"^---\n(.*?)\n---\n", content, re.DOTALL)
        self.assertIsNotNone(match, "SKILL.md must start with YAML frontmatter")

        frontmatter = {}
        for line in match.group(1).splitlines():
            key, value = line.split(":", 1)
            frontmatter[key.strip()] = value.strip()

        self.assertEqual(frontmatter["name"], "second-brain")
        self.assertIn("LLM wiki", frontmatter["description"])
        self.assertLessEqual(len(frontmatter["description"]), 1024)

    def test_publish_files_do_not_contain_local_machine_paths(self):
        local_path_patterns = [
            "/Users/lining/",
            "/Users/ambrosino/",
        ]
        for path in SKILL_DIR.rglob("*"):
            if not path.is_file():
                continue
            if path.suffix not in {".md", ".py", ".yaml", ".yml"}:
                continue
            text = path.read_text(errors="ignore")
            for pattern in local_path_patterns:
                self.assertNotIn(pattern, text, str(path.relative_to(REPO_ROOT)))

    def test_required_publish_files_exist(self):
        for relative in [
            "README.md",
            "LICENSE",
            ".gitignore",
            "skills/second-brain/SKILL.md",
            "skills/second-brain/scripts/second_brain.py",
            "skills/second-brain/references/methodology.md",
            "skills/second-brain/references/wiki-conventions.md",
            "skills/second-brain/assets/wiki-page-template.md",
            "skills/second-brain/assets/source-page-template.md",
            "skills/second-brain/agents/openai.yaml",
        ]:
            self.assertTrue((REPO_ROOT / relative).is_file(), relative)

    def test_every_skill_lives_under_skills_directory(self):
        skill_files = sorted(path.relative_to(REPO_ROOT) for path in SKILLS_DIR.glob("*/SKILL.md"))

        self.assertEqual(skill_files, [Path("skills/second-brain/SKILL.md")])


if __name__ == "__main__":
    unittest.main()
