import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PROBLEMS_ROOT = ROOT / "problems"
CATALOG = ROOT / "CATALOG.md"
METADATA = ROOT / "metadata.json"

PROBLEM_DIR_RE = re.compile(r"^(\d{4,})-(.+)$")
VALID_DIFFICULTIES = {"Easy", "Medium", "Hard"}
VALID_STATUSES = {"solved", "tested", "review-needed"}


def problem_directories():
    return sorted(
        path
        for path in PROBLEMS_ROOT.iterdir()
        if path.is_dir()
        and (match := PROBLEM_DIR_RE.match(path.name))
        and int(match.group(1)) > 0
    )


def escape_table_cell(value):
    return str(value).replace("|", r"\|")


def load_metadata():
    if not METADATA.is_file():
        raise FileNotFoundError("metadata.json is missing from the repository root.")

    data = json.loads(METADATA.read_text(encoding="utf-8"))
    problems = data.get("problems")
    if not isinstance(problems, list):
        raise ValueError("metadata.json must contain a 'problems' list.")

    by_id = {}
    for index, problem in enumerate(problems, start=1):
        if not isinstance(problem, dict):
            raise ValueError(f"metadata.json problem entry #{index} must be an object.")

        problem_id = str(problem.get("id", ""))
        if not re.fullmatch(r"\d{4,}", problem_id):
            raise ValueError(
                f"metadata.json problem entry #{index} has invalid id: {problem_id!r}."
            )
        if problem_id in by_id:
            raise ValueError(f"metadata.json contains duplicate id: {problem_id}.")

        difficulty = problem.get("difficulty")
        status = problem.get("status")
        topics = problem.get("topics")
        title = problem.get("title")

        if not isinstance(title, str) or not title.strip():
            raise ValueError(f"metadata.json entry {problem_id} must include a non-empty title.")
        if difficulty not in VALID_DIFFICULTIES:
            raise ValueError(
                f"metadata.json entry {problem_id} has invalid difficulty {difficulty!r}; "
                f"expected one of {sorted(VALID_DIFFICULTIES)}."
            )
        if status not in VALID_STATUSES:
            raise ValueError(
                f"metadata.json entry {problem_id} has invalid status {status!r}; "
                f"expected one of {sorted(VALID_STATUSES)}."
            )
        if not isinstance(topics, list) or not all(isinstance(topic, str) for topic in topics):
            raise ValueError(
                f"metadata.json entry {problem_id} must include a list of topic strings."
            )

        by_id[problem_id] = problem

    return by_id


def catalog_rows():
    metadata = load_metadata()
    rows = []
    seen_ids = set()

    for directory in problem_directories():
        problem_id = PROBLEM_DIR_RE.match(directory.name).group(1)
        seen_ids.add(problem_id)
        problem = metadata.get(problem_id)
        if problem is None:
            raise ValueError(f"metadata.json is missing an entry for {directory.name}.")

        rows.append(
            {
                "id": problem_id,
                "title": problem["title"],
                "difficulty": problem["difficulty"],
                "status": problem["status"],
                "paths": ", ".join(sorted(problem.get("path_membership") or [])),
                "ai_card": problem.get("ai_card_status") or "",
                "directory": f"problems/{directory.name}",
                "topics": "; ".join(problem["topics"]),
            }
        )

    extra_ids = sorted(set(metadata) - seen_ids)
    if extra_ids:
        joined_ids = ", ".join(extra_ids)
        raise ValueError(
            f"metadata.json contains entries without problem directories: {joined_ids}."
        )

    return rows


def render_catalog(rows):
    lines = [
        "# Problem Catalog",
        "",
        (
            "Generated from problem directories and `metadata.json` "
            "by `python scripts/generate_catalog.py`."
        ),
        "Directory naming follows `problem-id-kebab-case-title` (all lowercase).",
        "",
        f"**Total problems:** {len(rows)}",
        "",
        "| ID | Problem | Difficulty | Status | Paths | AI Card | Directory | Topics |",
        "|---:|---|---|---|---|---|---|---|",
    ]

    for row in rows:
        directory = row["directory"]
        lines.append(
            (
                "| {id} | {title} | {difficulty} | {status} | "
                "{paths} | {ai_card} | "
                "[`{directory}/`]({directory}/) | {topics} |"
            ).format(
                id=row["id"],
                title=escape_table_cell(row["title"]),
                difficulty=escape_table_cell(row["difficulty"]),
                status=escape_table_cell(row["status"]),
                paths=escape_table_cell(row["paths"]),
                ai_card=escape_table_cell(row["ai_card"]),
                directory=directory,
                topics=escape_table_cell(row["topics"]),
            )
        )

    return "\n".join(lines) + "\n"


def main():
    rows = catalog_rows()
    CATALOG.write_text(render_catalog(rows), encoding="utf-8")
    print(f"Generated CATALOG.md with {len(rows)} problem entries.")


if __name__ == "__main__":
    main()
