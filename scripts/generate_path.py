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

MILESTONES_SENTINEL_START = "<!-- MILESTONES_START -->"
MILESTONES_SENTINEL_END = "<!-- MILESTONES_END -->"

PROBLEM_DIR_RE = re.compile(r"^(\d{4,})-(.+)$")
SENTINEL_RE = re.compile(
    re.escape(LIST_SENTINEL_START) + r".*?" + re.escape(LIST_SENTINEL_END),
    re.DOTALL,
)
MILESTONES_SENTINEL_RE = re.compile(
    re.escape(MILESTONES_SENTINEL_START) + r".*?" + re.escape(MILESTONES_SENTINEL_END),
    re.DOTALL,
)

# Per-path milestone definitions. Each entry is (id, name, canonical count
# from the source list). The ids must match the keys of
# VALID_MILESTONE_IDS_PER_PATH in scripts/validate_repo.py.
#
# Blind 75 lumps Two Pointers + Sliding Window together (M2) and Heaps +
# Tries + Graphs together (M5). NeetCode 150 splits each of those into its
# own milestone --- M2 Two Pointers vs M3 Sliding Window, M8 Tries vs M9
# Heap / Priority Queue vs M11 Graphs.
PATH_MILESTONE_DEFS = {
    "blind75": [
        ("M1", "Arrays & Hashing", 10),
        ("M2", "Two Pointers & Sliding Window", 12),
        ("M3", "Stack, Queues & Binary Search", 10),
        ("M4", "Linked Lists & Trees", 15),
        ("M5", "Tries, Heaps & Graphs", 15),
        ("M6", "Dynamic Programming & Greedy", 13),
    ],
    "neetcode150": [
        ("M1", "Arrays & Hashing", 9),
        ("M2", "Two Pointers", 5),
        ("M3", "Sliding Window", 6),
        ("M4", "Stack", 7),
        ("M5", "Binary Search", 7),
        ("M6", "Linked List", 11),
        ("M7", "Trees", 15),
        ("M8", "Tries", 3),
        ("M9", "Heap / Priority Queue", 7),
        ("M10", "Backtracking", 9),
        ("M11", "Graphs", 13),
        ("M12", "Advanced Graphs", 6),
        ("M13", "1-D DP", 12),
        ("M14", "2-D DP", 11),
        ("M15", "Greedy", 8),
        ("M16", "Intervals", 6),
        ("M17", "Math & Geometry", 8),
        ("M18", "Bit Manipulation", 7),
    ],
}

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
        "| # | ID | Problem | Difficulty | Study Card | Directory |",
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
        study_card_raw = str(problem.get("study_card_status") or "")
        study_card_cell = (
            f"[{study_card_raw}](../../problems/{directory}/README.md#brute-force-baseline)"
            if study_card_raw
            else ""
        )
        lines.append(
            f"| {index} | {problem_id} | {title} | {difficulty} | "
            f"{study_card_cell} | "
            f"[`problems/{directory}/`](../../problems/{directory}/) |"
        )
    return "\n".join(lines)


def render_milestones(path_id, problems):
    """Emit the milestone summary table for `path_id`.

    Counts are derived from problem entries' `milestones[path_id]` field
    (validated by validate_repo.py to point at known milestone ids). A
    problem that omits `milestones` or uses a different `path_id` is
    simply not counted; this is intentional --- the metadata may have
    been added before the milestone classification was decided.
    """
    defs = PATH_MILESTONE_DEFS.get(path_id, [])
    if not defs:
        return ""

    tagged = {m_id: 0 for m_id, _, _ in defs}
    reviewed = {m_id: 0 for m_id, _, _ in defs}

    for problem in problems:
        memberships = problem.get("path_membership") or []
        if path_id not in memberships:
            continue
        milestones_field = problem.get("milestones") or {}
        m_id = milestones_field.get(path_id)
        if m_id is None or m_id not in tagged:
            continue
        tagged[m_id] += 1
        if problem.get("study_card_status") == "reviewed":
            reviewed[m_id] += 1

    lines = [
        "| # | Milestone | Canonical | In repo | Reviewed |",
        "|---|---|---:|---:|---:|",
    ]
    total_canonical = 0
    total_tagged = 0
    total_reviewed = 0
    for m_id, name, canonical in defs:
        lines.append(
            f"| {m_id} | {name} | {canonical} | {tagged[m_id]} | {reviewed[m_id]} |"
        )
        total_canonical += canonical
        total_tagged += tagged[m_id]
        total_reviewed += reviewed[m_id]
    lines.append(
        f"| **Total** | | **{total_canonical}** | "
        f"**{total_tagged}** | **{total_reviewed}** |"
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
    content = SENTINEL_RE.sub(replacement, content, count=1)

    # Milestones table is optional --- regenerate only if the sentinels exist.
    if MILESTONES_SENTINEL_RE.search(content):
        ms_body = render_milestones(path_id, problems)
        ms_replacement = (
            f"{MILESTONES_SENTINEL_START}\n{ms_body}\n{MILESTONES_SENTINEL_END}"
        )
        content = MILESTONES_SENTINEL_RE.sub(ms_replacement, content, count=1)

    readme.write_text(content, encoding="utf-8")
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
