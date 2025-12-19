# **LeetCode Solutions Repository**

Curated, well-documented **Python 3** solutions for a growing set of LeetCode problems. Each folder contains a clear explanation (`README.md`) and an implementation (`solution.py`) so this repo can serve as a reusable algorithm notebook.

---

## **Repository Layout**
- `####-problem-name/` — individual problems with an explanation and `solution.py`.
- `0000-notes/` — consolidated reference notes (moved from the old `notes/` path).

---

## **Notes**
- **How to Think**
  - [`how-to-read-problems.md`](0000-notes/00-how-to-think/how-to-read-problems.md) — reading and re-framing prompts effectively.
  - [`how-to-choose-algorithms.md`](0000-notes/00-how-to-think/how-to-choose-algorithms.md) — picking solution strategies quickly.
  - [`common-mistakes.md`](0000-notes/00-how-to-think/common-mistakes.md) — pitfalls to avoid during implementation.
- **Arrays**
  - [`array-basics.md`](0000-notes/01-array/array-basics.md) — traversal patterns and in-place tips.
- **Hash Table**
  - [`hashing-basics.md`](0000-notes/02-hash-table/hashing-basics.md) — core hashing concepts.
  - [`frequency-count.md`](0000-notes/02-hash-table/frequency-count.md) — counting patterns with dictionaries.
  - [`bucket-technique.md`](0000-notes/02-hash-table/bucket-technique.md) — bucket-based optimization tricks.
- **Two Pointers**
  - [`two-pointers-basics.md`](0000-notes/03-two-pointers/two-pointers-basics.md) — classic pointer patterns.
- **Sliding Window**
  - [`sliding-window-fixed.md`](0000-notes/04-sliding-window/sliding-window-fixed.md) — fixed-size templates.
  - [`sliding-window-variable.md`](0000-notes/04-sliding-window/sliding-window-variable.md) — variable-size templates.
- **Binary Search**
  - [`binary-search-on-array.md`](0000-notes/05-binary-search/binary-search-on-array.md) — array boundary search.
  - [`binary-search-on-answer.md`](0000-notes/05-binary-search/binary-search-on-answer.md) — search on monotonic answers.
- **Prefix Sum**
  - [`prefix-sum.md`](0000-notes/06-prefix-sum/prefix-sum.md) — prefix-sum patterns.
  - [`difference-array.md`](0000-notes/06-prefix-sum/difference-array.md) — range update trick.
- **Greedy**
  - [`greedy-thinking.md`](0000-notes/07-greedy/greedy-thinking.md) — greedy decision making.
  - [`interval-greedy.md`](0000-notes/07-greedy/interval-greedy.md) — interval scheduling patterns.
- **Dynamic Programming**
  - [`dp-introduction.md`](0000-notes/08-dynamic-programming/dp-introduction.md) — getting started with DP.

---

## **Problem Catalog**
A topic-focused index of all solutions currently in the repository.

