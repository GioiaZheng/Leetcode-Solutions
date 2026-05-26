# Notes Index

Concise, interview-oriented notes for reusable algorithm patterns. Start with the quick pattern guide below, then use the detailed topic files for deeper review.

## Quick Pattern Guide

| Pattern | Use When | Core Files | Solved Examples |
|---|---|---|---|
| Sliding window | Contiguous subarray/substring with a moving constraint | [fixed](04-sliding-window/sliding-window-fixed.md), [variable](04-sliding-window/sliding-window-variable.md) | [`0003`](../problems/0003-longest-substring-without-repeating-characters/), [`1888`](../problems/1888-minimum-number-of-flips-to-make-the-binary-string-alternating/), [`3578`](../problems/3578-count-partitions-with-max-min-difference-at-most-k/) |
| Two pointers | Ordered arrays/strings, pair checks, in-place filtering | [two pointers basics](03-two-pointers/two-pointers-basics.md) | [`0015`](../problems/0015-3sum/), [`0026`](../problems/0026-remove-duplicates-from-sorted-array/), [`0011`](../problems/0011-container-with-most-water/) |
| Binary search on answer | Numeric answer + monotonic feasibility check | [binary search on answer](05-binary-search/binary-search-on-answer.md) | [`2141`](../problems/2141-maximum-running-time-of-n-computers/), [`3453`](../problems/3453-separate-squares-i/), [`1292`](../problems/1292-maximum-side-length-of-a-square-with-sum-at-most-threshold/) |
| Prefix sum | Repeated range sums/counts or prefix-difference logic | [prefix sum](06-prefix-sum/prefix-sum.md) | [`1590`](../problems/1590-make-sum-divisible-by-p/), [`2435`](../problems/2435-paths-in-matrix-divisible-by-k/), [`3381`](../problems/3381-maximum-subarray-sum-with-length-divisible-by-k/) |
| Dynamic programming | Overlapping subproblems with choices affecting future states | [DP summary](08-dynamic-programming/summary.md) | [`1458`](../problems/1458-max-dot-product-of-two-subsequences/), [`0712`](../problems/0712-minimum-ascii-delete-sum-for-two-strings/), [`2435`](../problems/2435-paths-in-matrix-divisible-by-k/) |
| Graph BFS/DFS | Reachability, components, level order, unweighted shortest paths | [BFS](09-graph/bfs.md), [DFS](09-graph/dfs.md), [graph basics](09-graph/graph-basics.md) | [`2092`](../problems/2092-find-all-people-with-secret/), [`0756`](../problems/0756-pyramid-transition-matrix/), [`1161`](../problems/1161-maximum-level-of-a-binary-tree/) |
| Heap / priority queue | Repeatedly need min/max, top-k, scheduling, delayed processing | [heap / priority queue](13-heap/heap-priority-queue.md) | [`2402`](../problems/2402-meeting-rooms-iii/), [`0692`](../problems/0692-top-k-frequent-words/), [`2343`](../problems/2343-query-kth-smallest-trimmed-number/) |

---

## 00-how-to-think
- [common mistakes](00-how-to-think/common-mistakes.md)ï¼ˆ[ä¸­æ–‡](00-how-to-think/common-mistakes-zh.md)ï¼‰
- [how to choose algorithms](00-how-to-think/how-to-choose-algorithms.md)ï¼ˆ[ä¸­æ–‡](00-how-to-think/how-to-choose-algorithms-zh.md)ï¼‰
- [how to read problems](00-how-to-think/how-to-read-problems.md)ï¼ˆ[ä¸­æ–‡](00-how-to-think/how-to-read-problems-zh.md)ï¼‰

## 01-array
- [array basics](01-array/array-basics.md)ï¼ˆ[ä¸­æ–‡](01-array/array-basics-zh.md)ï¼‰

## 02-hash-table
- [bucket technique](02-hash-table/bucket-technique.md)ï¼ˆ[ä¸­æ–‡](02-hash-table/bucket-technique-zh.md)ï¼‰
- [frequency count](02-hash-table/frequency-count.md)ï¼ˆ[ä¸­æ–‡](02-hash-table/frequency-count-zh.md)ï¼‰
- [hashing basics](02-hash-table/hashing-basics.md)ï¼ˆ[ä¸­æ–‡](02-hash-table/hashing-basics-zh.md)ï¼‰

## 03-two-pointers
- [two pointers basics](03-two-pointers/two-pointers-basics.md)ï¼ˆ[ä¸­æ–‡](03-two-pointers/two-pointers-basics-zh.md)ï¼‰

