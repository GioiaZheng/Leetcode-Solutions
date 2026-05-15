# LeetCode Solutions

![Python](https://img.shields.io/badge/language-python-blue)
![LeetCode](https://img.shields.io/badge/leetcode-solutions-orange)
![License](https://img.shields.io/badge/license-MIT-lightgrey)

A personal collection of Python solutions to LeetCode problems, plus topic notes I write while studying.

This is a study repo, not a library. Solutions are organized one per directory and kept self-contained so I can grep / revisit them quickly before interviews.

---

# Highlights

- Problem directories: <!-- PROBLEM_DIRS_START -->98<!-- PROBLEM_DIRS_END -->
- Standard `solution.py` files: <!-- STANDARD_SOLUTIONS_START -->98<!-- STANDARD_SOLUTIONS_END -->
- Catalog entries: <!-- CATALOG_ENTRIES_START -->98<!-- CATALOG_ENTRIES_END -->
- Topic-tagged catalog ([`CATALOG.md`](CATALOG.md)) regenerated from each problem's `README.md`
- Topic notes under [`0000-notes/`](0000-notes/) (English with partial 中文 translations)

---

# Repository Overview

Each problem directory generally contains:

- `README.md` – problem summary, key insight, complexity analysis
- `solution.py` – my reference solution

Top-level files:

- `CATALOG.md` – generated index, one row per problem
- `0000-notes/` – topic notes (arrays, DP, graphs, …)
- `scripts/` – maintenance scripts (catalog, stats, structure validation)
- `tests/` – pytest cases for solutions that have them

---

# Directory Naming Convention

```
####-problem-name
```

- `####` – four-digit LeetCode problem ID
- `problem-name` – lowercase kebab-case (ASCII only, no `<`, `=`, `>` or other shell-unfriendly characters)

Examples:

```
0001-two-sum
1458-max-dot-product-of-two-subsequences
3453-separate-squares-i
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

Individual `solution.py` files are LeetCode-style modules — a single `class Solution`. They are not meant to be run directly.

---

# Notes Library

Topic indices live under [`0000-notes/`](0000-notes/README.md). Most notes have an English version and a shorter 中文 version.

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

---

# Scope and limitations

What this repo is:

- A personal solution archive that's easy to browse and revisit.
- Topic notes that summarize patterns in my own words.

What this repo is **not**:

- A benchmark or comparative study of algorithms.
- A reusable Python library — there is no shared package, every solution is standalone by design.
- A complete test suite — most problems do not yet have automated tests.

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
  python scripts/update_stats.py
  ```

  Commit the regenerated `CATALOG.md` and `README.md` along with your change.
