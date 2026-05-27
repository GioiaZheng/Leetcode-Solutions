# Notes Index

Concise, interview-oriented notes for reusable algorithm patterns. Start with the quick pattern guide below, then use the detailed topic files for deeper review.

> **Looking for annotated showcases?** The repo's [README "Where to start"](../README.md#where-to-start) section curates the problems whose READMEs carry a reviewed AI-card extension — brute-force baseline, common mistakes, failure cases (>=2), interview follow-ups, and a bilingual English + Chinese summary — on top of the standard problem write-up. Several of the **Solved Examples** linked from the table below (e.g. `0003`, `0011`, `0015`) are part of that showcase set.

## Quick Pattern Guide

| Pattern | Use When | Core Files | Solved Examples |
|---|---|---|---|
| Sliding window | Contiguous subarray/substring with a moving constraint | [fixed](04-sliding-window/sliding-window-fixed.md), [variable](04-sliding-window/sliding-window-variable.md) | [`0003`](../problems/0003-longest-substring-without-repeating-characters/), [`1888`](../problems/1888-minimum-number-of-flips-to-make-the-binary-string-alternating/), [`3578`](../problems/3578-count-partitions-with-max-min-difference-at-most-k/) |
| Two pointers | Ordered arrays/strings, pair checks, in-place filtering | [two pointers basics](03-two-pointers/two-pointers-basics.md) | [`0015`](../problems/0015-3sum/), [`0026`](../problems/0026-remove-duplicates-from-sorted-array/), [`0011`](../problems/0011-container-with-most-water/) |
| Binary search on answer | Numeric answer + monotonic feasibility check | [binary search on answer](05-binary-search/binary-search-on-answer.md) | [`2141`](../problems/2141-maximum-running-time-of-n-computers/), [`3453`](../problems/3453-separate-squares-i/), [`1292`](../problems/1292-maximum-side-length-of-a-square-with-sum-at-most-threshold/) |
| Prefix sum | Repeated range sums/counts or prefix-difference logic | [prefix sum](06-prefix-sum/prefix-sum.md) | [`1590`](../problems/1590-make-sum-divisible-by-p/), [`2435`](../problems/2435-paths-in-matrix-divisible-by-k/), [`3381`](../problems/3381-maximum-subarray-sum-with-length-divisible-by-k/) |
| Dynamic programming | Overlapping subproblems with choices affecting future states | [DP summary](08-dynamic-programming/summary.md) | [`1458`](../problems/1458-max-dot-product-of-two-subsequences/), [`0712`](../problems/0712-minimum-ascii-delete-sum-for-two-strings/), [`2435`](../problems/2435-paths-in-matrix-divisible-by-k/) |
| Graph BFS/DFS | Reachability, components, level order, unweighted shortest paths | [summary](09-graph/summary.md), [BFS](09-graph/bfs.md), [DFS](09-graph/dfs.md), [graph basics](09-graph/graph-basics.md) | [`2092`](../problems/2092-find-all-people-with-secret/), [`0756`](../problems/0756-pyramid-transition-matrix/), [`1161`](../problems/1161-maximum-level-of-a-binary-tree/) |
| Heap / priority queue | Repeatedly need min/max, top-k, scheduling, delayed processing | [heap / priority queue](13-heap/heap-priority-queue.md) | [`2402`](../problems/2402-meeting-rooms-iii/), [`0692`](../problems/0692-top-k-frequent-words/), [`2343`](../problems/2343-query-kth-smallest-trimmed-number/) |

---

## 00-how-to-think
- [common mistakes](00-how-to-think/common-mistakes.md) ([zh](00-how-to-think/common-mistakes-zh.md))
- [how to choose algorithms](00-how-to-think/how-to-choose-algorithms.md) ([zh](00-how-to-think/how-to-choose-algorithms-zh.md))
- [how to read problems](00-how-to-think/how-to-read-problems.md) ([zh](00-how-to-think/how-to-read-problems-zh.md))

