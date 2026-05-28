import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PATHS_DIR = ROOT / "paths"
PROBLEMS_DIR = ROOT / "problems"
METADATA = ROOT / "metadata.json"

VALID_PATH_MEMBERSHIPS = ("blind75", "neetcode150")

LIST_SENTINEL_START = "<!-- PATH_LIST_START -->"
LIST_SENTINEL_END = "<!-- PATH_LIST_END -->"

PROBLEM_DIR_RE = re.compile(r"^(\d{4,})-(.+)$")
SENTINEL_RE = re.compile(
    re.escape(LIST_SENTINEL_START) + r".*?" + re.escape(LIST_SENTINEL_END),
    re.DOTALL,
)

EMPTY_LIST_BODY = (
    '_No problems tagged yet. Add `path_membership: ["{path_id}"]` entries '
    "in `metadata.json` to populate this list._"
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


def collect_members(problems, path_id):
    members = []
    for problem in problems:
        memberships = problem.get("path_membership") or []
        if path_id in memberships:
            members.append(problem)
    members.sort(key=lambda p: p.get("id", ""))
    return members


def render_problem_list(members, path_id, directories):
    if not members:
        return EMPTY_LIST_BODY.format(path_id=path_id)

    lines = [
        "| # | ID | Problem | Difficulty | AI Card | Directory |",
        "|---:|---:|---|---|---|---|",
    ]
    for index, problem in enumerate(members, start=1):
        problem_id = problem["id"]
        directory = directories.get(problem_id)
        if directory is None:
            raise ValueError(
                f"metadata.json claims problem {problem_id} is in path {path_id} "
                "but no matching directory exists under problems/."
            )
        title = str(problem.get("title", "")).replace("|", r"\|")
        difficulty = str(problem.get("difficulty", "")).replace("|", r"\|")
        ai_card_raw = str(problem.get("ai_card_status") or "")
        ai_card_cell = (
            f"[{ai_card_raw}](../../problems/{directory}/README.md#brute-force-baseline)"
            if ai_card_raw
            else ""
        )
        lines.append(
            f"| {index} | {problem_id} | {title} | {difficulty} | "
            f"{ai_card_cell} | "
            f"[`problems/{directory}/`](../../problems/{directory}/) |"
        )
    return "\n".join(lines)


def regenerate_path(path_id, problems, directories):
    readme = PATHS_DIR / path_id / "README.md"
    if not readme.is_file():
        raise FileNotFoundError(
            f"{readme.relative_to(ROOT)} does not exist; cannot regenerate."
        )

    content = readme.read_text(encoding="utf-8")
    if not SENTINEL_RE.search(content):
        raise ValueError(
            f"{readme.relative_to(ROOT)} is missing the "
            f"{LIST_SENTINEL_START} ... {LIST_SENTINEL_END} sentinels."
        )

    members = collect_members(problems, path_id)
    body = render_problem_list(members, path_id, directories)
    replacement = f"{LIST_SENTINEL_START}\n{body}\n{LIST_SENTINEL_END}"
    new_content = SENTINEL_RE.sub(replacement, content, count=1)
    readme.write_text(new_content, encoding="utf-8")
    return len(members)


def main():
    if not PATHS_DIR.is_dir():
        print("paths/ does not exist; nothing to regenerate.")
        return

    problems = load_problems()
    directories = problem_directories()

    regenerated = 0
    for path_id in VALID_PATH_MEMBERSHIPS:
        path_dir = PATHS_DIR / path_id
        if not path_dir.is_dir():
            continue
        count = regenerate_path(path_id, problems, directories)
        print(f"Regenerated paths/{path_id}/README.md with {count} problems.")
        regenerated += 1

    if regenerated == 0:
        print("No path directories found under paths/; nothing to regenerate.")


if __name__ == "__main__":
    main()
