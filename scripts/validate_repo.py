import ast
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

PROBLEM_DIR_RE = re.compile(r"^(\d{4,})-.+")
STRICT_PROBLEM_DIR_RE = re.compile(r"^\d{4,}-[a-z0-9]+(?:-[a-z0-9]+)*$")
CATALOG_DIRECTORY_RE = re.compile(r"\[`([^`]+/?)`\]\(([^)]+)\)")
MARKDOWN_LINK_RE = re.compile(r"(?<!!)\[[^\]]+\]\(([^)]+)\)")
README_REQUIREMENTS = {
    "Problem": ("problem",),
    "Intuition": (
        "intuition",
        "key insight",
        "core insight",
        "key observation",
        "core idea",
        "correctness intuition",
        "important observation",
    ),
    "Approach": ("approach", "algorithm", "strategy", "key insight", "core idea"),
    "Complexity": ("complexity",),
    # Legacy READMEs may discuss edge cases as examples, pitfalls, or correctness notes.
    "Edge Cases": (
        "edge case",
        "edge cases",
        "common mistakes",
        "common pitfalls",
        "pitfalls",
        "example",
        "correctness",
        "comparison",
        "important observation",
    ),
    "Code": ("code", "solution", "implementation"),
}
SUSPICIOUS_FILENAMES = {
    "soution.py": "solution.py",
}
VALID_DIFFICULTIES = {"Easy", "Medium", "Hard"}
VALID_STATUSES = {"solved", "tested", "review-needed"}
VALID_PATH_MEMBERSHIPS = {"blind75", "neetcode150"}
VALID_STUDY_CARD_STATUSES = {"draft", "reviewed", "interview-ready"}

# Per-path valid milestone identifiers. Used to validate the optional
# `milestones` field on each problem entry. The number of milestones is the
# canonical count from each path's source list (Blind 75 = 6 pattern groups,
# NeetCode 150 = 18). Definitions of WHAT each milestone covers live in
# scripts/generate_path.py (PATH_MILESTONE_DEFS) so the generator can emit a
# table; the validator only checks that the ids are well-formed.
VALID_MILESTONE_IDS_PER_PATH = {
    "blind75": frozenset(f"M{i}" for i in range(1, 7)),
    "neetcode150": frozenset(f"M{i}" for i in range(1, 19)),
}

# Reliable signal that a problem README has been migrated to the Study Card
# template (templates/problem_README.md). "Brute-force baseline" is unique
# to the optional Study Card extension --- it never appears as an alias for
# any of the six required core sections in README_REQUIREMENTS, so its
# presence implies the author opted into the Study Card workflow.
STUDY_CARD_MARKER_HEADING = "## Brute-force baseline"
MOJIBAKE_MARKERS = ("ï", "Â", "Ã", "â€", "â†", "ä¸", "æ–")
MOJIBAKE_CHECKED_FILES = (
    "README.md",
    "CATALOG.md",
    "TOPICS.md",
    "0000-notes/README.md",
    "problems/README.md",
)


def problem_directories(root=ROOT):
    """Return LeetCode problem directories, excluding the reserved notes folder."""
    problems_root = root / "problems"
    if not problems_root.is_dir():
        return []

    return sorted(
        path
        for path in problems_root.iterdir()
        if path.is_dir()
        and (match := PROBLEM_DIR_RE.match(path.name))
        and int(match.group(1)) > 0
    )


def root_problem_directories(root=ROOT):
    """Return problem-like directories that should live under problems/."""
    return sorted(
        path
        for path in root.iterdir()
        if path.is_dir()
        and path.name != "0000-notes"
        and (match := PROBLEM_DIR_RE.match(path.name))
        and int(match.group(1)) > 0
    )


def relative(path, root=ROOT):
    return path.relative_to(root).as_posix()


def suspicious_files(root=ROOT):
    matches = []
    for path in root.rglob("*"):
        if ".git" in path.parts or not path.is_file():
            continue
        expected_name = SUSPICIOUS_FILENAMES.get(path.name)
        if expected_name:
            matches.append((path, expected_name))
    return sorted(matches)


def nested_notes_directories(root=ROOT):
    notes_root = root / "0000-notes"
    if not notes_root.is_dir():
        return []

    return sorted(path for path in notes_root.rglob("0000-notes") if path.is_dir())


