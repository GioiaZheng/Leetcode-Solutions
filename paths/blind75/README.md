# Blind 75

A focused interview-prep path through 75 problems chosen for breadth-of-pattern coverage rather than topic depth.

## Overview

The Blind 75 is the canonical short list for filling pattern gaps before a coding interview. This page groups the 75 problems by pattern and tracks completion against `metadata.json`. Membership is declared by setting `"path_membership": ["blind75"]` on a problem; the [Problem List](#problem-list) below is auto-regenerated.

## Prerequisites

- Comfortable writing Python `class` methods and using `dict` / `set` / `list` operations.
- Basic asymptotic-complexity vocabulary (`O(n)`, `O(n log n)`, …).
- Familiarity with the six required `problems/####-<slug>/README.md` sections (Problem / Intuition / Approach / Complexity / Edge Cases / Code).

## Milestones

The Blind 75 path groups its 75 problems into six pattern milestones. The table below is auto-regenerated from `milestones["blind75"]` entries in `metadata.json`; **Canonical** = problems per milestone on the source list, **In repo** = problems already living under `problems/` and tagged into this milestone, **Reviewed** = subset of those that also carry an AI-card extension (`ai_card_status: "reviewed"`).

<!-- MILESTONES_START -->
| # | Milestone | Canonical | In repo | Reviewed |
|---|---|---:|---:|---:|
| M1 | Arrays & Hashing | 10 | 3 | 3 |
| M2 | Two Pointers & Sliding Window | 12 | 5 | 5 |
| M3 | Stack, Queues & Binary Search | 10 | 0 | 0 |
| M4 | Linked Lists & Trees | 15 | 0 | 0 |
| M5 | Tries, Heaps & Graphs | 15 | 1 | 1 |
| M6 | Dynamic Programming & Greedy | 13 | 1 | 1 |
| **Total** | | **75** | **10** | **10** |
<!-- MILESTONES_END -->

A milestone is "done" when every problem in it has `ai_card_status: reviewed` or better.

## Problem List

<!-- PATH_LIST_START -->
| # | ID | Problem | Difficulty | AI Card | Directory |
|---:|---:|---|---|---|---|
| 1 | 0001 | Two Sum | Easy | [reviewed](../../problems/0001-two-sum/README.md#brute-force-baseline) | [`problems/0001-two-sum/`](../../problems/0001-two-sum/) |
| 2 | 0003 | Longest Substring Without Repeating Characters | Medium | [reviewed](../../problems/0003-longest-substring-without-repeating-characters/README.md#brute-force-baseline) | [`problems/0003-longest-substring-without-repeating-characters/`](../../problems/0003-longest-substring-without-repeating-characters/) |
| 3 | 0005 | Longest Palindromic Substring | Medium | [reviewed](../../problems/0005-longest-palindromic-substring/README.md#brute-force-baseline) | [`problems/0005-longest-palindromic-substring/`](../../problems/0005-longest-palindromic-substring/) |
| 4 | 0011 | Container With Most Water | Medium | [reviewed](../../problems/0011-container-with-most-water/README.md#brute-force-baseline) | [`problems/0011-container-with-most-water/`](../../problems/0011-container-with-most-water/) |
| 5 | 0015 | 3sum | Medium | [reviewed](../../problems/0015-3sum/README.md#brute-force-baseline) | [`problems/0015-3sum/`](../../problems/0015-3sum/) |
| 6 | 0042 | Trapping Rain Water | Hard | [reviewed](../../problems/0042-trapping-rain-water/README.md#brute-force-baseline) | [`problems/0042-trapping-rain-water/`](../../problems/0042-trapping-rain-water/) |
| 7 | 0049 | Group Anagrams | Medium | [reviewed](../../problems/0049-group-anagrams/README.md#brute-force-baseline) | [`problems/0049-group-anagrams/`](../../problems/0049-group-anagrams/) |
| 8 | 0121 | Best Time To Buy And Sell Stock | Easy | [reviewed](../../problems/0121-best-time-to-buy-and-sell-stock/README.md#brute-force-baseline) | [`problems/0121-best-time-to-buy-and-sell-stock/`](../../problems/0121-best-time-to-buy-and-sell-stock/) |
| 9 | 0242 | Valid Anagram | Easy | [reviewed](../../problems/0242-valid-anagram/README.md#brute-force-baseline) | [`problems/0242-valid-anagram/`](../../problems/0242-valid-anagram/) |
| 10 | 0347 | Top K Frequent Elements | Medium | [reviewed](../../problems/0347-top-k-frequent-elements/README.md#brute-force-baseline) | [`problems/0347-top-k-frequent-elements/`](../../problems/0347-top-k-frequent-elements/) |
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
