"""Verify that the repository instructions preserve the requested policies."""

from pathlib import Path
import unittest


class RepositoryPolicyTests(unittest.TestCase):
    def test_required_policies_are_present(self):
        root = Path(__file__).resolve().parents[1]
        lines = (root / "AGENTS.md").read_text(encoding="utf-8").splitlines()
        required_lines = (
            "### 注意事项",
            "- 每次改动完成后，都必须创建一个对应的Gitcommit，以便后续追踪和回滚。",
            "- 每次改动后，都必须编写或更新相关测试，并在交付给用户前，确保所有测试和验证全部通过",
        )
        for line in required_lines:
            with self.subTest(policy=line):
                self.assertIn(line, lines)


if __name__ == "__main__":
    unittest.main()
