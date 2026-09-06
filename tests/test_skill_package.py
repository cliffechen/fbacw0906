"""Check that the portable skill includes its entry point and linked resources."""

from pathlib import Path
import re
import unittest
from urllib.parse import unquote, urlsplit


SKILL_ROOT = Path(__file__).resolve().parents[1] / "amazon-supplement-copywriting"


class SkillPackageTests(unittest.TestCase):
    def test_skill_entry_point_preserves_its_identity(self):
        text = (SKILL_ROOT / "SKILL.md").read_text(encoding="utf-8")
        frontmatter = re.match(r"\A---\n(.*?)\n---(?:\n|$)", text, re.DOTALL)
        self.assertIsNotNone(frontmatter, "SKILL.md needs YAML frontmatter")
        header = frontmatter.group(1)
        self.assertRegex(header, r"(?m)^name: amazon-supplement-copywriting$")
        self.assertRegex(header, r"(?m)^description: \S.+$")

    def test_document_links_are_present_in_the_portable_package(self):
        documents = [SKILL_ROOT / "SKILL.md"]
        for folder in ("references", "assets", "evals"):
            documents.extend((SKILL_ROOT / folder).rglob("*.md"))
        package_root = SKILL_ROOT.resolve()
        for document in documents:
            text = document.read_text(encoding="utf-8")
            for raw_target in re.findall(r"\]\(([^)]+)\)", text):
                target_url = urlsplit(raw_target)
                if target_url.scheme in {"https", "http"}:
                    continue
                with self.subTest(document=document.name, target=raw_target):
                    self.assertFalse(target_url.scheme, "Use relative file links")
                    target = (document.parent / unquote(target_url.path)).resolve()
                    self.assertTrue(target.is_relative_to(package_root))
                    self.assertTrue(target.is_file(), f"Missing linked file: {target}")

    def test_readme_navigation_resolves_within_repository(self):
        repository = SKILL_ROOT.parent.resolve()
        readme = repository / "README.md"
        text = readme.read_text(encoding="utf-8")
        links = re.findall(r"\]\(([^)]+)\)", text)
        self.assertTrue(links, "README must link to project documentation")
        for raw_target in links:
            url = urlsplit(raw_target)
            if url.scheme in {"https", "http"}:
                continue
            with self.subTest(target=raw_target):
                self.assertFalse(url.scheme, "Use portable relative links")
                self.assertFalse(Path(url.path).is_absolute())
                target = (repository / unquote(url.path)).resolve()
                self.assertTrue(target.is_relative_to(repository))
                self.assertTrue(target.is_file(), f"Broken README link: {target}")


if __name__ == "__main__":
    unittest.main()
