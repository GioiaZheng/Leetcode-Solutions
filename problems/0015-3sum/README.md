# LeetCode 15 – 3Sum
**Difficulty:** Medium 
**Tags:** Array, Two Pointers, Sorting 
**Link:** [https://leetcode.com/problems/3sum/](https://leetcode.com/problems/3sum/)

---

## Problem Summary
You are given an integer array `nums`.

Your task is to find **all unique triplets** `[nums[i], nums[j], nums[k]]` such that:

* `i ≠ j`, `i ≠ k`, `j ≠ k`
* `nums[i] + nums[j] + nums[k] == 0`

The solution **must not contain duplicate triplets**.

The order of triplets and the order of numbers inside a triplet do **not** matter.

---

## Key Insight
* Sorting the array allows:

 * Efficient searching using the **two-pointer technique**
 * Easy handling of **duplicate values**
* Once sorted:

 * Fix one number
 * Reduce the problem to a **2Sum** search on the remaining array

This transforms a brute-force `O(n³)` problem into an `O(n²)` solution.

---

## Approach
1. **Sort** the array.
2. Iterate through the array with index `i`:

 * Skip duplicate values for `nums[i]`
3. For each `i`, use two pointers:

 * `left = i + 1`
 * `right = n - 1`
4. Compute the sum:

 * If sum == 0 → record the triplet
 * If sum < 0 → move `left` forward
 * If sum > 0 → move `right` backward
5. After finding a valid triplet:

 * Skip duplicates for both `left` and `right`

---

## Example
### Example 1

```
Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
```

Explanation:

Sorted array:

```
[-4, -1, -1, 0, 1, 2]
```

Valid triplets:

```
-1 + -1 + 2 = 0
-1 + 0 + 1 = 0
```

---

### Example 2

```
Input: nums = [0,1,1]
Output: []
```

---

### Example 3

```
Input: nums = [0,0,0]
Output: [[0,0,0]]
```

---

## Why This Works
* Sorting enables deterministic pointer movement.
* Two-pointer search efficiently finds pairs with a target sum.
* Skipping duplicates ensures:

 * Each triplet is unique
 * No redundant results
* Each valid combination is explored exactly once.

---

## Complexity
Let `n = len(nums)`.

| Aspect | Complexity |
| ------ | --------------------------- |
| Time | **O(n²)** |
| Space | **O(1)** (excluding output) |

---

## What I Learned
* How sorting simplifies multi-sum problems.
* Correct and careful handling of duplicates.
* Applying two-pointer techniques beyond 2Sum.
* A foundational pattern for many array problems.

---

### Notes

This problem is the foundation for many related problems:

* 16. 3Sum Closest
* 18. 4Sum
* 611. Valid Triangle Number

Mastering **3Sum** makes these much easier.

---

## One-Line Interview Summary
> “Sort the array, fix one element, then use two pointers to find pairs summing to the target while skipping duplicates.”

<!--
Sections below are the optional "AI card" extension. The problem
carries `"ai_card_status": "reviewed"` in metadata.json. See
CONTRIBUTING.md section "Optional Problem README Sections (AI Card)".
-->

---

## Brute-force baseline

Three nested loops over all triples `(i, j, k)`; check whether the sum is zero; deduplicate the result by sorting each triplet and inserting into a set.

- **Time:** `O(n^3)` for the loops, plus an `O(1)`-amortised set lookup per triplet.
- **Space:** `O(n)` for the dedupe set.

The sort + two-pointer solution above improves to `O(n^2)` time and `O(1)` extra space (excluding the output).

---

## Common mistakes

- Forgetting to sort first. Without sort, the two-pointer cannot make ordered progress, *and* the duplicate-skip logic breaks (it relies on equal values being adjacent).
- Skipping the outer-loop duplicate AFTER the inner search instead of before. The work has already been done; the dedup must be **at the top of the loop**: `if i > 0 and nums[i] == nums[i - 1]: continue`.
- Skipping duplicates only for `left` after a hit, not for `right`. Produces dup output like `[-1, -1, 2]` reported twice on inputs like `[-1, -1, -1, 2]`.
- Returning a `set` of tuples instead of `list[list[int]]`. The problem signature expects nested lists.
- Using `nums[i] > 0` as an early exit but comparing it before doing the dedup-skip — the optimisation is correct, but easy to slot in the wrong order and skip a legitimate `nums[i] == 0` start.

---

## Failure cases

1. **`nums = [0, 0, 0, 0]`** — expected `[[0, 0, 0]]` (single triplet, even though four zeros exist). Without proper dedup-skipping on `i`, returns `[[0, 0, 0], [0, 0, 0]]` (or worse).
2. **`nums = [-1, -1, 2, 2]`** — expected `[[-1, -1, 2]]`. Without skipping right-pointer duplicates after a hit, returns `[[-1, -1, 2], [-1, -1, 2]]`.
3. **`nums = [0, 1, 1]`** — only three elements summing to `2`, not `0`. Expected `[]`. Tests the "no triplets" path; bugs that always return the first attempt fail here.

---

## Interview follow-ups

- *"Generalise to k-sum."* — recursively reduce: `k-sum -> fix one element -> (k-1)-sum on the rest`; base case is 2-sum with two pointers. Time `O(n^(k-1))`.
- *"3Sum Closest."* (LeetCode 16) — same skeleton, but minimise `|sum - target|` instead of demanding exact equality. No dedup needed; track the best so far.
- *"What if duplicates ARE allowed in the output?"* — drop all three layers of dedup-skip; otherwise identical.
- *"Out-of-memory case."* — sort externally (merge-sort with disk-backed runs), then two-pointer with seekable reads. The `O(n^2)` random reads become the new bottleneck.

---

## Bilingual summary

**English.** Sort the array. For each outer index `i`, fix `nums[i]` and run two pointers `left = i + 1`, `right = n - 1` over the remainder, looking for pairs that sum to `-nums[i]`. Skip equal-value neighbours at every level (outer `i`, inner `left` after a hit, inner `right` after a hit) to deduplicate. `O(n^2)` time, `O(1)` extra space excluding the output.

**中文。** 先排序。外层固定 `nums[i]`，对剩余部分用 `left = i + 1`、`right = n - 1` 双指针，寻找和等于 `-nums[i]` 的二元组。在每一层（外层 `i`、`left` hit 之后、`right` hit 之后）都跳过相邻相等元素以去重。时间 `O(n^2)`，额外空间 `O(1)`（不含输出）。
