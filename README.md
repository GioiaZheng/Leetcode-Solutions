# LeetCode Solutions

![Python](https://img.shields.io/badge/language-python-blue)
![LeetCode](https://img.shields.io/badge/leetcode-solutions-orange)
![Problems](https://img.shields.io/badge/problems-96-green)
![License](https://img.shields.io/badge/license-MIT-lightgrey)

A collection of **Python 3 implementations for LeetCode problems**, organized with consistent structure and concise explanations.
The repository is intended as both a **solution reference** and a **structured review resource** for algorithm practice and interview preparation.

---

# Repository Overview

* **96 solved problems**, each stored in a dedicated directory.
* A **topic-tagged index** available in [`CATALOG.md`](CATALOG.md).
* **Algorithm study notes** located in [`0000-notes/`](0000-notes/), with both English and Chinese versions.

Each problem directory contains:

* `README.md` – problem summary, key insight, and complexity analysis
* `solution.py` – a runnable Python implementation

---

# Repository Structure

```
####-problem-name/
0000-notes/
CATALOG.md
LICENSE
```

Description of key components:

| Path                 | Description                                           |
| -------------------- | ----------------------------------------------------- |
| `####-problem-name/` | One directory per LeetCode problem                    |
| `0000-notes/`        | Algorithm notes and reusable problem-solving patterns |
| `CATALOG.md`         | Full list of solved problems with topic tags          |
| `LICENSE`            | License information                                   |

---

# Directory Naming Convention

All problem directories follow the format:

```
####-problem-name
```

Where:

* `####` – four-digit LeetCode problem ID
* `problem-name` – lowercase title written in **kebab-case**

Examples:

```
0001-two-sum
1458-max-dot-product-of-two-subsequences
3453-separate-squares-i
```

This convention keeps the repository predictable and allows quick navigation by problem ID.

---

# Problem Catalog

The complete list of solved problems is maintained in:

```
CATALOG.md
```

Open the catalog:

[View the problem catalog](CATALOG.md)

The catalog includes:

* Problem ID
* Title
* Directory link
* Topic tags

---

# Quick Start

Clone the repository and run any solution directly.

```bash
git clone https://github.com/<username>/<repo-name>.git
cd <repo-name>

cd 0001-two-sum
python solution.py
```

Most solutions include small test snippets or example usage that can be executed directly.

---

# Notes Library

The repository includes algorithm notes covering common problem-solving patterns.

Main topics include:

* Arrays
* Hash tables
* Two pointers
* Sliding window
* Binary search
* Prefix sums
* Greedy algorithms
* Dynamic programming
* Graph algorithms
* Recursion and backtracking

Full index:

```
0000-notes/README.md
```

These notes are designed as quick references for revisiting common interview techniques.

---

# Contributing

Contributions are welcome.

Please follow the existing repository conventions:

* Use the directory format `####-problem-name`
* Keep implementations clear and self-contained
* Include both:

  * explanation (`README.md`)
  * implementation (`solution.py`)

After adding or removing problems, update the repository statistics using:

```bash
python scripts/update_readme_stats.py
```

---

If you find this repository useful for practice or interview preparation, consider starring the project.
