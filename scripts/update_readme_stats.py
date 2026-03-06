#!/usr/bin/env python3
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parent.parent
README = ROOT / "README.md"


def count_solved_problems() -> int:
    count = 0
    for p in ROOT.iterdir():
        if p.is_dir() and re.match(r"^\d{4}-", p.name) and p.name != "0000-notes":
            count += 1
    return count


def update_readme(problem_count: int) -> None:
    text = README.read_text(encoding="utf-8")

    badge_line = (
        f"![Python](https://img.shields.io/badge/language-python-blue) "
        f"![LeetCode](https://img.shields.io/badge/leetcode-solutions-orange) "
        f"![Problems](https://img.shields.io/badge/problems-{problem_count}-green) "
        f"![License](https://img.shields.io/badge/license-MIT-lightgrey)"
    )

    snapshot_line = f"- **{problem_count} solved problems** organized in standardized directories."

    text, n1 = re.subn(
        r"^!\[Python\]\(https://img\.shields\.io/badge/language-python-blue\).*\n",
        badge_line + "\n",
        text,
        count=1,
        flags=re.M,
    )
    if n1 == 0:
        text = re.sub(r"^(# LeetCode Solutions\n)", r"\1\n" + badge_line + "\n", text, count=1, flags=re.M)

    text, n2 = re.subn(
        r"^- \*\*\d+ solved problems\*\* organized in standardized directories\.\n",
        snapshot_line + "\n",
        text,
        count=1,
        flags=re.M,
    )
    if n2 == 0:
        raise SystemExit("Could not find snapshot solved-problems line in README.md")

    README.write_text(text, encoding="utf-8")


if __name__ == "__main__":
    c = count_solved_problems()
    update_readme(c)
    print(f"Updated README stats: problems={c}")
