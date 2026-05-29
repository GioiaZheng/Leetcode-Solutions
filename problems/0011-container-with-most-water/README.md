# LeetCode 11 – Container With Most Water
**Difficulty:** Medium 
**Tags:** Array, Two Pointers 
**Link:** [https://leetcode.com/problems/container-with-most-water/](https://leetcode.com/problems/container-with-most-water/)

---

## Problem Summary
You are given an integer array `height` of length `n`.

Each element represents a vertical line drawn at position `i` with height `height[i]`.

Choose **two lines** such that together with the x-axis they form a container,
and the container holds the **maximum amount of water**.

You may **not slant** the container.

---

## Key Insight
* The amount of water is determined by:

 * the **distance** between two lines
 * the **shorter height** of the two lines
* The area formula is:

```text
area = (right - left) * min(height[left], height[right])
```

* To maximize the area efficiently:

 * Start with the **widest container**
 * Gradually shrink the width
 * Always move the pointer at the **shorter line**

---

## Approach
1. Initialize two pointers:

 * `left` at the beginning
 * `right` at the end
2. Compute the area formed by the two pointers.
3. Update the maximum area.
4. Move the pointer with the **smaller height** inward.
5. Repeat until the pointers meet.

This guarantees that all potential maximum containers are considered.

---

## Example
### Example 1

```
Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
```

---

### Example 2

```
Input: height = [1,1]
Output: 1
```

---

## Why This Works
* The width decreases at every step.
* The height is always limited by the **shorter line**.
* Moving the taller line cannot increase the area.
* Moving the shorter line is the **only chance** to find a larger container.

This leads to a linear-time solution.

---

## Complexity
| Aspect | Complexity |
| ------ | ---------- |
| Time | **O(n)** |
| Space | **O(1)** |

---

## What I Learned
* How to optimize brute-force problems using two pointers.
* Why greedy pointer movement works in this scenario.
* A classic example of reducing `O(n²)` to `O(n)`.
* One of the most important two-pointer patterns in interviews.

---

### Notes

This problem is a cornerstone of the **Two Pointers** technique.

Understanding it helps with problems such as:

* Trapping Rain Water
* 3Sum
* Sliding Window optimizations

<!--
Sections below are the optional "study card" extension. The problem
carries `"study_card_status": "reviewed"` in metadata.json. See
CONTRIBUTING.md section "Optional Problem README Sections (Study Card)".
-->

---

## Brute-force baseline

Two nested loops over every pair `(i, j)` with `i < j`; compute `min(h[i], h[j]) * (j - i)` and track the maximum.

- **Time:** `O(n^2)`.
- **Space:** `O(1)`.

The two-pointer solution above collapses this to `O(n)` by abandoning the shorter line as soon as it's the bottleneck.

---

## Common mistakes

- Moving the pointer at the **taller** line instead of the shorter. The shorter line caps the height; moving the taller one shrinks the width without ever raising the bound.
- Computing area as `max(h[i], h[j]) * (j - i)`. Water is bounded by the **shorter** line — anything above it spills over.
- Mixing in trapping-rain-water logic. LC 11 measures one container between two chosen lines; LC 42 sums trapped water across many gaps. Different abstractions.
- Forgetting to advance on ties (`h[i] == h[j]`). Either pointer may move; both give the same theoretical improvement bound. But one of them **must** move or the loop hangs.

---

## Failure cases

1. **`heights = [1, 8, 6, 2, 5, 4, 8, 3, 7]`** — the canonical example; the answer is `49` (`heights[1] = 8` with `heights[8] = 7`, width `7`). A buggy "always move the left pointer" misses this pair.
2. **`heights = [1, 2, 4, 3]`** — answer is `4` (`heights[1] = 2` to `heights[3] = 3`, width `2`, height `2`). A buggy "move whichever index is smaller" rule fails here because the index test does not correspond to the height test.

---

## Interview follow-ups

- *"Why is moving the shorter pointer safe?"* — Any container that still includes the shorter line at its current position has strictly smaller width and is still capped by the same shorter line. Its area cannot exceed the current one; we lose nothing by discarding it.
- *"Generalise to Trapping Rain Water."* → LeetCode 42. Different abstraction (sum across all gaps), but the same two-pointer skeleton works: track `left_max` and `right_max`, accumulate `min(left_max, right_max) - h[i]`.
- *"What if all heights are zero?"* — every pair has area `0`. The two-pointer still converges in `O(n)`; the answer is `0`.
- *"Find every `(i, j)` achieving the maximum area, not just the value."* — the two-pointer is destructive (it abandons pairs as it moves). Run a full `O(n^2)` scan, or augment the two-pointer to remember tied maxima at each step.

---

## Bilingual summary

**English.** Two pointers at both ends. At each step the area is `min(h[L], h[R]) * (R - L)`; move the pointer at the **shorter** line inward, since moving the taller cannot improve the area (width shrinks, height still bounded by the shorter). Loop until `L` meets `R`. `O(n)` time, `O(1)` space.

**中文。** 左右双指针。每步面积 = `min(h[L], h[R]) * (R - L)`；每次把较矮一端的指针向内移——较高端往里挪，宽度变小、高度仍被较矮端卡死，不可能更大。直到 `L` 与 `R` 相遇为止。时间 `O(n)`，空间 `O(1)`。