def validate_entrypoint_encoding(root=ROOT):
    errors = []

    for relative_path in MOJIBAKE_CHECKED_FILES:
        path = root / relative_path
        if not path.is_file():
            continue

        for line_number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), start=1):
            if any(marker in line for marker in MOJIBAKE_MARKERS):
                errors.append(
                    f"{relative_path}:{line_number} contains mojibake; "
                    "check the file encoding."
                )

    return errors


def validate_entrypoint_links(root=ROOT):
    errors = []

    for relative_path in MOJIBAKE_CHECKED_FILES:
        path = root / relative_path
        if not path.is_file():
            continue

        for line_number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), start=1):
            for match in MARKDOWN_LINK_RE.finditer(line):
                target = match.group(1).strip()
                if (
                    not target
                    or target.startswith("#")
                    or re.match(r"^[a-z][a-z0-9+.-]*:", target)
                ):
                    continue

                target_path = target.split("#", 1)[0]
                if not target_path:
                    continue

                resolved = (path.parent / target_path).resolve()
                try:
                    resolved.relative_to(root.resolve())
                except ValueError:
                    errors.append(
                        f"{relative_path}:{line_number} links outside the repository: {target}."
                    )
                    continue

                if not resolved.exists():
                    errors.append(f"{relative_path}:{line_number} has a broken link: {target}.")

    return errors


def readme_has_requirement(content, keywords):
    content = content.lower()
    return any(keyword in content for keyword in keywords)


def validate_readme(readme, root=ROOT):
    errors = []
    content = readme.read_text(encoding="utf-8")

    for label, keywords in README_REQUIREMENTS.items():
        if not readme_has_requirement(content, keywords):
            expected = "'" + "', '".join(keywords) + "'"
            errors.append(
                f"{relative(readme, root)} must describe {label} "
                f"(include one of: {expected})."
            )

    return errors


def validate_solution(solution, root=ROOT):
    errors = []

    try:
        tree = ast.parse(solution.read_text(encoding="utf-8"), filename=str(solution))
    except SyntaxError as exc:
        errors.append(
            f"{relative(solution, root)} has invalid Python syntax: "
            f"line {exc.lineno}, column {exc.offset}: {exc.msg}."
        )
        return errors

    has_solution_class = any(
        isinstance(node, ast.ClassDef) and node.name == "Solution"
        for node in ast.walk(tree)
    )
    if not has_solution_class:
        errors.append(f"{relative(solution, root)} must define class Solution.")

    return errors


