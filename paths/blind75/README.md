# Blind 75

A focused interview-prep path through 75 problems chosen for breadth-of-pattern coverage rather than topic depth.

## Overview

The Blind 75 is the canonical short list for filling pattern gaps before a coding interview. This page groups the 75 problems by pattern and tracks completion against `metadata.json`. Membership is declared by setting `"path_membership": ["blind75"]` on a problem; the [Problem List](#problem-list) below is auto-regenerated.

## Prerequisites

- Comfortable writing Python `class` methods and using `dict` / `set` / `list` operations.
- Basic asymptotic-complexity vocabulary (`O(n)`, `O(n log n)`, …).
- Familiarity with the six required `problems/####-<slug>/README.md` sections (Problem / Intuition / Approach / Complexity / Edge Cases / Code).

## Milestones

- **M1 — Arrays & Hashing** (10 problems) — pattern-recognition warmup.
- **M2 — Two Pointers & Sliding Window** (12 problems) — pointer arithmetic and window invariants.
- **M3 — Stack, Queues & Binary Search** (10 problems) — classic data-structure mechanics.
- **M4 — Linked Lists & Trees** (15 problems) — recursion versus iteration on linear and branched structures.
- **M5 — Tries, Heaps & Graphs** (15 problems) — non-trivial data structures and BFS / DFS.
- **M6 — Dynamic Programming & Greedy** (13 problems) — state definition and transition design.

A milestone is "done" when every problem in it has `ai_card_status: reviewed` or better.

## Problem List

<!-- PATH_LIST_START -->
| # | ID | Problem | Difficulty | Directory |
|---:|---:|---|---|---|
| 1 | 0001 | Two Sum | Easy | [`problems/0001-two-sum/`](../../problems/0001-two-sum/) |
| 2 | 0003 | Longest Substring Without Repeating Characters | Medium | [`problems/0003-longest-substring-without-repeating-characters/`](../../problems/0003-longest-substring-without-repeating-characters/) |
| 3 | 0005 | Longest Palindromic Substring | Medium | [`problems/0005-longest-palindromic-substring/`](../../problems/0005-longest-palindromic-substring/) |
| 4 | 0011 | Container With Most Water | Medium | [`problems/0011-container-with-most-water/`](../../problems/0011-container-with-most-water/) |
| 5 | 0015 | 3sum | Medium | [`problems/0015-3sum/`](../../problems/0015-3sum/) |
| 6 | 0049 | Group Anagrams | Medium | [`problems/0049-group-anagrams/`](../../problems/0049-group-anagrams/) |
| 7 | 0121 | Best Time To Buy And Sell Stock | Easy | [`problems/0121-best-time-to-buy-and-sell-stock/`](../../problems/0121-best-time-to-buy-and-sell-stock/) |
| 8 | 0242 | Valid Anagram | Easy | [`problems/0242-valid-anagram/`](../../problems/0242-valid-anagram/) |
| 9 | 0347 | Top K Frequent Elements | Medium | [`problems/0347-top-k-frequent-elements/`](../../problems/0347-top-k-frequent-elements/) |
<!-- PATH_LIST_END -->

Regenerate with `python scripts/generate_path.py` (or `python scripts/update_indexes.py` to rebuild all derived indexes).

## Pattern Notes

Each milestone has a corresponding topic note in [`0000-notes/`](../../0000-notes/) — work the note before attempting the milestone's problems.

## Mock-Interview Tips

- Time-box at 35 minutes per problem on the first pass. If stuck at 15 minutes, write down the blocker (no recall, no data-structure choice, no invariant) before peeking at the solution.
- On the second pass, write the solution from scratch without re-reading the README. Diff against `solution.py` to find the part that still does not come from memory.
- Use the **Common mistakes** section of each problem README as a checklist while reviewing.

## Weekly Plan

| Week | Focus | Target |
|---|---|---|
| 1 | M1 Arrays & Hashing | 10 problems, all `ai_card_status: draft` minimum |
| 2 | M2 Two Pointers & Sliding Window | 12 problems |
| 3 | M3 Stack, Queues & Binary Search | 10 problems |
| 4 | M4 Linked Lists & Trees | 15 problems |
| 5 | M5 Tries, Heaps & Graphs | 15 problems |
| 6 | M6 DP & Greedy | 13 problems |
| 7 | Review pass | Every problem to `ai_card_status: reviewed` |
| 8 | Mock interviews | Top-up gaps; tag `interview-ready` |
