import sys
from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPT_PATH = ROOT / "scripts" / "generate_featured.py"


def load_generate_featured():
    # generate_featured imports category_for from generate_topics, which
    # in turn imports from generate_catalog --- the whole chain sits in
    # scripts/, so put it on sys.path before exec.
    scripts_dir = str(ROOT / "scripts")
    added = scripts_dir not in sys.path
    if added:
        sys.path.insert(0, scripts_dir)
    try:
        spec = spec_from_file_location("generate_featured", SCRIPT_PATH)
        module = module_from_spec(spec)
        spec.loader.exec_module(module)
        return module
    finally:
        if added:
            sys.path.remove(scripts_dir)


generate_featured = load_generate_featured()


# ---- primary_category --------------------------------------------------


def test_primary_category_picks_most_specific_over_array_catchall():
    # 0011-style metadata: Array, Two Pointers. The lazy first-topic
    # heuristic would lump this into "Arrays & Matrices"; the
    # specificity ranking lifts it to "Two Pointers & Sliding Window".
    problem = {"topics": ["Array", "Two Pointers"]}
    assert (
        generate_featured.primary_category(problem)
        == "Two Pointers & Sliding Window"
    )


def test_primary_category_prefers_dp_over_two_pointers():
    # 0042-style metadata: Array, Two Pointers, Dynamic Programming,
    # Stack. Per the PRIMARY_CATEGORY_SPECIFICITY ranking, Dynamic
    # Programming is more specific than the pointer/window catch-all.
    problem = {
        "topics": ["Array", "Two Pointers", "Dynamic Programming", "Stack"]
    }
    assert generate_featured.primary_category(problem) == "Dynamic Programming"


def test_primary_category_falls_through_to_other_techniques():
    # All topics map to "Other Techniques" (or the topic does not match
    # any alias), so the function returns the catch-all category.
    problem = {"topics": ["Divide and Conquer"]}
    assert generate_featured.primary_category(problem) == "Other Techniques"


def test_primary_category_handles_missing_topics_field():
    assert generate_featured.primary_category({}) == "Other Techniques"


# ---- featured_problems --------------------------------------------------


def test_featured_problems_filters_to_reviewed_and_sorts_by_id():
    problems = [
        {"id": "0050", "study_card_status": "draft"},
        {"id": "0042", "study_card_status": "reviewed"},
        {"id": "0001", "study_card_status": "reviewed"},
        {"id": "0099", "study_card_status": None},
        {"id": "0010", "study_card_status": "interview-ready"},  # not "reviewed"
        {"id": "0005", "study_card_status": "reviewed"},
    ]

    ids = [p["id"] for p in generate_featured.featured_problems(problems)]

    # Only "reviewed" makes the cut, in ascending numeric id order.
    assert ids == ["0001", "0005", "0042"]


def test_featured_problems_empty_when_no_reviewed_cards():
    problems = [
        {"id": "0001", "study_card_status": "draft"},
        {"id": "0002"},
    ]
    assert generate_featured.featured_problems(problems) == []


# ---- render_featured ----------------------------------------------------


def test_render_featured_emits_six_columns_with_paths_inline():
    problems = [
        {
            "id": "0001",
            "title": "Two Sum",
            "difficulty": "Easy",
            "topics": ["Array", "Hash Table"],
            "study_card_status": "reviewed",
            "path_membership": ["blind75", "neetcode150"],
        }
    ]
    directories = {"0001": "0001-two-sum"}

    body = generate_featured.render_featured(problems, directories)

    assert "| # | ID | Problem | Difficulty | Paths | Primary topic |" in body
    assert "| 1 | 0001 | [Two Sum](problems/0001-two-sum/) | Easy" in body
    assert "blind75, neetcode150" in body
    assert "Hashing" in body  # primary_category for {Array, Hash Table}


def test_render_featured_orphan_showcase_renders_empty_paths_cell():
    # 0085-style: reviewed study card but no path_membership. The Paths
    # column should be blank --- this is the visual signal for an
    # orphan showcase.
    problems = [
        {
            "id": "0085",
            "title": "Maximal Rectangle",
            "difficulty": "Hard",
            "topics": ["Dynamic Programming", "Stack"],
            "study_card_status": "reviewed",
        }
    ]
    directories = {"0085": "0085-maximal-rectangle"}

    body = generate_featured.render_featured(problems, directories)

    # Paths cell is empty (no comma-joined ids between the two
    # surrounding pipes); we anchor on the bracketing pipes via
    # the difficulty/topic columns on either side.
    assert "| Hard |  | Dynamic Programming |" in body


def test_render_featured_empty_state_emits_actionable_placeholder():
    body = generate_featured.render_featured([], {})

    assert "study_card_status: reviewed" in body
    assert "CONTRIBUTING.md" in body
