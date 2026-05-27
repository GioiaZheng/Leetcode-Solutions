import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PROBLEMS_ROOT = ROOT / "problems"
README = ROOT / "README.md"
CATALOG = ROOT / "CATALOG.md"
METADATA = ROOT / "metadata.json"

PROBLEM_DIR_RE = re.compile(r"^(\d{4,})-.+")
CATALOG_ENTRY_RE = re.compile(r"^\|\s*\d{4}\s*\|")

METRIC_MARKERS = {
    "problem_directories": ("<!-- PROBLEM_DIRS_START -->", "<!-- PROBLEM_DIRS_END -->"),
    "standard_solutions": (
        "<!-- STANDARD_SOLUTIONS_START -->",
        "<!-- STANDARD_SOLUTIONS_END -->",
    ),
    "catalog_entries": ("<!-- CATALOG_ENTRIES_START -->", "<!-- CATALOG_ENTRIES_END -->"),
    "easy_count": ("<!-- EASY_COUNT_START -->", "<!-- EASY_COUNT_END -->"),
    "medium_count": ("<!-- MEDIUM_COUNT_START -->", "<!-- MEDIUM_COUNT_END -->"),
    "hard_count": ("<!-- HARD_COUNT_START -->", "<!-- HARD_COUNT_END -->"),
    "blind75_count": ("<!-- BLIND75_COUNT_START -->", "<!-- BLIND75_COUNT_END -->"),
    "reviewed_ai_card_count": (
        "<!-- REVIEWED_AI_CARDS_START -->",
        "<!-- REVIEWED_AI_CARDS_END -->",
    ),
}


def problem_directories():
    return sorted(
        item
        for item in PROBLEMS_ROOT.iterdir()
        if item.is_dir()
        and (match := PROBLEM_DIR_RE.match(item.name))
        and int(match.group(1)) > 0
    )


def count_problem_directories():
    return len(problem_directories())


def count_standard_solutions():
    return sum(
        1 for directory in problem_directories() if (directory / "solution.py").is_file()
    )


def count_catalog_entries():
    if not CATALOG.is_file():
        return 0

    return sum(
        1
        for line in CATALOG.read_text(encoding="utf-8").splitlines()
        if CATALOG_ENTRY_RE.match(line)
    )


def difficulty_counts():
    counts = {"Easy": 0, "Medium": 0, "Hard": 0}
    if not METADATA.is_file():
        return counts

    data = json.loads(METADATA.read_text(encoding="utf-8"))
    for problem in data.get("problems", []):
        difficulty = problem.get("difficulty")
        if difficulty in counts:
            counts[difficulty] += 1

    return counts


def blind75_count():
    if not METADATA.is_file():
        return 0
    data = json.loads(METADATA.read_text(encoding="utf-8"))
    return sum(
        1
        for problem in data.get("problems", [])
        if "blind75" in (problem.get("path_membership") or [])
    )


def reviewed_ai_card_count():
    if not METADATA.is_file():
        return 0
    data = json.loads(METADATA.read_text(encoding="utf-8"))
    return sum(
        1
        for problem in data.get("problems", [])
        if problem.get("ai_card_status") == "reviewed"
    )


def collect_metrics():
    difficulties = difficulty_counts()
    return {
        "problem_directories": count_problem_directories(),
        "standard_solutions": count_standard_solutions(),
        "catalog_entries": count_catalog_entries(),
        "easy_count": difficulties["Easy"],
        "medium_count": difficulties["Medium"],
        "hard_count": difficulties["Hard"],
        "blind75_count": blind75_count(),
        "reviewed_ai_card_count": reviewed_ai_card_count(),
    }


def update_readme(metrics):
    content = README.read_text(encoding="utf-8")

    for name, count in metrics.items():
        start, end = METRIC_MARKERS[name]
        pattern = re.escape(start) + r".*?" + re.escape(end)
        if not re.search(pattern, content, flags=re.DOTALL):
            raise ValueError(
                f"Placeholder not found in README. Expected: {start}...{end}"
            )
        replacement = f"{start}{count}{end}"
        content = re.sub(pattern, replacement, content, flags=re.DOTALL)

    README.write_text(content, encoding="utf-8")


if __name__ == "__main__":
    metrics = collect_metrics()
    update_readme(metrics)
    print("Updated README metrics:")
    for name, count in metrics.items():
        print(f"- {name}: {count}")
