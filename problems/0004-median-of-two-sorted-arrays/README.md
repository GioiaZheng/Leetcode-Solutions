# LeetCode 4 – Median of Two Sorted Arrays
**Difficulty:** Hard 
**Tags:** Binary Search, Divide and Conquer, Partitioning 
**Link:** [https://leetcode.com/problems/median-of-two-sorted-arrays/](https://leetcode.com/problems/median-of-two-sorted-arrays/)

---

## Problem Summary
You are given two sorted arrays `nums1` and `nums2`, of sizes `m` and `n` respectively.
Your task is to compute the **median** of the two arrays when they are merged into one sorted array.

However, you must achieve this in:

```
O(log(m + n)) time complexity.
```

A direct merge or full sort would require `O(m + n)` or `O((m+n) log(m+n))`,
and therefore **cannot** be used.

---

## Key Insight
The classical merge approach is too slow because the arrays may include up to 2000 elements.
To meet the logarithmic time requirement, we need a strategy that eliminates half of the search space each step.

The key idea is to treat the problem as finding the correct **partition** of the two arrays such that:

```
All elements on the left side of the partition 
≤ 
All elements on the right side.
```

If we find such a partition, then:

* For odd total length:
 The median is the **minimum** of the right partition.
* For even total length:
 The median is the **average** of:

 * The **maximum** value from the left partition
 * The **minimum** value from the right partition

We apply **binary search** on the smaller array to find the correct partition position.

This reduces the search space at every step and gives the required `O(log(m+n))`.

---

## Approach
1. Always binary-search on the **shorter array** to simplify partitioning logic.
2. Let:

 ```
 total = m + n
 half = total // 2
 ```
3. Perform binary search on `nums1` for a partition index `i`.
4. Partition `nums2` accordingly:

 ```
 j = half - i
 ```
5. Extract the border values:

 ```
 nums1_left, nums1_right
 nums2_left, nums2_right
 ```

 Using `+inf` or `-inf` for out-of-bounds indices.
6. Check if the partition is valid:

 ```
 nums1_left <= nums2_right
 and 
 nums2_left <= nums1_right
 ```
7. If valid:

 * If total length is odd → return min(right values)
 * If even → return (max(left values) + min(right values)) / 2
8. Otherwise adjust binary search range:

 * If nums1_left > nums2_right → move left
 * Else → move right

This guarantees logarithmic time complexity.

---

## Example
**Input**

```
nums1 = [1, 2]
nums2 = [3, 4]
```

Merged array would be:

```
[1, 2, 3, 4]
```

Left partition and right partition:

```
Left: [1, 2]
Right: [3, 4]
```

Median:

```
(2 + 3) / 2 = 2.5
```

**Output**

```
2.5
```

---

## Why This Works
The key observation is:

### Median depends only on the boundary between the left half and the right half.

By searching for the correct boundary using binary search:

* We avoid merging arrays.
* We avoid full sorting.
* We eliminate half of the search space each iteration.
* We treat both arrays as contributing to a single combined sorted order.

The use of `±∞` for edge cases ensures clean comparisons without extra conditionals.

This is one of the most elegant applications of binary search in algorithm design.

---

## Complexity
| Metric | Value |
| --------- | ------------------- |
| **Time** | `O(log(min(m, n)))` |
| **Space** | `O(1)` |

---

## What I Learned
* How binary search can be applied to partition boundaries instead of numeric targets.
* Why median problems often reduce to balancing left and right partitions.
* How to use conceptual “virtual merge” instead of explicitly building arrays.
* The importance of always binary-searching the shorter array to avoid invalid partitions.
* How to represent out-of-bounds values with `±∞` to simplify logic.

---

## Solution Files
- `solution.py` is the recommended binary-search partition solution because it meets the required `O(log(min(m, n)))` time complexity.
- `approaches/solution_sorting.py` keeps the simpler sorting-based approach for comparison, but it does not meet the optimal time bound.

<!--
Sections below are the optional "study card" extension. The problem
carries `"study_card_status": "reviewed"` in metadata.json. See
CONTRIBUTING.md section "Optional Problem README Sections (Study Card)".
-->

---

## Brute-force baseline

Concatenate the two arrays, sort the result, return the middle element (or average of the two middle elements for even total length).

- **Time:** `O((m + n) \log(m + n))` --- dominated by the sort.
- **Space:** `O(m + n)` for the merged array.

A linear merge variant (two-pointer walk through both arrays, stop at index `(m + n) // 2`) tightens this to `O(m + n)` time / `O(1)` space. Both fail the problem's explicit `O(\log(m + n))` requirement.

---

## Common mistakes

- Binary-searching on the **larger** array instead of the smaller. The partition index `i` ranges over `[0, len(shorter)]` and `j = half - i` must stay valid. If you search the larger array, `j` can go negative on inputs where one array is much larger than the other.
- Using closed-interval binary search with the wrong loop guard. The canonical form is `lo = 0, hi = m` (NOT `m - 1`) because `i = m` is a valid partition (everything from `nums1` goes left).
- Computing the median **before** confirming the partition is valid. The four boundary comparisons `nums1_left <= nums2_right` AND `nums2_left <= nums1_right` must both hold; otherwise the partition needs adjustment.
- Using `nums[m]` (out-of-bounds) instead of `+inf` for the right boundary when `i == m`. The sentinel form (`float('inf')` / `float('-inf')`) cleans the boundary cases; explicit if-branches multiply by the number of corners (`i == 0`, `i == m`, `j == 0`, `j == n`).
- Off-by-one on `half`: it should be `(m + n + 1) // 2` (not `(m + n) // 2`) so the left side has the extra element when the total length is odd. With `(m + n) // 2`, the right side has the extra element, and the odd-length median formula becomes `min(right)` instead of `max(left)` --- both work, but the conventions must match.

---

## Failure cases

1. **`nums1 = [], nums2 = [1]`** --- one array empty. Naive partition logic that assumes both arrays contribute at least one element returns `None` or crashes. The binary search must accept `i = 0` cleanly via the `+inf` / `-inf` sentinels on the left/right boundaries.
2. **`nums1 = [1, 3], nums2 = [2]`** --- canonical odd-total example; expected median `2`. With `(m + n + 1) // 2 = 2`, the partition `i = 1` over `nums1` gives `j = 1` over `nums2`: left = `[1, 2]`, right = `[3]`. Median = `max(left) = 2`.
3. **`nums1 = [1, 2], nums2 = [3, 4]`** --- canonical even-total example; expected `2.5`. Partition `i = 2` over `nums1` (all of it goes left), `j = 0` over `nums2`. Left = `[1, 2]`, right = `[3, 4]`. Median = `(max(left) + min(right)) / 2 = (2 + 3) / 2 = 2.5`.
4. **`nums1 = [1, 2, 3, 4, 5], nums2 = [6, 7, 8, 9, 10]`** --- entirely disjoint, both arrays contribute. Partition `i = 2`, `j = 3`. Left = `[1, 2, 6, 7, 8]`, right = `[3, 4, 5, 9, 10]`. Median = `(8 + 3) / 2 = 5.5`. Tests the case where the algorithm must reach a partition where one array "uses up" more than half its elements.

---

## Interview follow-ups

- *"What if there are k sorted arrays instead of 2?"* --- LC 4 does not generalise cleanly to `k > 2`. The standard approach is a min-heap merge ($O((m_1 + ... + m_k) \log k)$) or a $k$-way binary search variant, but the elegant 2-array partition trick relies on `j = half - i` being a single derived index, which breaks for $k$ arrays.
- *"What if the arrays are not sorted?"* --- can no longer use binary search on partitions. Either sort first ($O((m + n) \log(m + n))$) or use the QuickSelect-style randomised median-finding algorithm ($O(m + n)$ average). LeetCode 4's $O(\log)$ bound exploits sortedness.
- *"Generalise to find the k-th smallest element across two sorted arrays."* --- same partition idea: target `half = k - 1` instead of `(m + n + 1) // 2`. Time stays $O(\log(\min(m, n)))$.
- *"What if elements can be duplicates across arrays?"* --- algorithm works unchanged; the four boundary comparisons `<=` (not `<`) handle equality cleanly.

---

## Bilingual summary

**English.** Binary search on the smaller array for the correct partition index `i`. The complementary index `j = (m + n + 1) // 2 - i` partitions the larger array. A valid partition satisfies `nums1[i-1] <= nums2[j]` AND `nums2[j-1] <= nums1[i]`; out-of-bounds slots use $\pm\infty$. Median is `max(left)` for odd total length, `(max(left) + min(right)) / 2` for even. Time `O(\log(\min(m, n)))`, space `O(1)`.

**中文。** 在较短的数组上二分搜索分割位置 `i`，互补位置 `j = (m + n + 1) // 2 - i` 自然给出较长数组的分割位置。有效分割要满足 `nums1[i-1] <= nums2[j]` 且 `nums2[j-1] <= nums1[i]`；越界位置用 $\pm\infty$ 哨兵填补。总长为奇数时中位数 = `max(left)`，偶数时 = `(max(left) + min(right)) / 2`。时间 `O(\log(\min(m, n)))`，空间 `O(1)`。
