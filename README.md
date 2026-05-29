# LeetCode Solutions

![Python](https://img.shields.io/badge/language-python-blue)
![LeetCode](https://img.shields.io/badge/leetcode-solutions-orange)
![CI](https://github.com/GioiaZheng/Leetcode-Solutions/actions/workflows/quality.yml/badge.svg)
![License](https://img.shields.io/badge/license-MIT-lightgrey)

A personal collection of Python solutions to LeetCode problems, plus topic notes I write while studying.

This is a study repo, not a library. Solutions live under `problems/`, one directory per problem, and are kept self-contained so I can grep / revisit them quickly before interviews.

---

# Highlights

- Problem directories under `problems/`: <!-- PROBLEM_DIRS_START -->99<!-- PROBLEM_DIRS_END -->
- Standard `solution.py` files: <!-- STANDARD_SOLUTIONS_START -->99<!-- STANDARD_SOLUTIONS_END -->
- Catalog entries: <!-- CATALOG_ENTRIES_START -->99<!-- CATALOG_ENTRIES_END -->
- Difficulty mix: Easy <!-- EASY_COUNT_START -->28<!-- EASY_COUNT_END --> / Medium <!-- MEDIUM_COUNT_START -->52<!-- MEDIUM_COUNT_END --> / Hard <!-- HARD_COUNT_START -->19<!-- HARD_COUNT_END --> (regenerated from `metadata.json`)
- Topic index ([`TOPICS.md`](TOPICS.md)) groups problems by major algorithm pattern
- Full catalog ([`CATALOG.md`](CATALOG.md)) regenerated from `metadata.json` + problem directories
- Topic notes under [`0000-notes/`](0000-notes/) (English with partial Chinese translations); see the [Quick Pattern Guide](0000-notes/README.md) for cross-references between patterns and solved problems
- Curated learning paths under [`paths/`](paths/); **Blind 75** path live (<!-- BLIND75_COUNT_START -->10<!-- BLIND75_COUNT_END -->/75 problems tagged, <!-- REVIEWED_STUDY_CARDS_START -->13<!-- REVIEWED_STUDY_CARDS_END --> with reviewed study cards)

---

# Repository Overview

Each problem directory under `problems/` generally contains:

- `README.md` - problem summary, key insight, complexity analysis
- `solution.py` - my reference solution

Top-level files:

- [`problems/`](problems/) - solved problem directories, one per LeetCode problem
- [`paths/`](paths/) - curated learning paths (Blind 75, NeetCode 150) with hand-written narrative and an auto-generated Problem List per path
- `CATALOG.md` - generated index, one row per problem (id / title / difficulty / status / topics)
- `TOPICS.md` - generated topic index for browsing by major algorithm pattern
- `metadata.json` - source of truth for problem titles, difficulty, topics, and review status; `CATALOG.md` and the README difficulty counts are derived from it
- `templates/problem_README.md` - starter template for new problem READMEs
- `0000-notes/` - topic notes (arrays, DP, graphs, etc.) with a Quick Pattern Guide that cross-references solved problems
- `scripts/` - maintenance scripts (catalog generation, stats, structural + schema validation)
- `tests/` - pytest cases (per-problem and validator self-tests)
- `CONTRIBUTING.md` - rules for adding problems, updating metadata, and running local checks

---

# Where to start

The reviewed Study Card showcases below are the recommended entry points. Each problem README carries a brute-force baseline, common mistakes, failure cases, interview follow-ups, and a bilingual English + Chinese summary on top of the standard six core sections (Problem / Intuition / Approach / Complexity / Edge Cases / Code).

<!-- FEATURED_LIST_START -->
| # | ID | Problem | Difficulty | Paths | Primary topic |
|---:|---:|---|---|---|---|
| 1 | 0001 | [Two Sum](problems/0001-two-sum/) | Easy | blind75, neetcode150 | Hashing |
| 2 | 0003 | [Longest Substring Without Repeating Characters](problems/0003-longest-substring-without-repeating-characters/) | Medium | blind75, neetcode150 | Two Pointers & Sliding Window |
| 3 | 0004 | [Median Of Two Sorted Arrays](problems/0004-median-of-two-sorted-arrays/) | Hard | neetcode150 | Binary Search |
| 4 | 0005 | [Longest Palindromic Substring](problems/0005-longest-palindromic-substring/) | Medium | blind75, neetcode150 | Two Pointers & Sliding Window |
| 5 | 0010 | [Regular Expression Matching](problems/0010-regular-expression-matching/) | Hard | neetcode150 | Dynamic Programming |
| 6 | 0011 | [Container With Most Water](problems/0011-container-with-most-water/) | Medium | blind75, neetcode150 | Two Pointers & Sliding Window |
| 7 | 0015 | [3sum](problems/0015-3sum/) | Medium | blind75, neetcode150 | Two Pointers & Sliding Window |
| 8 | 0042 | [Trapping Rain Water](problems/0042-trapping-rain-water/) | Hard | blind75, neetcode150 | Dynamic Programming |
| 9 | 0049 | [Group Anagrams](problems/0049-group-anagrams/) | Medium | blind75, neetcode150 | Hashing |
| 10 | 0085 | [Maximal Rectangle](problems/0085-maximal-rectangle/) | Hard |  | Dynamic Programming |
| 11 | 0121 | [Best Time To Buy And Sell Stock](problems/0121-best-time-to-buy-and-sell-stock/) | Easy | blind75, neetcode150 | Greedy |
| 12 | 0242 | [Valid Anagram](problems/0242-valid-anagram/) | Easy | blind75, neetcode150 | Sorting & Heap |
| 13 | 0347 | [Top K Frequent Elements](problems/0347-top-k-frequent-elements/) | Medium | blind75, neetcode150 | Sorting & Heap |
<!-- FEATURED_LIST_END -->

Regenerated from `study_card_status: reviewed` entries in `metadata.json` by `python scripts/update_indexes.py`. Primary topic is derived from the first entry in each problem's `topics` list mapped to the canonical categories defined in `scripts/generate_topics.py`.

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

pip install -e ".[dev]"

# Local quality checks
python scripts/validate_repo.py
python scripts/security_scan.py
python -m compileall -q .
ruff check .
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

# Learning Paths

Curated study paths live under [`paths/`](paths/). Each path has a hand-written narrative (overview, prerequisites, milestones, weekly plan, mock-interview tips) plus an auto-generated **Problem List** between sentinel comments, derived from the `path_membership` field in `metadata.json`.

Live paths:

- [**Blind 75**](paths/blind75/README.md) - <!-- BLIND75_COUNT_START -->10<!-- BLIND75_COUNT_END -->/75 problems tagged so far; <!-- REVIEWED_STUDY_CARDS_START -->13<!-- REVIEWED_STUDY_CARDS_END --> of those carry a `reviewed` study card with brute-force baseline, common mistakes, failure cases, interview follow-ups, and a bilingual English + Chinese summary (see [`CONTRIBUTING.md`](CONTRIBUTING.md) section "Optional Problem README Sections (Study Card)").

`paths/<name>/README.md` files are regenerated by `python scripts/update_indexes.py`. Problem membership is declared in `metadata.json`, not by moving directories.

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

See [`CONTRIBUTING.md`](CONTRIBUTING.md) for problem layout rules, metadata
updates, and local checks to run before committing.
