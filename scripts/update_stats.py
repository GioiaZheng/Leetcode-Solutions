from pathlib import Path
import re

ROOT = Path(__file__).resolve().parent.parent
README = ROOT / "README.md"

def count_solved_problems():
    count = 0
    for item in ROOT.iterdir():
        if item.is_dir() and re.match(r"^\d{4,}-", item.name):
            count += 1
    return count

def update_readme(count):
    content = README.read_text(encoding="utf-8")

    updated = re.sub(
        r"(<!-- SOLVED_COUNT_START -->)(.*?)(<!-- SOLVED_COUNT_END -->)",
        rf"\g<1>{count}\g<3>",
        content,
        flags=re.DOTALL,
    )

    if content == updated:
        raise ValueError("Placeholder not found in README.")

    README.write_text(updated, encoding="utf-8")

if __name__ == "__main__":
    solved = count_solved_problems()
    update_readme(solved)
    print(f"Updated solved problems: {solved}")
