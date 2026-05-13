# LeetCode Solutions

![Python](https://img.shields.io/badge/language-python-blue)
![LeetCode](https://img.shields.io/badge/leetcode-solutions-orange)
![License](https://img.shields.io/badge/license-MIT-lightgrey)

A structured collection of **Python implementations for LeetCode problems**, designed for algorithm practice, interview preparation, and reusable problem-solving patterns.

This repository serves as both a **solution archive** and a **long-term algorithm reference**.

---

# What This Repository Demonstrates

This repository demonstrates:

- Consistent problem-solving patterns across algorithm categories
- Clean and reusable Python implementations
- Systematic organization for long-term knowledge retention
- Automated repository maintenance using GitHub Actions

It reflects a structured approach to algorithm learning and engineering discipline.

---

# Highlights

- Problem directories: <!-- PROBLEM_DIRS_START -->98<!-- PROBLEM_DIRS_END -->
- Standard `solution.py` files: <!-- STANDARD_SOLUTIONS_START -->96<!-- STANDARD_SOLUTIONS_END -->
- Catalog entries: <!-- CATALOG_ENTRIES_START -->98<!-- CATALOG_ENTRIES_END -->
- Topic-tagged catalog for fast lookup
- Reusable notes for common algorithm patterns

---

# Repository Overview

Problem directories generally include:

- `README.md` – explanation, key insight, and complexity analysis
- `solution.py` – standard solution file when available

Additional resources:

- `CATALOG.md` – generated problem catalog with topic tags
- `0000-notes/` – reusable algorithm notes and patterns

---

# Repository Structure

```

####-problem-name/
0000-notes/
CATALOG.md
LICENSE

```

| Path                 | Description                                           |
|----------------------|-------------------------------------------------------|
| `####-problem-name/` | One directory per LeetCode problem                    |
| `0000-notes/`        | Algorithm notes and reusable problem-solving patterns |
| `CATALOG.md`         | Generated problem catalog with topic tags             |
| `LICENSE`            | License information                                   |

---

# Directory Naming Convention

All problem directories follow:

```

####-problem-name

```

Where:

- `####` – four-digit LeetCode problem ID
- `problem-name` – lowercase kebab-case

Examples:

```

0001-two-sum
1458-max-dot-product-of-two-subsequences
3453-separate-squares-i

```

---

# Problem Catalog

Generated full list:

[View the problem catalog](CATALOG.md)

Includes:

- Problem ID
- Title
- Directory link
- Topic tags

---

# Quick Start

```bash
git clone https://github.com/GioiaZheng/Leetcode-Solutions.git
cd Leetcode-Solutions

python scripts/validate_repo.py
python -m compileall -q .
pytest
```

Individual LeetCode files are primarily solution modules for reference and submission. Run them directly only when a file includes its own test harness or an accompanying test exists.

---

# Notes Library

Topics covered:

* Arrays
* Hash tables
* Two pointers
* Sliding window
* Binary search
* Prefix sums
* Greedy algorithms
* Dynamic programming
* Graph algorithms
* Recursion & backtracking

See:

```
0000-notes/README.md
```

---

# Why This Repository

Algorithm practice is most effective when solutions are easy to revisit and generalize.

This repository is designed to support:

* fast review before interviews
* pattern recognition across problems
* reusable knowledge for common techniques

---

# Contributing

Contributions are welcome.

Guidelines:

* Use directory format `####-problem-name`
* Keep solutions clear and self-contained
* Include an explanation and implementation
* Add tests or an example main block when marking a solution as tested

After adding problems, regenerate the catalog and update statistics:

```bash
python scripts/generate_catalog.py
python scripts/update_stats.py
```

---

If you find this repository useful, consider starring ⭐ the project.
