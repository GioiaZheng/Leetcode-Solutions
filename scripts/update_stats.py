from pathlib import Path
import re

ROOT = Path(__file__).resolve().parent.parent
README = ROOT / "README.md"

START = "<!-- SOLVED_COUNT_START -->"
END = "<!-- SOLVED_COUNT_END -->"

def count_solved_problems():
    count = 0
    for item in ROOT.iterdir():
        if item.is_dir():
            m = re.match(r"^(\d{4,})-", item.name)
            if m and int(m.group(1)) > 0:
                count += 1
    return count

def update_readme(count):
    content = README.read_text(encoding="utf-8")

    pattern = re.escape(START) + r".*?" + re.escape(END)
    if not re.search(pattern, content, flags=re.DOTALL):
        raise ValueError(
            f"Placeholder not found in README. Expected: {START}...{END}"
        )

    replacement = f"{START}{count}{END}"
    updated = re.sub(pattern, replacement, content, flags=re.DOTALL)

    README.write_text(updated, encoding="utf-8")

if __name__ == "__main__":
    solved = count_solved_problems()
    update_readme(solved)
    print(f"Updated solved problems: {solved}")
