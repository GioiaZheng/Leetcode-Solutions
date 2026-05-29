import sys
from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPT_PATH = ROOT / "scripts" / "generate_catalog.py"


def load_generate_catalog():
    scripts_dir = str(ROOT / "scripts")
    added = scripts_dir not in sys.path
    if added:
        sys.path.insert(0, scripts_dir)
    try:
        spec = spec_from_file_location("generate_catalog", SCRIPT_PATH)
        module = module_from_spec(spec)
        spec.loader.exec_module(module)
        return module
    finally:
        if added:
            sys.path.remove(scripts_dir)


generate_catalog = load_generate_catalog()


# ---- escape_table_cell -------------------------------------------------


def test_escape_table_cell_escapes_pipes():
    assert generate_catalog.escape_table_cell("a|b") == r"a\|b"
    assert generate_catalog.escape_table_cell("|leading") == r"\|leading"
    assert generate_catalog.escape_table_cell("trailing|") == r"trailing\|"


def test_escape_table_cell_passes_through_safe_strings():
    assert generate_catalog.escape_table_cell("Two Sum") == "Two Sum"
    assert generate_catalog.escape_table_cell("") == ""


def test_escape_table_cell_coerces_non_strings():
    assert generate_catalog.escape_table_cell(42) == "42"
    assert generate_catalog.escape_table_cell(None) == "None"


# ---- render_catalog ----------------------------------------------------


def _sample_row(**overrides):
    base = {
        "id": "0001",
        "title": "Two Sum",
        "difficulty": "Easy",
        "status": "tested",
        "paths": "blind75, neetcode150",
        "study_card": "reviewed",
        "directory": "problems/0001-two-sum",
        "topics": "Array; Hash Table",
    }
    base.update(overrides)
    return base


def test_render_catalog_emits_eight_column_header_and_total():
    rows = [_sample_row()]

    body = generate_catalog.render_catalog(rows)

    assert "# Problem Catalog" in body
    assert "**Total problems:** 1" in body
    assert (
        "| ID | Problem | Difficulty | Status | Paths | Study Card | Directory | Topics |"
        in body
    )


def test_render_catalog_emits_clickable_study_card_link_when_reviewed():
    rows = [_sample_row(study_card="reviewed")]

    body = generate_catalog.render_catalog(rows)

    assert (
        "[reviewed](problems/0001-two-sum/README.md#brute-force-baseline)"
        in body
    )


def test_render_catalog_empty_study_card_cell_when_status_absent():
    rows = [_sample_row(study_card="")]

    body = generate_catalog.render_catalog(rows)

    # The Study Card cell is two pipes with nothing between when there is no
    # status to surface --- and crucially does NOT emit a link with an
    # empty anchor text.
    assert (
        "| 0001 | Two Sum | Easy | tested | blind75, neetcode150 |  |"
        in body
    )
    assert "[]" not in body  # no empty link text leaked


def test_render_catalog_escapes_pipe_in_title():
    rows = [_sample_row(title="A | B problem", paths="", study_card="")]

    body = generate_catalog.render_catalog(rows)

    assert r"A \| B problem" in body
