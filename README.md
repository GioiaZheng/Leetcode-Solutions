# LeetCode Solutions

![Python](https://img.shields.io/badge/language-python-blue)
![LeetCode](https://img.shields.io/badge/leetcode-solutions-orange)
![Problems](https://img.shields.io/badge/problems-96-green)
![License](https://img.shields.io/badge/license-MIT-lightgrey)

A structured collection of **Python implementations for LeetCode problems**, designed for algorithm practice, interview preparation, and reusable problem-solving patterns.

This repository serves as both a **solution archive** and a **long-term algorithm reference**.

---

# Highlights

- <!-- SOLVED_COUNT_START -->96<!-- SOLVED_COUNT_END --> solved problems
- Topic-tagged catalog for fast lookup
- Reusable notes for common algorithm patterns
- Consistent directory structure for maintainability
- Runnable Python solutions with explanations

---

# Repository Overview

Each problem is stored in an individual directory with:

- `README.md` – explanation, key insight, and complexity analysis  
- `solution.py` – clean and runnable implementation  

Additional resources:

- `CATALOG.md` – full index of solved problems with topic tags  
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
| `CATALOG.md`         | Full list of solved problems with topic tags          |
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

````

---

# Problem Catalog

Full list:

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

cd 0001-two-sum
python solution.py
````

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
* Include both explanation and implementation

After adding problems, update statistics:

```bash
python scripts/update_stats.py
```

---

If you find this repository useful, consider starring ⭐ the project.
