import re
from pathlib import Path
import unittest


REPO_ROOT = Path(__file__).resolve().parents[1]
SKILLS_DIR = REPO_ROOT / "skills"
EXPECTED_SKILLS = {
    "second-brain": "LLM wiki",
    "project-bootstrap": "approved `PRD.md`",
    "brainstorm-to-prd": "PRD.md",
    "prd-to-bootstrap": "PRODUCT_SPEC.md",
    "bootstrap-harness": "harness",
    "first-plan-seeder": ".agent/active-plans",
}


class SkillPackageTests(unittest.TestCase):
    def test_skill_frontmatter_is_portable_and_valid(self):
        for skill_name, expected_phrase in EXPECTED_SKILLS.items():
            content = (SKILLS_DIR / skill_name / "SKILL.md").read_text()
            match = re.match(r"^---\n(.*?)\n---\n", content, re.DOTALL)
            self.assertIsNotNone(match, f"{skill_name} must start with YAML frontmatter")

            frontmatter = {}
            for line in match.group(1).splitlines():
                key, value = line.split(":", 1)
                frontmatter[key.strip()] = value.strip()

            self.assertEqual(frontmatter["name"], skill_name)
            self.assertIn(expected_phrase, frontmatter["description"])
            self.assertLessEqual(len(frontmatter["description"]), 1024)

    def test_publish_files_do_not_contain_local_machine_paths(self):
        local_path_patterns = [
            "/Users/lining/",
            "/Users/ambrosino/",
        ]
        for skill_name in EXPECTED_SKILLS:
            skill_dir = SKILLS_DIR / skill_name
            for path in skill_dir.rglob("*"):
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
            "README.zh-CN.md",
            "LICENSE",
            ".gitignore",
            "skills/second-brain/SKILL.md",
            "skills/second-brain/scripts/second_brain.py",
            "skills/second-brain/references/methodology.md",
            "skills/second-brain/references/wiki-conventions.md",
            "skills/second-brain/assets/wiki-page-template.md",
            "skills/second-brain/assets/source-page-template.md",
            "skills/second-brain/agents/openai.yaml",
            "skills/project-bootstrap/SKILL.md",
            "skills/project-bootstrap/references/PRD_TEMPLATE.md",
            "skills/brainstorm-to-prd/SKILL.md",
            "skills/brainstorm-to-prd/references/PRD_TEMPLATE.md",
            "skills/brainstorm-to-prd/references/SECTION_GUIDE.md",
            "skills/prd-to-bootstrap/SKILL.md",
            "skills/prd-to-bootstrap/references/PRODUCT_SPEC_TEMPLATE.md",
            "skills/prd-to-bootstrap/references/HARNESS_BOOTSTRAP_TEMPLATE.md",
            "skills/prd-to-bootstrap/references/REQUIRED_FIELDS.md",
            "skills/bootstrap-harness/SKILL.md",
            "skills/bootstrap-harness/assets/harness-instantiator/harness-base/AGENTS.md",
            "skills/bootstrap-harness/assets/harness-instantiator/harness-base/docs/api/API_CONTRACT.md",
            "skills/bootstrap-harness/assets/harness-instantiator/templates/PRODUCT_SPEC.template.md",
            "skills/bootstrap-harness/assets/harness-instantiator/templates/HARNESS_BOOTSTRAP.template.md",
            "skills/bootstrap-harness/assets/harness-instantiator/project-bootstrap-checklist.md",
            "skills/first-plan-seeder/SKILL.md",
            "tutorial/project-bootstrap/claude-example.md",
            "tutorial/project-bootstrap/plugin-skeleton.md",
        ]:
            self.assertTrue((REPO_ROOT / relative).is_file(), relative)

    def test_every_skill_lives_under_skills_directory(self):
        skill_files = sorted(path.relative_to(REPO_ROOT) for path in SKILLS_DIR.glob("*/SKILL.md"))

        self.assertEqual(
            skill_files,
            [
                Path("skills/bootstrap-harness/SKILL.md"),
                Path("skills/brainstorm-to-prd/SKILL.md"),
                Path("skills/first-plan-seeder/SKILL.md"),
                Path("skills/prd-to-bootstrap/SKILL.md"),
                Path("skills/project-bootstrap/SKILL.md"),
                Path("skills/second-brain/SKILL.md"),
            ],
        )

    def test_bootstrap_harness_bundles_portable_instantiator_snapshot(self):
        base = SKILLS_DIR / "bootstrap-harness" / "assets" / "harness-instantiator"
        self.assertTrue((base / "harness-base" / "AGENTS.md").is_file())
        self.assertTrue((base / "harness-base" / ".agent" / "PLANS.md").is_file())
        self.assertTrue((base / "templates" / "CLAUDE.template.md").is_file())
        self.assertTrue((base / "project-bootstrap-checklist.md").is_file())

    def test_tutorials_do_not_contain_personal_machine_paths(self):
        tutorial_dir = REPO_ROOT / "tutorial"
        for path in tutorial_dir.rglob("*.md"):
            text = path.read_text(errors="ignore")
            self.assertNotIn("/Users/lining/", text, str(path.relative_to(REPO_ROOT)))


if __name__ == "__main__":
    unittest.main()
