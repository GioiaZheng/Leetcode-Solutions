# NeetCode 150

A broader interview-prep path through 150 problems chosen for both pattern coverage and depth. NeetCode 150 is a strict superset of Blind 75 --- every Blind 75 problem also appears here, plus harder variants and additional topic areas (tries, advanced graphs, intervals, bit manipulation).

## Overview

NeetCode 150 trades the time-efficiency of Blind 75 for thoroughness. Use it when you have 6--12 weeks of preparation rather than 2--3, or when interviews are likely to drill into one or two specific topic areas (trees, graphs, DP) at depth. Membership is declared by setting `"path_membership": ["neetcode150"]` on a problem; the [Problem List](#problem-list) below is auto-regenerated.

Problems tagged with `"blind75"` will typically also be tagged with `"neetcode150"`. Both tags can coexist on the same problem.

## Prerequisites

- Comfortable writing Python `class` methods and using `dict` / `set` / `list` operations.
- Working knowledge of recursion, asymptotic complexity (`O(n)`, `O(n log n)`, ...), and basic data-structure operations (heap push/pop, queue / deque, hash map insert / lookup).
- Familiarity with the six required `problems/####-<slug>/README.md` sections. Problems in this path that already carry an AI-card extension can be identified by the `AI Card` column in the auto-regenerated table below.
- Optional but useful: a clean run through [Blind 75](../blind75/README.md) first, to get the pattern-recognition baseline.

## Milestones

NeetCode 150's canonical 18 pattern groupings:

- **M1 --- Arrays & Hashing** (9 problems)
- **M2 --- Two Pointers** (5)
- **M3 --- Sliding Window** (6)
- **M4 --- Stack** (7)
- **M5 --- Binary Search** (7)
- **M6 --- Linked List** (11)
- **M7 --- Trees** (15)
- **M8 --- Tries** (3)
- **M9 --- Heap / Priority Queue** (7)
- **M10 --- Backtracking** (9)
- **M11 --- Graphs** (13)
- **M12 --- Advanced Graphs** (6)
- **M13 --- 1-D DP** (12)
- **M14 --- 2-D DP** (11)
- **M15 --- Greedy** (8)
- **M16 --- Intervals** (6)
- **M17 --- Math & Geometry** (8)
- **M18 --- Bit Manipulation** (7)

A milestone is "done" when every problem in it has `ai_card_status: reviewed` or better.

## Problem List

<!-- PATH_LIST_START -->
_No problems tagged yet. Add `path_membership: ["neetcode150"]` entries in `metadata.json` to populate this list._
<!-- PATH_LIST_END -->

Regenerate with `python scripts/generate_path.py` (or `python scripts/update_indexes.py` to rebuild all derived indexes).

## Pattern Notes

Each milestone has a corresponding topic note in [`0000-notes/`](../../0000-notes/) where the underlying technique is documented. Work the note before attempting the milestone's problems --- patterns recognised cold are much faster than patterns derived from scratch under interview pressure.

## Mock-Interview Tips

- Time-box at 35--40 minutes per problem on the first pass. The harder NeetCode-150-only problems (intervals, advanced graphs, 2-D DP) genuinely take 30+ minutes the first time; do not be discouraged.
- Treat the problems flagged with a `reviewed` AI card as starting points within each milestone --- their READMEs already document the common mistakes, failure cases, and follow-up directions you are likely to be asked about.
- On the second pass, write the solution from scratch without re-reading the README. Diff against `solution.py` to find the part that still does not come from memory.

## Weekly Plan

A 12-week plan that front-loads the patterns shared with Blind 75 and uses the back half for the NeetCode-150-only categories:

| Week | Focus | Target |
|---|---|---|
| 1 | M1 Arrays & Hashing, M2 Two Pointers | 14 problems, all `ai_card_status: draft` minimum |
| 2 | M3 Sliding Window, M4 Stack | 13 problems |
| 3 | M5 Binary Search, M6 Linked List (part 1) | ~13 problems |
| 4 | M6 Linked List (part 2), M7 Trees (part 1) | ~13 problems |
| 5 | M7 Trees (part 2), M8 Tries | ~13 problems |
| 6 | M9 Heap, M10 Backtracking | 16 problems |
| 7 | M11 Graphs | 13 problems |
| 8 | M12 Advanced Graphs, M13 1-D DP (part 1) | ~12 problems |
| 9 | M13 1-D DP (part 2), M14 2-D DP (part 1) | ~12 problems |
| 10 | M14 2-D DP (part 2), M15 Greedy | ~13 problems |
| 11 | M16 Intervals, M17 Math & Geometry, M18 Bit Manipulation | 21 problems |
| 12 | Review pass | Every problem to `ai_card_status: reviewed`, plus mock-interview rotation |

Pace is aggressive --- 12--14 problems per week is heavy if you are starting from cold. Consider a 16-week version (~10 problems per week) if interviews are not imminent.
