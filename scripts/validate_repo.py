import ast
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

PROBLEM_DIR_RE = re.compile(r"^(\d{4,})-.+")
STRICT_PROBLEM_DIR_RE = re.compile(r"^\d{4,}-[a-z0-9]+(?:-[a-z0-9]+)*$")
CATALOG_DIRECTORY_RE = re.compile(r"\[`([^`]+/?)`\]\(([^)]+)\)")
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


def problem_directories(root=ROOT):
    """Return LeetCode problem directories, excluding the reserved notes folder."""
    return sorted(
        path
        for path in root.iterdir()
        if path.is_dir()
        and (match := PROBLEM_DIR_RE.match(path.name))
        and int(match.group(1)) > 0
    )


def relative(path, root=ROOT):
    return path.relative_to(root)


def suspicious_files(root=ROOT):
    matches = []
    for path in root.rglob("*"):
        if ".git" in path.parts or not path.is_file():
            continue
        expected_name = SUSPICIOUS_FILENAMES.get(path.name)
        if expected_name:
            matches.append((path, expected_name))
    return sorted(matches)


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

    expected = {directory.name for directory in problem_dirs}
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


def validate(root=ROOT):
    errors = []
    directories = problem_directories(root)

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
    errors.extend(validate_metadata(directories, root))

    for path, expected_name in suspicious_files(root):
        errors.append(
            f"Suspicious filename {relative(path, root)} found; did you mean {expected_name}?"
        )

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
