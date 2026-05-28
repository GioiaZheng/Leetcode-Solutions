import sys
from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPT_PATH = ROOT / "scripts" / "generate_topics.py"


def load_generate_topics():
    scripts_dir = str(ROOT / "scripts")
    added = scripts_dir not in sys.path
    if added:
        sys.path.insert(0, scripts_dir)
    try:
        spec = spec_from_file_location("generate_topics", SCRIPT_PATH)
        module = module_from_spec(spec)
        spec.loader.exec_module(module)
        return module
    finally:
        if added:
            sys.path.remove(scripts_dir)


generate_topics = load_generate_topics()


# ---- category_for ------------------------------------------------------


def test_category_for_known_topic_returns_canonical_category():
    assert generate_topics.category_for("Array") == "Arrays & Matrices"
    assert generate_topics.category_for("Hash Map") == "Hashing"
    assert generate_topics.category_for("Two Pointers") == "Two Pointers & Sliding Window"
    assert generate_topics.category_for("Sliding Window") == "Two Pointers & Sliding Window"
    assert generate_topics.category_for("Dynamic Programming") == "Dynamic Programming"
    assert generate_topics.category_for("Heap") == "Sorting & Heap"


def test_category_for_unknown_topic_returns_other_techniques():
    assert generate_topics.category_for("Not A Real Topic") == "Other Techniques"
    assert generate_topics.category_for("") == "Other Techniques"


# ---- slug --------------------------------------------------------------


def test_slug_lowercases_and_hyphenates():
    assert generate_topics.slug("Arrays & Matrices") == "arrays-matrices"
    assert generate_topics.slug("Two Pointers & Sliding Window") == "two-pointers-sliding-window"


def test_slug_strips_punctuation_and_compresses_whitespace():
    assert generate_topics.slug("Math, Counting & Modulo!") == "math-counting-modulo"
    assert generate_topics.slug("  Trailing   Spaces  ") == "trailing-spaces"


# ---- topic_groups ------------------------------------------------------


def test_topic_groups_assigns_each_problem_to_every_canonical_category_it_touches():
    # 0001-style row: topics include both "Array" and "Hash Table",
    # so it should appear under BOTH "Arrays & Matrices" and "Hashing".
    rows = [
        {
            "id": "0001",
            "title": "Two Sum",
            "topics": "Array; Hash Table",
        }
    ]

    groups = generate_topics.topic_groups(rows)

    assert "Arrays & Matrices" in groups
    assert "Hashing" in groups
    assert any(r["id"] == "0001" for r in groups["Arrays & Matrices"])
    assert any(r["id"] == "0001" for r in groups["Hashing"])


def test_topic_groups_emits_untagged_for_rows_without_topics():
    rows = [{"id": "9999", "title": "Mystery", "topics": ""}]

    groups = generate_topics.topic_groups(rows)

    # An empty topics string falls through to "Untagged" via the
    # category_for("Untagged") path.
    assert "Untagged" in groups
    assert any(r["id"] == "9999" for r in groups["Untagged"])


def test_topic_groups_orders_rows_by_numeric_id_within_a_topic():
    rows = [
        {"id": "0050", "title": "Fifty", "topics": "Array"},
        {"id": "0001", "title": "One", "topics": "Array"},
        {"id": "0012", "title": "Twelve", "topics": "Array"},
    ]

    groups = generate_topics.topic_groups(rows)

    ids = [r["id"] for r in groups["Arrays & Matrices"]]
    assert ids == ["0001", "0012", "0050"]


# ---- render_topics -----------------------------------------------------


def test_render_topics_emits_anchor_list_and_per_topic_tables():
    rows = [
        {
            "id": "0001",
            "title": "Two Sum",
            "difficulty": "Easy",
            "status": "tested",
            "paths": "blind75, neetcode150",
            "ai_card": "reviewed",
            "directory": "problems/0001-two-sum",
            "topics": "Array; Hash Table",
        }
    ]
    groups = generate_topics.topic_groups(rows)

    body = generate_topics.render_topics(groups)

    # Top-level header and anchor list.
    assert "# Topic Index" in body
    assert "## Major Topics" in body
    assert "- [Arrays & Matrices](#arrays-matrices) (1)" in body
    assert "- [Hashing](#hashing) (1)" in body

    # Per-topic section header and 8-col table (matches the post-0bb2d49 schema:
    # ID / Problem / Difficulty / Status / Paths / AI Card / Directory / Original Topics).
    assert "## Arrays & Matrices" in body
    assert (
        "| ID | Problem | Difficulty | Status | Paths | AI Card | Directory | Original Topics |"
        in body
    )

    # AI Card cell is a link with the brute-force-baseline anchor.
    assert (
        "[reviewed](problems/0001-two-sum/README.md#brute-force-baseline)"
        in body
    )
    assert "blind75, neetcode150" in body