## 04-sliding-window
- [sliding window fixed](04-sliding-window/sliding-window-fixed.md)ï¼ˆ[ä¸­æ–‡](04-sliding-window/sliding-window-fixed-zh.md)ï¼‰
- [sliding window variable](04-sliding-window/sliding-window-variable.md)ï¼ˆ[ä¸­æ–‡](04-sliding-window/sliding-window-variable-zh.md)ï¼‰

## 05-binary-search
- [binary search on answer](05-binary-search/binary-search-on-answer.md)ï¼ˆ[ä¸­æ–‡](05-binary-search/binary-search-on-answer-zh.md)ï¼‰
- [binary search on array](05-binary-search/binary-search-on-array.md)ï¼ˆ[ä¸­æ–‡](05-binary-search/binary-search-on-array-zh.md)ï¼‰

## 06-prefix-sum
- [difference array](06-prefix-sum/difference-array.md)ï¼ˆ[ä¸­æ–‡](06-prefix-sum/difference-array-zh.md)ï¼‰
- [prefix sum](06-prefix-sum/prefix-sum.md)ï¼ˆ[ä¸­æ–‡](06-prefix-sum/prefix-sum-zh.md)ï¼‰

## 07-greedy
- [greedy thinking](07-greedy/greedy-thinking.md)ï¼ˆ[ä¸­æ–‡](07-greedy/greedy-thinking-zh.md)ï¼‰
- [interval greedy](07-greedy/interval-greedy.md)ï¼ˆ[ä¸­æ–‡](07-greedy/interval-greedy-zh.md)ï¼‰

## 08-dynamic-programming
- [dp introduction](08-dynamic-programming/dp-introduction.md)ï¼ˆ[ä¸­æ–‡](08-dynamic-programming/dp-introduction-zh.md)ï¼‰
- [dp on array](08-dynamic-programming/dp-on-array.md)ï¼ˆ[ä¸­æ–‡](08-dynamic-programming/dp-on-array-zh.md)ï¼‰
- [dp on strings](08-dynamic-programming/dp-on-strings.md)ï¼ˆ[ä¸­æ–‡](08-dynamic-programming/dp-on-strings-zh.md)ï¼‰
- [dp state design](08-dynamic-programming/dp-state-design.md)ï¼ˆ[ä¸­æ–‡](08-dynamic-programming/dp-state-design-zh.md)ï¼‰
- [summary](08-dynamic-programming/summary.md)ï¼ˆ[ä¸­æ–‡](08-dynamic-programming/summary-zh.md)ï¼‰

## 09-graph
- [bfs](09-graph/bfs.md)ï¼ˆ[ä¸­æ–‡](09-graph/bfs-zh.md)ï¼‰
- [dfs](09-graph/dfs.md)
- [graph basics](09-graph/graph-basics.md)ï¼ˆ[ä¸­æ–‡](09-graph/graph-basics-zh.md)ï¼‰
- [shortest path dijkstra](09-graph/shortest-path-dijkstra.md)ï¼ˆ[ä¸­æ–‡](09-graph/shortest-path-dijkstra-zh.md)ï¼‰
- [topological sort](09-graph/topological-sort.md)ï¼ˆ[ä¸­æ–‡](09-graph/topological-sort-zh.md)ï¼‰
- [union find](09-graph/union-find.md)ï¼ˆ[ä¸­æ–‡](09-graph/union-find-zh.md)ï¼‰

## 10-how-to-choose-algorithm
- [algorithm selection guide](10-how-to-choose-algorithm/algorithm-selection-guide.md)ï¼ˆ[ä¸­æ–‡](10-how-to-choose-algorithm/algorithm-selection-guide-zh.md)ï¼‰

## 11-pattern-library
- [core patterns](11-pattern-library/core-patterns.md)ï¼ˆ[ä¸­æ–‡](11-pattern-library/core-patterns-zh.md)ï¼‰

## 12-recursion-backtracking
- [backtracking template](12-recursion-backtracking/backtracking-template.md)ï¼ˆ[ä¸­æ–‡](12-recursion-backtracking/backtracking-template-zh.md)ï¼‰
- [recursion basics](12-recursion-backtracking/recursion-basics.md)ï¼ˆ[ä¸­æ–‡](12-recursion-backtracking/recursion-basics-zh.md)ï¼‰

## 13-heap
- [heap / priority queue](13-heap/heap-priority-queue.md)
