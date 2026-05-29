import json
import sys
from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
SCRIPT_PATH = ROOT / "scripts" / "update_stats.py"


def load_update_stats():
    scripts_dir = str(ROOT / "scripts")
    added = scripts_dir not in sys.path
    if added:
        sys.path.insert(0, scripts_dir)
    try:
        spec = spec_from_file_location("update_stats", SCRIPT_PATH)
        module = module_from_spec(spec)
        spec.loader.exec_module(module)
        return module
    finally:
        if added:
            sys.path.remove(scripts_dir)


update_stats = load_update_stats()


def _write_metadata(path, problems):
    path.write_text(
        json.dumps({"problems": problems}, indent=2) + "\n",
        encoding="utf-8",
    )


@pytest.fixture
def isolated_metadata(tmp_path, monkeypatch):
    """Point update_stats at a tmp metadata.json so each test is hermetic."""
    metadata = tmp_path / "metadata.json"
    monkeypatch.setattr(update_stats, "METADATA", metadata)
    return metadata


# ---- difficulty_counts -------------------------------------------------


def test_difficulty_counts_buckets_easy_medium_hard(isolated_metadata):
    _write_metadata(
        isolated_metadata,
        [
            {"id": "0001", "difficulty": "Easy"},
            {"id": "0002", "difficulty": "Medium"},
            {"id": "0003", "difficulty": "Hard"},
            {"id": "0004", "difficulty": "Medium"},
        ],
    )

    counts = update_stats.difficulty_counts()

    assert counts == {"Easy": 1, "Medium": 2, "Hard": 1}


def test_difficulty_counts_ignores_unknown_difficulty(isolated_metadata):
    _write_metadata(
        isolated_metadata,
        [
            {"id": "0001", "difficulty": "Easy"},
            {"id": "0002", "difficulty": "Extreme"},  # not in the bucket dict
        ],
    )

    counts = update_stats.difficulty_counts()

    assert counts == {"Easy": 1, "Medium": 0, "Hard": 0}


def test_difficulty_counts_returns_zeros_when_metadata_missing(
    tmp_path, monkeypatch
):
    monkeypatch.setattr(update_stats, "METADATA", tmp_path / "nope.json")
    assert update_stats.difficulty_counts() == {"Easy": 0, "Medium": 0, "Hard": 0}


# ---- blind75_count -----------------------------------------------------


def test_blind75_count_only_counts_problems_tagged_with_blind75(
    isolated_metadata,
):
    _write_metadata(
        isolated_metadata,
        [
            {"id": "0001", "path_membership": ["blind75", "neetcode150"]},
            {"id": "0002", "path_membership": ["neetcode150"]},
            {"id": "0003", "path_membership": ["blind75"]},
            {"id": "0004"},  # no path_membership at all
            {"id": "0005", "path_membership": None},
        ],
    )

    assert update_stats.blind75_count() == 2  # 0001 + 0003


def test_blind75_count_returns_zero_when_metadata_missing(tmp_path, monkeypatch):
    monkeypatch.setattr(update_stats, "METADATA", tmp_path / "nope.json")
    assert update_stats.blind75_count() == 0


# ---- reviewed_study_card_count -------------------------------------------


def test_reviewed_study_card_count_only_counts_status_reviewed(isolated_metadata):
    _write_metadata(
        isolated_metadata,
        [
            {"id": "0001", "study_card_status": "reviewed"},
            {"id": "0002", "study_card_status": "draft"},
            {"id": "0003", "study_card_status": "interview-ready"},
            {"id": "0004"},  # no study_card_status
            {"id": "0005", "study_card_status": "reviewed"},
        ],
    )

    # Only "reviewed" counts. "draft" and "interview-ready" are valid
    # states but are NOT surfaced in the README's reviewed-card count
    # (that count gates the "Where to start" curated showcase).
    assert update_stats.reviewed_study_card_count() == 2  # 0001 + 0005


def test_reviewed_study_card_count_returns_zero_when_metadata_missing(
    tmp_path, monkeypatch
):
    monkeypatch.setattr(update_stats, "METADATA", tmp_path / "nope.json")
    assert update_stats.reviewed_study_card_count() == 0


# ---- update_readme (marker substitution) ------------------------------


def test_update_readme_replaces_each_marker_pair(tmp_path, monkeypatch):
    readme = tmp_path / "README.md"
    readme.write_text(
        "Counts: easy <!-- EASY_COUNT_START -->0<!-- EASY_COUNT_END --> / "
        "medium <!-- MEDIUM_COUNT_START -->0<!-- MEDIUM_COUNT_END -->\n",
        encoding="utf-8",
    )
    monkeypatch.setattr(update_stats, "README", readme)

    # Pass only the two metrics that appear in our fake README; full
    # collect_metrics() would also include problem_directories etc., but
    # update_readme requires the marker to exist for every metric it
    # iterates over.
    update_stats.update_readme({"easy_count": 28, "medium_count": 52})

    updated = readme.read_text(encoding="utf-8")
    assert "<!-- EASY_COUNT_START -->28<!-- EASY_COUNT_END -->" in updated
    assert "<!-- MEDIUM_COUNT_START -->52<!-- MEDIUM_COUNT_END -->" in updated


def test_update_readme_raises_when_marker_missing(tmp_path, monkeypatch):
    readme = tmp_path / "README.md"
    readme.write_text("No markers here at all.\n", encoding="utf-8")
    monkeypatch.setattr(update_stats, "README", readme)

    with pytest.raises(ValueError, match="Placeholder not found"):
        update_stats.update_readme({"easy_count": 28})
