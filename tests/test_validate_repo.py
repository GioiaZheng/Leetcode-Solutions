import json
from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
VALIDATE_REPO_PATH = ROOT / "scripts" / "validate_repo.py"


def load_validate_repo():
    spec = spec_from_file_location("validate_repo", VALIDATE_REPO_PATH)
    module = module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


validate_repo = load_validate_repo()


def standard_readme():
    return (
        "# Problem\n\n"
        "## Intuition\n\n"
        "## Approach\n\n"
        "## Complexity\n\n"
        "## Edge Cases\n\n"
        "## Code\n"
    )


def write_problem(root, name, readme=None, solution=None):
    directory = root / "problems" / name
    directory.mkdir(parents=True)
    if readme is not None:
        (directory / "README.md").write_text(readme, encoding="utf-8")
    if solution is not None:
        (directory / "solution.py").write_text(solution, encoding="utf-8")
    return directory


def write_catalog(root, directories):
    rows = [
        "# Problem Catalog",
        "",
        "| ID | Problem | Directory | Topics |",
        "|---:|---|---|---|",
    ]
    for directory in directories:
        problem_id = directory.split("-", 1)[0]
        rows.append(
            f"| {problem_id} | Example | [`problems/{directory}/`](problems/{directory}/) |  |"
        )
    (root / "CATALOG.md").write_text("\n".join(rows) + "\n", encoding="utf-8")


def write_topics(root, directories):
    rows = [
        "# Topic Index",
        "",
        "## Array",
        "",
        "| ID | Problem | Directory |",
        "|---:|---|---|",
    ]
    for directory in directories:
        problem_id = directory.split("-", 1)[0]
        rows.append(f"| {problem_id} | Example | [`problems/{directory}/`](problems/{directory}/) |")
    (root / "TOPICS.md").write_text("\n".join(rows) + "\n", encoding="utf-8")


def write_metadata(root, directories):
    problems = []
    for directory in directories:
        problem_id = directory.split("-", 1)[0]
        problems.append(
            {
                "id": problem_id,
                "title": "Example",
                "difficulty": "Easy",
                "topics": ["Array"],
                "status": "solved",
            }
        )
    (root / "metadata.json").write_text(
        json.dumps({"problems": problems}, indent=2) + "\n",
        encoding="utf-8",
    )


def test_validate_accepts_well_formed_repository(tmp_path):
    directory = "0001-two-sum"
    write_problem(
        tmp_path,
        directory,
        readme=standard_readme(),
        solution="class Solution:\n    pass\n",
    )
    write_catalog(tmp_path, [directory])
    write_topics(tmp_path, [directory])
    write_metadata(tmp_path, [directory])

    directories, errors = validate_repo.validate(tmp_path)

    assert [path.name for path in directories] == [directory]
    assert errors == []


def test_validate_reports_missing_required_files(tmp_path):
    directory = "0001-two-sum"
    (tmp_path / "problems" / directory).mkdir(parents=True)
    write_catalog(tmp_path, [directory])
    write_topics(tmp_path, [directory])
    write_metadata(tmp_path, [directory])

    _, errors = validate_repo.validate(tmp_path)

    assert f"problems/{directory} is missing README.md." in errors
    assert f"problems/{directory} is missing solution.py." in errors


def test_validate_reports_problem_directories_at_repository_root(tmp_path):
    directory = "0001-two-sum"
    misplaced = "0002-add-two-numbers"
    write_problem(
        tmp_path,
        directory,
        readme=standard_readme(),
        solution="class Solution:\n    pass\n",
    )
    (tmp_path / misplaced).mkdir()
    write_catalog(tmp_path, [directory])
    write_topics(tmp_path, [directory])
    write_metadata(tmp_path, [directory])

    _, errors = validate_repo.validate(tmp_path)

    assert f"{misplaced} should be moved under problems/{misplaced}." in errors


def test_validate_reports_solution_parse_and_class_errors(tmp_path):
    bad_syntax = "0001-two-sum"
    missing_class = "0002-add-two-numbers"
    readme = standard_readme()
    write_problem(tmp_path, bad_syntax, readme=readme, solution="class Solution(:\n")
    write_problem(tmp_path, missing_class, readme=readme, solution="class NotSolution:\n    pass\n")
    write_catalog(tmp_path, [bad_syntax, missing_class])
    write_topics(tmp_path, [bad_syntax, missing_class])
    write_metadata(tmp_path, [bad_syntax, missing_class])

    _, errors = validate_repo.validate(tmp_path)

    assert any(
        f"problems/{bad_syntax}/solution.py has invalid Python syntax" in error
        for error in errors
    )
    assert f"problems/{missing_class}/solution.py must define class Solution." in errors


