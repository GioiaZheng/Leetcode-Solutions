from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
GENERATE_PATH_PATH = ROOT / "scripts" / "generate_path.py"


def load_generate_path():
    # generate_path imports from generate_topics at module load time
    # (for category_for), so the scripts/ directory must be on sys.path
    # before we exec.
    import sys

    scripts_dir = str(ROOT / "scripts")
    added = scripts_dir not in sys.path
    if added:
        sys.path.insert(0, scripts_dir)
    try:
        spec = spec_from_file_location("generate_path", GENERATE_PATH_PATH)
        module = module_from_spec(spec)
        spec.loader.exec_module(module)
        return module
    finally:
        if added:
            sys.path.remove(scripts_dir)


generate_path = load_generate_path()


# ---- render_milestones ----------------------------------------------------


def test_render_milestones_blind75_empty_state():
    body = generate_path.render_milestones("blind75", [])

    assert "M1 | Arrays & Hashing | 10 | 0 | 0" in body
    assert "M6 | Dynamic Programming & Greedy | 13 | 0 | 0" in body
    assert "**Total** | | **75** | **0** | **0**" in body


def test_render_milestones_counts_tagged_and_reviewed():
    problems = [
        {
            "id": "0001",
            "path_membership": ["blind75"],
            "milestones": {"blind75": "M1"},
            "study_card_status": "reviewed",
        },
        {
            "id": "0049",
            "path_membership": ["blind75"],
            "milestones": {"blind75": "M1"},
            "study_card_status": "draft",
        },
        {
            "id": "0242",
            "path_membership": ["blind75"],
            "milestones": {"blind75": "M1"},
            # no study_card_status --- counted as tagged but not reviewed
        },
    ]

    body = generate_path.render_milestones("blind75", problems)

    # 3 tagged into M1, only one ("reviewed") counts toward reviewed
    assert "M1 | Arrays & Hashing | 10 | 3 | 1" in body
    assert "**Total** | | **75** | **3** | **1**" in body


def test_render_milestones_skips_problems_outside_path():
    problems = [
        {
            "id": "0001",
            "path_membership": ["blind75"],
            "milestones": {"blind75": "M1"},
            "study_card_status": "reviewed",
        },
        {
            "id": "0010",
            "path_membership": ["neetcode150"],
            "milestones": {"neetcode150": "M14"},
            "study_card_status": "reviewed",
        },
    ]

    body = generate_path.render_milestones("blind75", problems)

    # Only 0001 should be counted; 0010 is neetcode150-only.
    assert "M1 | Arrays & Hashing | 10 | 1 | 1" in body
    assert "**Total** | | **75** | **1** | **1**" in body


def test_render_milestones_unknown_path_returns_empty():
    body = generate_path.render_milestones("not-a-path", [])
    assert body == ""


def test_render_milestones_skips_problems_without_milestone_field():
    # Tagged into path_membership but without milestones entry: counted in
    # the overall path total elsewhere, but render_milestones cannot place
    # them in a specific row, so they are silently skipped.
    problems = [
        {
            "id": "0001",
            "path_membership": ["blind75"],
            "study_card_status": "reviewed",
            # milestones field absent
        }
    ]

    body = generate_path.render_milestones("blind75", problems)

    assert "**Total** | | **75** | **0** | **0**" in body


# ---- render_problem_list --------------------------------------------------


def test_render_problem_list_empty_state_emits_placeholder():
    body = generate_path.render_problem_list([], "blind75", {})

    assert "No problems tagged yet" in body
    assert 'path_membership: ["blind75"]' in body


def test_render_problem_list_renders_six_columns_including_study_card_link():
    problems = [
        {
            "id": "0001",
            "title": "Two Sum",
            "difficulty": "Easy",
            "study_card_status": "reviewed",
        }
    ]
    directories = {"0001": "0001-two-sum"}

    body = generate_path.render_problem_list(problems, "blind75", directories)

    assert "| # | ID | Problem | Difficulty | Study Card | Directory |" in body
    assert "0001 | Two Sum | Easy" in body
    assert (
        "[reviewed](../../problems/0001-two-sum/README.md#brute-force-baseline)"
        in body
    )
    assert "[`problems/0001-two-sum/`](../../problems/0001-two-sum/)" in body


def test_render_problem_list_empty_study_card_cell_when_status_absent():
    problems = [
        {
            "id": "0004",
            "title": "Median Of Two Sorted Arrays",
            "difficulty": "Hard",
            # no study_card_status
        }
    ]
    directories = {"0004": "0004-median-of-two-sorted-arrays"}

    body = generate_path.render_problem_list(problems, "neetcode150", directories)

    # Study Card cell is bare (empty between pipes) when study_card_status is absent
    # --- no link, no text. The row still renders.
    assert "| 1 | 0004 | Median Of Two Sorted Arrays | Hard |  |" in body


def test_render_problem_list_raises_when_directory_missing():
    problems = [
        {
            "id": "9999",
            "title": "Phantom Problem",
            "difficulty": "Easy",
        }
    ]
    directories = {}  # 9999 not in filesystem

    try:
        generate_path.render_problem_list(problems, "blind75", directories)
    except ValueError as exc:
        assert "9999" in str(exc)
        assert "no matching directory exists" in str(exc)
    else:
        raise AssertionError("expected ValueError for missing directory")