## 01-array
- [array basics](01-array/array-basics.md) ([zh](01-array/array-basics-zh.md))

## 02-hash-table
- [bucket technique](02-hash-table/bucket-technique.md) ([zh](02-hash-table/bucket-technique-zh.md))
- [frequency count](02-hash-table/frequency-count.md) ([zh](02-hash-table/frequency-count-zh.md))
- [hashing basics](02-hash-table/hashing-basics.md) ([zh](02-hash-table/hashing-basics-zh.md))

## 03-two-pointers
- [two pointers basics](03-two-pointers/two-pointers-basics.md) ([zh](03-two-pointers/two-pointers-basics-zh.md))

## 04-sliding-window
- [sliding window fixed](04-sliding-window/sliding-window-fixed.md) ([zh](04-sliding-window/sliding-window-fixed-zh.md))
- [sliding window variable](04-sliding-window/sliding-window-variable.md) ([zh](04-sliding-window/sliding-window-variable-zh.md))

## 05-binary-search
- [binary search on answer](05-binary-search/binary-search-on-answer.md) ([zh](05-binary-search/binary-search-on-answer-zh.md))
- [binary search on array](05-binary-search/binary-search-on-array.md) ([zh](05-binary-search/binary-search-on-array-zh.md))

## 06-prefix-sum
- [difference array](06-prefix-sum/difference-array.md) ([zh](06-prefix-sum/difference-array-zh.md))
- [prefix sum](06-prefix-sum/prefix-sum.md) ([zh](06-prefix-sum/prefix-sum-zh.md))

## 07-greedy
- [greedy thinking](07-greedy/greedy-thinking.md) ([zh](07-greedy/greedy-thinking-zh.md))
- [interval greedy](07-greedy/interval-greedy.md) ([zh](07-greedy/interval-greedy-zh.md))

## 08-dynamic-programming
- [dp introduction](08-dynamic-programming/dp-introduction.md) ([zh](08-dynamic-programming/dp-introduction-zh.md))
- [dp on array](08-dynamic-programming/dp-on-array.md) ([zh](08-dynamic-programming/dp-on-array-zh.md))
- [dp on strings](08-dynamic-programming/dp-on-strings.md) ([zh](08-dynamic-programming/dp-on-strings-zh.md))
- [dp state design](08-dynamic-programming/dp-state-design.md) ([zh](08-dynamic-programming/dp-state-design-zh.md))
- [summary](08-dynamic-programming/summary.md) ([zh](08-dynamic-programming/summary-zh.md))

## 09-graph
- [summary](09-graph/summary.md)
- [bfs](09-graph/bfs.md) ([zh](09-graph/bfs-zh.md))
- [dfs](09-graph/dfs.md)
- [graph basics](09-graph/graph-basics.md) ([zh](09-graph/graph-basics-zh.md))
- [shortest path dijkstra](09-graph/shortest-path-dijkstra.md) ([zh](09-graph/shortest-path-dijkstra-zh.md))
- [topological sort](09-graph/topological-sort.md) ([zh](09-graph/topological-sort-zh.md))
- [union find](09-graph/union-find.md) ([zh](09-graph/union-find-zh.md))

## 10-how-to-choose-algorithm
- [algorithm selection guide](10-how-to-choose-algorithm/algorithm-selection-guide.md) ([zh](10-how-to-choose-algorithm/algorithm-selection-guide-zh.md))

## 11-pattern-library
- [core patterns](11-pattern-library/core-patterns.md) ([zh](11-pattern-library/core-patterns-zh.md))

## 12-recursion-backtracking
- [backtracking template](12-recursion-backtracking/backtracking-template.md) ([zh](12-recursion-backtracking/backtracking-template-zh.md))
- [recursion basics](12-recursion-backtracking/recursion-basics.md) ([zh](12-recursion-backtracking/recursion-basics-zh.md))

## 13-heap
- [heap / priority queue](13-heap/heap-priority-queue.md)