def test_validate_reports_readme_directory_and_catalog_errors(tmp_path):
    bad_name = "0001-Two_Sum"
    missing_from_catalog = "0002-add-two-numbers"
    extra = "9999-extra-problem"
    readme = "# Problem\n\n## Complexity\n"
    write_problem(tmp_path, bad_name, readme=readme, solution="class Solution:\n    pass\n")
    write_problem(
        tmp_path,
        missing_from_catalog,
        readme=(
            "# Problem\n\n"
            "## Intuition\n\n"
            "## Algorithm\n\n"
            "## Complexity\n\n"
            "## Edge Cases\n\n"
            "## Code\n"
        ),
        solution="class Solution:\n    pass\n",
    )
    write_catalog(tmp_path, [bad_name, bad_name, extra])
    write_topics(tmp_path, [bad_name, missing_from_catalog])
    write_metadata(tmp_path, [bad_name, missing_from_catalog])

    _, errors = validate_repo.validate(tmp_path)

    assert any("problems/0001-Two_Sum must use ####-lowercase-kebab-case" in error for error in errors)
    assert any("problems/0001-Two_Sum/README.md must describe Approach" in error for error in errors)
    assert f"CATALOG.md is missing an entry for problems/{missing_from_catalog}." in errors
    assert f"CATALOG.md contains duplicate entries for problems/{bad_name}." in errors
    assert f"CATALOG.md contains an entry for unknown directory problems/{extra}." in errors


def test_validate_reports_topics_errors(tmp_path):
    directory = "0001-two-sum"
    extra = "9999-extra-problem"
    write_problem(
        tmp_path,
        directory,
        readme=standard_readme(),
        solution="class Solution:\n    pass\n",
    )
    write_catalog(tmp_path, [directory])
    write_topics(tmp_path, [extra])
    write_metadata(tmp_path, [directory])

    _, errors = validate_repo.validate(tmp_path)

    assert f"TOPICS.md is missing an entry for problems/{directory}." in errors
    assert f"TOPICS.md contains an entry for unknown directory problems/{extra}." in errors


def test_validate_reports_metadata_errors(tmp_path):
    directory = "0001-two-sum"
    extra_id = "9999"
    write_problem(
        tmp_path,
        directory,
        readme=standard_readme(),
        solution="class Solution:\n    pass\n",
    )
    write_catalog(tmp_path, [directory])
    write_topics(tmp_path, [directory])
    (tmp_path / "metadata.json").write_text(
        json.dumps(
            {
                "problems": [
                    {
                        "id": extra_id,
                        "title": "Extra",
                        "difficulty": "Extreme",
                        "topics": "Array",
                        "status": "done",
                    }
                ]
            }
        ),
        encoding="utf-8",
    )

    _, errors = validate_repo.validate(tmp_path)

    assert f"metadata.json is missing an entry for {directory}." in errors
    assert (
        f"metadata.json contains entry {extra_id} without a matching problem directory."
        in errors
    )
    assert any("invalid difficulty 'Extreme'" in error for error in errors)
    assert f"metadata.json entry {extra_id} must include a list of topic strings." in errors
    assert any("invalid status 'done'" in error for error in errors)


def test_validate_reports_suspicious_filenames(tmp_path):
    directory = "0001-two-sum"
    problem = write_problem(
        tmp_path,
        directory,
        readme=standard_readme(),
        solution="class Solution:\n    pass\n",
    )
    (problem / "soution.py").write_text("class Solution:\n    pass\n", encoding="utf-8")
    write_catalog(tmp_path, [directory])
    write_topics(tmp_path, [directory])
    write_metadata(tmp_path, [directory])

    _, errors = validate_repo.validate(tmp_path)

    assert (
        f"Suspicious filename problems/{directory}/soution.py found; did you mean solution.py?"
        in errors
    )


def test_validate_reports_nested_notes_directories(tmp_path):
    directory = "0001-two-sum"
    write_problem(
        tmp_path,
        directory,
        readme=standard_readme(),
        solution="class Solution:\n    pass\n",
    )
    (tmp_path / "0000-notes" / "09-graph" / "0000-notes").mkdir(parents=True)
    write_catalog(tmp_path, [directory])
    write_topics(tmp_path, [directory])
    write_metadata(tmp_path, [directory])

    _, errors = validate_repo.validate(tmp_path)

    assert "Nested notes directory 0000-notes/09-graph/0000-notes should be removed." in errors


def test_validate_reports_mojibake_in_entrypoint_docs(tmp_path):
    directory = "0001-two-sum"
    write_problem(
        tmp_path,
        directory,
        readme=standard_readme(),
        solution="class Solution:\n    pass\n",
    )
    write_catalog(tmp_path, [directory])
    write_topics(tmp_path, [directory])
    write_metadata(tmp_path, [directory])
    (tmp_path / "README.md").write_text("Broken ä¸­æ–‡ marker\n", encoding="utf-8")

    _, errors = validate_repo.validate(tmp_path)

    assert "README.md:1 contains mojibake; check the file encoding." in errors


def test_validate_reports_broken_entrypoint_links(tmp_path):
    directory = "0001-two-sum"
    write_problem(
        tmp_path,
        directory,
        readme=standard_readme(),
        solution="class Solution:\n    pass\n",
    )
    write_catalog(tmp_path, [directory])
    write_topics(tmp_path, [directory])
    write_metadata(tmp_path, [directory])
    (tmp_path / "README.md").write_text(
        "[missing](docs/missing.md)\n[outside](../outside.md)\n",
        encoding="utf-8",
    )

    _, errors = validate_repo.validate(tmp_path)

    assert "README.md:1 has a broken link: docs/missing.md." in errors
    assert "README.md:2 links outside the repository: ../outside.md." in errors
