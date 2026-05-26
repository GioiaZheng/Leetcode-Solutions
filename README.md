# LeetCode Solutions

![Python](https://img.shields.io/badge/language-python-blue)
![LeetCode](https://img.shields.io/badge/leetcode-solutions-orange)
![CI](https://github.com/GioiaZheng/Leetcode-Solutions/actions/workflows/quality.yml/badge.svg)
![License](https://img.shields.io/badge/license-MIT-lightgrey)

A personal collection of Python solutions to LeetCode problems, plus topic notes I write while studying.

This is a study repo, not a library. Solutions live under `problems/`, one directory per problem, and are kept self-contained so I can grep / revisit them quickly before interviews.

---

# Highlights

- Problem directories under `problems/`: <!-- PROBLEM_DIRS_START -->98<!-- PROBLEM_DIRS_END -->
- Standard `solution.py` files: <!-- STANDARD_SOLUTIONS_START -->98<!-- STANDARD_SOLUTIONS_END -->
- Catalog entries: <!-- CATALOG_ENTRIES_START -->98<!-- CATALOG_ENTRIES_END -->
- Difficulty mix: Easy <!-- EASY_COUNT_START -->28<!-- EASY_COUNT_END --> / Medium <!-- MEDIUM_COUNT_START -->52<!-- MEDIUM_COUNT_END --> / Hard <!-- HARD_COUNT_START -->18<!-- HARD_COUNT_END --> (regenerated from `metadata.json`)
- Topic index ([`TOPICS.md`](TOPICS.md)) groups problems by major algorithm pattern
- Full catalog ([`CATALOG.md`](CATALOG.md)) regenerated from `metadata.json` + problem directories
- Topic notes under [`0000-notes/`](0000-notes/) (English with partial Chinese translations); see the [Quick Pattern Guide](0000-notes/README.md) for cross-references between patterns and solved problems

---

# Repository Overview

Each problem directory under `problems/` generally contains:

- `README.md` - problem summary, key insight, complexity analysis
- `solution.py` - my reference solution

Top-level files:

- `problems/` - solved problem directories, one per LeetCode problem
- `CATALOG.md` - generated index, one row per problem (id / title / difficulty / status / topics)
- `TOPICS.md` - generated topic index for browsing by major algorithm pattern
- `metadata.json` - source of truth for problem titles, difficulty, topics, and review status; `CATALOG.md` and the README difficulty counts are derived from it
- `templates/problem_README.md` - starter template for new problem READMEs
- `0000-notes/` - topic notes (arrays, DP, graphs, etc.) with a Quick Pattern Guide that cross-references solved problems
- `scripts/` - maintenance scripts (catalog generation, stats, structural + schema validation)
- `tests/` - pytest cases (per-problem and validator self-tests)

---

# Directory Naming Convention

```
problems/####-problem-name
```

- `####` - four-digit LeetCode problem ID
- `problem-name` - lowercase kebab-case (ASCII only, no `<`, `=`, `>` or other shell-unfriendly characters)

Examples:

```
problems/0001-two-sum
problems/1458-max-dot-product-of-two-subsequences
problems/3453-separate-squares-i
```

---

# Quick Start

```bash
git clone https://github.com/GioiaZheng/Leetcode-Solutions.git
cd Leetcode-Solutions

pip install "pytest>=8.0" "ruff>=0.5"

# Structural checks
python scripts/validate_repo.py
python -m compileall -q .

# Tests (only the problems that ship with cases are covered today)
pytest
```

Individual `solution.py` files are LeetCode-style modules - a single `class Solution`. They are not meant to be run directly.

---

# Notes Library

Topic indices live under [`0000-notes/`](0000-notes/README.md). Most notes have an English version and a shorter Chinese version.

Topics:

- 00 how-to-think
- 01 arrays
- 02 hash tables
- 03 two pointers
- 04 sliding window
- 05 binary search
- 06 prefix sums
- 07 greedy
- 08 dynamic programming
- 09 graphs
- 10 how-to-choose-algorithm
- 11 pattern library
- 12 recursion & backtracking
- 13 heap / priority queue

---

# Scope and limitations

What this repo is:

- A personal solution archive that's easy to browse and revisit.
- Topic notes that summarize patterns in my own words.

What this repo is **not**:

- A benchmark or comparative study of algorithms.
- A reusable Python library - there is no shared package, every solution is standalone by design.
- A complete test suite - only a curated subset of problems has automated tests today (see `tests/test_selected_solutions.py`).

---

# Contributing

This is primarily a personal study repo. If you do want to contribute:

- Use the directory format `####-problem-name`.
- Keep solutions in a single `class Solution` with standard LeetCode method signatures.
- Add a `README.md` with problem summary, approach, and complexity.
- If you add tests, put them under `tests/` (see `tests/test_two_sum.py` for the loading pattern).
- After adding problems, regenerate the catalog and stats locally:

  ```bash
  python scripts/generate_catalog.py
  python scripts/generate_topics.py
  python scripts/update_stats.py
  ```

  Commit the regenerated `CATALOG.md`, `TOPICS.md`, and `README.md` along with your change.
