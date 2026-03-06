# LeetCode Solutions

![Python](https://img.shields.io/badge/language-python-blue) ![LeetCode](https://img.shields.io/badge/leetcode-solutions-orange) ![Problems](https://img.shields.io/badge/problems-96-green) ![License](https://img.shields.io/badge/license-MIT-lightgrey)

A curated collection of **Python 3** LeetCode solutions focused on clarity, consistency, and interview-oriented learning.

## Repository snapshot
- **96 solved problems** organized in standardized directories.
- **Topic-tagged catalog** in [`CATALOG.md`](CATALOG.md) with no `TBD` placeholders.
- **Reusable study notes** in [`0000-notes/`](0000-notes/) with English + Chinese variants.

## Why this repository
This repository is designed as both a **solution archive** and a **study reference** for technical interviews.

Key characteristics:

- Consistent folder structure for every problem
- Clear per-problem README explanations
- Runnable Python implementations
- Topic-based study notes
- English + Chinese note variants

It can be used as:

- an interview revision notebook
- a personal algorithm knowledge base
- a reference for common problem-solving patterns

## Directory Naming Convention
All problem directories follow:

```text
####-problem-name
```

Where:
- `####` = 4-digit problem ID.
- `problem-name` = **kebab-case, lowercase** title.

Canonical format:

```text
problem-id + kebab-case + lowercase
```

Examples:
- `0001-two-sum`
- `1458-max-dot-product-of-two-subsequences`
- `3453-separate-squares-i`

## Repository Structure
- `####-problem-name/` — one problem per directory.
- `0000-notes/` — reusable algorithm notes and study guides.
- `CATALOG.md` — complete problem index.
- `LICENSE` — license information.

## Problem Catalog
- 👉 [Open full problem catalog](CATALOG.md)

## Quick Start
```bash
git clone https://github.com/<username>/<repo-name>.git
cd <repo-name>

cd 0001-two-sum
python solution.py
```

## Notes library
The repository also contains reusable study notes covering common algorithm patterns.

Topics include:

- Arrays
- Hash tables
- Two pointers
- Sliding window
- Binary search
- Prefix sum
- Greedy
- Dynamic programming
- Graph algorithms
- Recursion and backtracking

See the full notes index here:

➡️ [0000-notes/README.md](0000-notes/README.md)

## Contributing
- Follow the naming convention: `####-kebab-case-lowercase`.
- Keep solutions self-contained and readable.
- Include both explanation (`README.md`) and implementation (`solution.py`).
- After adding/removing problem folders, run `python scripts/update_readme_stats.py` to refresh the badge and solved-count line.

---
If this repository helps your interview prep or daily practice, feel free to star it.