def load_metadata(root=ROOT):
    metadata = root / "metadata.json"
    if not metadata.is_file():
        return None, ["metadata.json is missing from the repository root."]

    try:
        data = json.loads(metadata.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        return None, [
            f"metadata.json is invalid JSON: "
            f"line {exc.lineno}, column {exc.colno}: {exc.msg}."
        ]

    problems = data.get("problems")
    if not isinstance(problems, list):
        return None, ["metadata.json must contain a 'problems' list."]

    by_id = {}
    errors = []
    for index, problem in enumerate(problems, start=1):
        if not isinstance(problem, dict):
            errors.append(f"metadata.json problem entry #{index} must be an object.")
            continue

        problem_id = str(problem.get("id", ""))
        if not re.fullmatch(r"\d{4,}", problem_id):
            errors.append(f"metadata.json problem entry #{index} has invalid id: {problem_id!r}.")
            continue
        if problem_id in by_id:
            errors.append(f"metadata.json contains duplicate id: {problem_id}.")
            continue

        title = problem.get("title")
        difficulty = problem.get("difficulty")
        topics = problem.get("topics")
        status = problem.get("status")

        if not isinstance(title, str) or not title.strip():
            errors.append(f"metadata.json entry {problem_id} must include a non-empty title.")
        if difficulty not in VALID_DIFFICULTIES:
            errors.append(
                f"metadata.json entry {problem_id} has invalid difficulty {difficulty!r}; "
                f"expected one of {sorted(VALID_DIFFICULTIES)}."
            )
        if not isinstance(topics, list) or not all(isinstance(topic, str) for topic in topics):
            errors.append(f"metadata.json entry {problem_id} must include a list of topic strings.")
        if status not in VALID_STATUSES:
            errors.append(
                f"metadata.json entry {problem_id} has invalid status {status!r}; "
                f"expected one of {sorted(VALID_STATUSES)}."
            )

        path_membership = problem.get("path_membership")
        if path_membership is not None:
            if not isinstance(path_membership, list) or not all(
                isinstance(p, str) for p in path_membership
            ):
                errors.append(
                    f"metadata.json entry {problem_id} has invalid path_membership; "
                    f"expected a list of strings or omitted."
                )
            else:
                unknown = sorted(set(path_membership) - VALID_PATH_MEMBERSHIPS)
                if unknown:
                    errors.append(
                        f"metadata.json entry {problem_id} has unknown path_membership "
                        f"values {unknown}; expected subset of "
                        f"{sorted(VALID_PATH_MEMBERSHIPS)}."
                    )

        study_card_status = problem.get("study_card_status")
        if study_card_status is not None and study_card_status not in VALID_STUDY_CARD_STATUSES:
            errors.append(
                f"metadata.json entry {problem_id} has invalid study_card_status "
                f"{study_card_status!r}; expected one of "
                f"{sorted(VALID_STUDY_CARD_STATUSES)}."
            )

        milestones = problem.get("milestones")
        if milestones is not None:
            if not isinstance(milestones, dict):
                errors.append(
                    f"metadata.json entry {problem_id} has invalid milestones; "
                    f"expected a dict mapping path id to milestone id, or omitted."
                )
            else:
                membership = set(problem.get("path_membership") or [])
                for path_id, milestone_id in milestones.items():
                    if not isinstance(path_id, str) or not isinstance(milestone_id, str):
                        errors.append(
                            f"metadata.json entry {problem_id} milestones has a "
                            f"non-string key or value."
                        )
                        continue
                    if path_id not in membership:
                        errors.append(
                            f"metadata.json entry {problem_id} milestones references "
                            f"path {path_id!r} but that path is not in path_membership "
                            f"{sorted(membership)}."
                        )
                        continue
                    valid_ids = VALID_MILESTONE_IDS_PER_PATH.get(path_id)
                    if valid_ids is None:
                        errors.append(
                            f"metadata.json entry {problem_id} milestones references "
                            f"unknown path {path_id!r}; expected subset of "
                            f"{sorted(VALID_MILESTONE_IDS_PER_PATH)}."
                        )
                        continue
                    if milestone_id not in valid_ids:
                        errors.append(
                            f"metadata.json entry {problem_id} milestones[{path_id!r}] "
                            f"has invalid id {milestone_id!r}; expected one of "
                            f"{sorted(valid_ids)}."
                        )

        by_id[problem_id] = problem

    return by_id, errors


def validate_metadata(problem_dirs, root=ROOT):
    metadata_by_id, errors = load_metadata(root)
    if metadata_by_id is None:
        return errors

    expected_ids = {PROBLEM_DIR_RE.match(directory.name).group(1) for directory in problem_dirs}
    metadata_ids = set(metadata_by_id)

    for directory in problem_dirs:
        problem_id = PROBLEM_DIR_RE.match(directory.name).group(1)
        if problem_id not in metadata_by_id:
            errors.append(f"metadata.json is missing an entry for {directory.name}.")

    for problem_id in sorted(metadata_ids - expected_ids):
        errors.append(
            f"metadata.json contains entry {problem_id} "
            "without a matching problem directory."
        )

    return errors


def catalog_directories(catalog):
    entries = []
    for line in catalog.read_text(encoding="utf-8").splitlines():
        if not line.startswith("|"):
            continue
        match = CATALOG_DIRECTORY_RE.search(line)
        if match:
            display_directory, link_directory = match.groups()
            directory = link_directory.rstrip("/") or display_directory.rstrip("/")
            entries.append(directory)
    return entries


def validate_catalog(problem_dirs, root=ROOT):
    errors = []
    catalog = root / "CATALOG.md"

    if not catalog.is_file():
        return ["CATALOG.md is missing from the repository root."]

    expected = {relative(directory, root) for directory in problem_dirs}
    entries = catalog_directories(catalog)
    seen = set()
    duplicates = set()

    for directory in entries:
        if directory in seen:
            duplicates.add(directory)
        seen.add(directory)

    missing = sorted(expected - seen)
    extra = sorted(seen - expected)

    for directory in missing:
        errors.append(f"CATALOG.md is missing an entry for {directory}.")
    for directory in sorted(duplicates):
        errors.append(f"CATALOG.md contains duplicate entries for {directory}.")
    for directory in extra:
        errors.append(f"CATALOG.md contains an entry for unknown directory {directory}.")

    return errors


def readme_has_study_card_sections(content):
    return STUDY_CARD_MARKER_HEADING in content


def validate_study_card_consistency(problem_dirs, root=ROOT):
    """Per-problem README + metadata.json must agree about Study Card status.

    A problem README that ships Study Card sections (detected via the
    `## Brute-force baseline` heading) must carry an study_card_status entry
    in metadata.json, and vice versa: a metadata entry that sets
    study_card_status must point at a README that actually has the sections.
    """
    metadata_by_id, _ = load_metadata(root)
    if metadata_by_id is None:
        # load_metadata's own errors surface in validate_metadata; do not
        # double-report them here.
        return []

    errors = []
    for directory in problem_dirs:
        problem_id = PROBLEM_DIR_RE.match(directory.name).group(1)
        readme = directory / "README.md"
        if not readme.is_file():
            continue

        content = readme.read_text(encoding="utf-8")
        has_card = readme_has_study_card_sections(content)
        study_card_status = metadata_by_id.get(problem_id, {}).get("study_card_status")

        if has_card and study_card_status is None:
            errors.append(
                f"{relative(readme, root)} contains Study Card sections "
                f"but metadata.json has no study_card_status for entry "
                f"{problem_id} (set it to one of "
                f"{sorted(VALID_STUDY_CARD_STATUSES)})."
            )
        elif study_card_status is not None and not has_card:
            errors.append(
                f"metadata.json entry {problem_id} sets "
                f"study_card_status={study_card_status!r} but "
                f"{relative(readme, root)} contains no Study Card sections "
                f"(the template marker heading "
                f"{STUDY_CARD_MARKER_HEADING!r} is missing)."
            )

    return errors


def validate_topics(problem_dirs, root=ROOT):
    errors = []
    topics = root / "TOPICS.md"

    if not topics.is_file():
        return ["TOPICS.md is missing from the repository root."]

    expected = {relative(directory, root) for directory in problem_dirs}
    entries = set(catalog_directories(topics))
    missing = sorted(expected - entries)
    extra = sorted(entries - expected)

    for directory in missing:
        errors.append(f"TOPICS.md is missing an entry for {directory}.")
    for directory in extra:
        errors.append(f"TOPICS.md contains an entry for unknown directory {directory}.")

    return errors


def validate(root=ROOT):
    errors = []
    directories = problem_directories(root)

    for directory in root_problem_directories(root):
        errors.append(
            f"{relative(directory, root)} should be moved under problems/{directory.name}."
        )

    for directory in directories:
        if not STRICT_PROBLEM_DIR_RE.match(directory.name):
            errors.append(
                f"{relative(directory, root)} must use ####-lowercase-kebab-case "
                "with only lowercase letters, digits, and hyphens."
            )

        readme = directory / "README.md"
        solution = directory / "solution.py"

        if not readme.is_file():
            errors.append(f"{relative(directory, root)} is missing README.md.")
        else:
            errors.extend(validate_readme(readme, root))

        if not solution.is_file():
            errors.append(f"{relative(directory, root)} is missing solution.py.")
        else:
            errors.extend(validate_solution(solution, root))

    errors.extend(validate_catalog(directories, root))
    errors.extend(validate_topics(directories, root))
    errors.extend(validate_metadata(directories, root))
    errors.extend(validate_study_card_consistency(directories, root))
    errors.extend(validate_entrypoint_encoding(root))
    errors.extend(validate_entrypoint_links(root))

    for path, expected_name in suspicious_files(root):
        errors.append(
            f"Suspicious filename {relative(path, root)} found; did you mean {expected_name}?"
        )

    for path in nested_notes_directories(root):
        errors.append(f"Nested notes directory {relative(path, root)} should be removed.")

    return directories, errors


def main():
    directories, errors = validate()

    print(f"Checked {len(directories)} problem directories.")

    if errors:
        print("Repository validation failed:")
        for error in errors:
            print(f"- ERROR: {error}")
        return 1

    print("Repository validation passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
