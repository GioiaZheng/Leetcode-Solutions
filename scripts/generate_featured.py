import json
import re
from pathlib import Path

from generate_topics import category_for

ROOT = Path(__file__).resolve().parent.parent
README = ROOT / "README.md"
METADATA = ROOT / "metadata.json"
PROBLEMS_DIR = ROOT / "problems"

LIST_SENTINEL_START = "<!-- FEATURED_LIST_START -->"
LIST_SENTINEL_END = "<!-- FEATURED_LIST_END -->"

SENTINEL_RE = re.compile(
    re.escape(LIST_SENTINEL_START) + r".*?" + re.escape(LIST_SENTINEL_END),
    re.DOTALL,
)

PROBLEM_DIR_RE = re.compile(r"^(\d{4,})-(.+)$")

EMPTY_BODY = (
    "_No problems carry `ai_card_status: reviewed` yet. "
    "Migrate a problem README to the AI-card template (see CONTRIBUTING.md) "
    "and set `ai_card_status: reviewed` to populate this list._"
)


def load_problems():
    if not METADATA.is_file():
        raise FileNotFoundError("metadata.json is missing from the repository root.")
    data = json.loads(METADATA.read_text(encoding="utf-8"))
    problems = data.get("problems")
    if not isinstance(problems, list):
        raise ValueError("metadata.json must contain a 'problems' list.")
    return problems


def problem_directories():
    if not PROBLEMS_DIR.is_dir():
        return {}
    by_id = {}
    for path in PROBLEMS_DIR.iterdir():
        if not path.is_dir():
            continue
        match = PROBLEM_DIR_RE.match(path.name)
        if not match:
            continue
        by_id[match.group(1)] = path.name
    return by_id


# Most specific first. When a problem maps to multiple canonical categories,
# the one earliest in this list wins: e.g. (Array, Two Pointers) -> "Two
# Pointers & Sliding Window" rather than the catch-all "Arrays & Matrices".
PRIMARY_CATEGORY_SPECIFICITY = (
    "Linked Lists",
    "Graph & Tree",
    "Dynamic Programming",
    "Backtracking & Search",
    "Stack & Monotonic Structures",
    "Prefix & Difference Techniques",
    "Two Pointers & Sliding Window",
    "Binary Search",
    "Sorting & Heap",
    "Hashing",
    "Greedy",
    "Advanced Data Structures",
    "Math & Counting",
    "Geometry",
    "Simulation",
    "Strings",
    "Arrays & Matrices",
    "Other Techniques",
)


def primary_category(problem):
    topics = problem.get("topics") or []
    categories = {category_for(topic) for topic in topics}
    for category in PRIMARY_CATEGORY_SPECIFICITY:
        if category in categories:
            return category
    return "Other Techniques"


def featured_problems(problems):
    return sorted(
        (p for p in problems if p.get("ai_card_status") == "reviewed"),
        key=lambda p: int(p.get("id", "0")),
    )


def render_featured(problems, directories):
    members = featured_problems(problems)
    if not members:
        return EMPTY_BODY

    lines = [
        "| # | ID | Problem | Difficulty | Primary topic |",
        "|---:|---:|---|---|---|",
    ]
    for index, problem in enumerate(members, start=1):
        problem_id = problem["id"]
        directory = directories.get(problem_id)
        if directory is None:
            raise ValueError(
                f"metadata.json marks problem {problem_id} as ai_card_status: reviewed "
                "but no matching directory exists under problems/."
            )
        title = str(problem.get("title", "")).replace("|", r"\|")
        difficulty = str(problem.get("difficulty", "")).replace("|", r"\|")
        topic = primary_category(problem).replace("|", r"\|")
        lines.append(
            f"| {index} | {problem_id} | "
            f"[{title}](problems/{directory}/) | "
            f"{difficulty} | {topic} |"
        )
    return "\n".join(lines)


def main():
    if not README.is_file():
        raise FileNotFoundError("README.md is missing from the repository root.")

    content = README.read_text(encoding="utf-8")
    if not SENTINEL_RE.search(content):
        raise ValueError(
            f"README.md is missing the {LIST_SENTINEL_START} ... "
            f"{LIST_SENTINEL_END} sentinels."
        )

    problems = load_problems()
    directories = problem_directories()
    body = render_featured(problems, directories)
    replacement = f"{LIST_SENTINEL_START}\n{body}\n{LIST_SENTINEL_END}"
    new_content = SENTINEL_RE.sub(replacement, content, count=1)
    README.write_text(new_content, encoding="utf-8")

    members = featured_problems(problems)
    print(f"Regenerated README featured list with {len(members)} problems.")


if __name__ == "__main__":
    main()
