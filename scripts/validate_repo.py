from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parent.parent
CATALOG = ROOT / "CATALOG.md"

PROBLEM_DIR_RE = re.compile(r"^(\d{4,})-.+")
SUSPICIOUS_FILENAMES = {
    "soution.py": "solution.py",
}


def problem_directories():
    """Return LeetCode problem directories, excluding the reserved notes folder."""
    return sorted(
        path
        for path in ROOT.iterdir()
        if path.is_dir()
        and (match := PROBLEM_DIR_RE.match(path.name))
        and int(match.group(1)) > 0
    )


def relative(path):
    return path.relative_to(ROOT)


def suspicious_files():
    matches = []
    for path in ROOT.rglob("*"):
        if ".git" in path.parts or not path.is_file():
            continue
        expected_name = SUSPICIOUS_FILENAMES.get(path.name)
        if expected_name:
            matches.append((path, expected_name))
    return sorted(matches)


def validate():
    errors = []
    directories = problem_directories()

    if not CATALOG.is_file():
        errors.append("CATALOG.md is missing from the repository root.")

    for directory in directories:
        if not (directory / "README.md").is_file():
            errors.append(f"{relative(directory)} is missing README.md.")
        if not (directory / "solution.py").is_file():
            errors.append(f"{relative(directory)} is missing solution.py.")

    for path, expected_name in suspicious_files():
        errors.append(
            f"Suspicious filename {relative(path)} found; did you mean {expected_name}?"
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