| ID | Problem | Topics |
| --- | --- | --- |
| 0001 | [Two Sum](0001-two-sum/) | Array, Hash Table |
| 0002 | [Add Two Numbers](0002-add-two-numbers/) | Linked List, Math |
| 0003 | [Longest Substring Without Repeating Characters](0003-longest-substring-without-repeating-characters/) | Sliding Window, Hash Map, Two Pointers |
| 0004 | [Median of Two Sorted Arrays](0004-median-of-two-sorted-arrays/) | Binary Search, Divide and Conquer, Partitioning |
| 0005 | [Longest Palindromic Substring](0005-longest-palindromic-substring/) | String, Two Pointers, Expand Around Center |
| 0006 | [Zigzag Conversion](0006-zigzag-conversion/) | String, Simulation |
| 0007 | [Reverse Integer](0007-reverse-integer/) | Math |
| 0008 | [String to Integer (atoi)](0008-string-to-integer-atoi/) | String, Parsing |
| 0009 | [Palindrome Number](0009-palindrome-number/) | Math |
| 0010 | [Regular Expression Matching](0010-regular-expression-matching/) | String, Dynamic Programming |
| 0011 | [Container With Most Water](0011-container-with-most-water/) | Array, Two Pointers |
| 0026 | [Remove Duplicates from Sorted Array](0026-remove-duplicates-from-sorted-array/) | Array, Two Pointers |
| 0027 | [Remove Element](0027-remove-element/) | Array, Two Pointers |
| 0028 | [Find the Index of the First Occurrence in a String](0028-find-the-index-of-the-first-occurrence-in-a-string/) | String, Two Pointers, Pattern Matching |
| 0049 | [Group Anagrams](0049-group-anagrams/) | Array, Hash Table, String |
| 0121 | [Best Time to Buy and Sell Stock](0121-best-time-to-buy-and-shell-stock/) | Array, Greedy |
| 0164 | [Maximum Gap](0164-maximum-gap/) | Bucket Sort, Pigeonhole Principle, Sorting |
| 0220 | [Contains Duplicate III](0220-contains-duplicate-iii/) | Sliding Window, Bucket Sort, Hash Map |
| 0242 | [Valid Anagram](0242-valid-anagram/) | Hash Table, String, Sorting |
| 0347 | [Top K Frequent Elements](0347-top-k-frequent-elements/) | Array, Hash Table, Heap, Sorting |
| 0451 | [Sort Characters by Frequency](0451-sort-characters-by-frequency/) | Hash Table, String, Sorting, Heap |
| 0692 | [Top K Frequent Words](0692-top-k-frequent-words/) | String, Hash Table, Heap, Sorting |
| 0912 | [Sort an Array](0912-sort-an-array/) | Sorting, Divide and Conquer |
| 1523 | [Count Odd Numbers in an Interval Range](1523-count-odd-numbers-in-an-interval-range/) | Math |
| 1925 | [Count Square Sum Triples](1925-count-square-sum-triples/) | Math, Number Theory |
| 2092 | [Find All People With Secret](2092-final-all-people-with-secret/) | Graph, BFS, Sorting |
| 2110 | [Number of Smooth Descent Periods of a Stock](2110-number-of-smooth-descent-periods-of-a-stock/) | Array, Sliding Window, Consecutive Segment Counting |
| 2141 | [Maximum Running Time of N Computers](2141-maximum-running-time-of-n-computers/) | Binary Search, Greedy, Math |
| 2147 | [Number of Ways to Divide a Long Corridor](2147-number-of-ways-to-divide-a-long-corridor/) | Greedy, Combinatorics, Counting |
| 2211 | [Count Collisions on a Road](2211-count-collisions-on-a-road/) | String, Simulation |
| 2273 | [Find Resultant Array After Removing Anagrams](2273-find-resultant-array-after-removing-anagrams/) | Array, String, Hashing |
| 2435 | [Paths in Matrix Whose Sum Is Divisible by K](2435-paths-in-matrix-divisible-by-k/) | Dynamic Programming, Matrix, Prefix Sum |
| 3381 | [Maximum Subarray Sum With Length Divisible by K](3381-maximum-subarray-sum-with-length-divisible-by-k/) | Array, Prefix Sum, Hash Map |
| 3432 | [Count Partitions with Even Sum Difference](3432-count-partitions-with-even-sum-difference/) | Prefix Sum, Math, Parity |
| 3433 | [Count Mentions Per User](3433-count-mentions-per-user/) | Simulation, Hashing, Timeline Processing |
| 3531 | [Count Covered Buildings](3531-count-convered-buildings/) | Hashing, Geometry, Grid, Prefix Min/Max |
| 3562 | [Maximum Profit from Trading Stocks with Discounts](3562-maximum-profit-from-trading-stocks-with-discounts/) | Tree DP, Knapsack, Dynamic Programming, DFS |
| 3573 | [Best Time to Buy and Sell Stock V](3573-best-time-to-buy-and-sell-stock-v/) | Dynamic Programming, Stock Trading, State Machine |
| 3577 | [Count the Number of Computer Unlocking Permutations](3577-count-the-number-of-computer-unlocking-permutations/) | Sorting, Feasibility Check, Combinatorics |
| 3578 | [Count Partitions With Max-Min Difference at Most K](3578-count-partitions-with-max-min-difference-at-most-k/) | Sliding Window, Monotonic Queue, Dynamic Programming, Prefix Sum |
| 3583 | [Count Special Triplets](3583-count-special-triplets/) | Hash Map, Prefix/Suffix Frequency, Combinatorics |
| 3606 | [Coupon Code Validator](3606-coupon-code-validator/) | String Validation, Sorting, Simulation |
| 3623 | [Count Number of Trapezoids I](3623-count-number-of-trapezoids-i/) | Array, Geometry, Combinatorics |
| 3625 | [Count Number of Trapezoids II](3625-count-number-of-trapezoids-ii/) | Array, Geometry, Combinatorics |
| 3652 | [Best Time to Buy and Sell Stock using Strategy](3652-best-time-to-buy-and-sell-stock-using-strategy/) | Prefix Sum, Sliding Window, Greedy |

---

## **How to Use**
- Open any problem folder to read the explanation and run `solution.py` locally.
- Keep an eye on `0000-notes/` for reusable templates and pattern summaries as they are added.
