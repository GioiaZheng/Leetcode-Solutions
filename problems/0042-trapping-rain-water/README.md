# LeetCode 42 – Trapping Rain Water
**Difficulty:** Hard
**Tags:** Array, Two Pointers, Dynamic Programming, Stack
**Link:** [https://leetcode.com/problems/trapping-rain-water/](https://leetcode.com/problems/trapping-rain-water/)

---

## Problem

Given `n` non-negative integers representing an elevation map where the width of each bar is `1`, compute how much water can be trapped after raining.

The terrain is `height[i]` at column `i`; water fills any "valley" between higher walls on the left and the right. Return the total trapped water.

---

## Key Insight

The water above column `i` is bounded by the **shorter** of:

- the maximum height seen anywhere to the left of `i` (the left wall), and
- the maximum height seen anywhere to the right of `i` (the right wall).

If `min(left_max[i], right_max[i]) <= height[i]`, no water can sit on column `i`. Otherwise, the amount is `min(left_max[i], right_max[i]) - height[i]`.

Computing both prefix-max arrays takes `O(n)` time and `O(n)` space. A two-pointer pass shrinks the space to `O(1)` by only tracking the running max on whichever side is currently lower — that side's water level is already determined.

---

## Approach

Two pointers `left = 0` and `right = n - 1`, plus running `left_max`, `right_max`, and a `total` accumulator.

At each step:

1. Look at which side has the **lower** height. That side bounds the water level for its column, because the opposite wall is at least as tall as the current running max on that side.
2. Update the running max for that side, OR if today's height is below it, add the difference to `total`.
3. Move that pointer inward.

Stop when `left >= right`.

---

## Complexity

| Aspect | Complexity |
| ------ | ---------- |
| Time   | **O(n)**   |
| Space  | **O(1)**   |

The dynamic-programming variant with explicit `left_max[]` / `right_max[]` arrays is `O(n)` time, `O(n)` space — easier to explain but uses more memory.

---

## Edge Cases

- `height` is empty or has fewer than 3 elements: no water can be trapped, return `0`.
- Strictly increasing or strictly decreasing heights: also `0`, because one of the two walls is missing.
- Plateaus (`[3, 0, 0, 3]`): trapped = `2 * 3 = 6`; the algorithm handles equal walls correctly because the "which side is lower" branch falls through to the else branch on equality.

---

## Code

The canonical implementation is in [`solution.py`](solution.py). The two-pointer variant is the recommended one for interviews — it requires explaining the bounding-wall invariant but uses constant extra memory.

<!--
Sections below are the optional "study card" extension. The problem
carries `"study_card_status": "reviewed"` in metadata.json. See
CONTRIBUTING.md section "Optional Problem README Sections (Study Card)".
-->

---

## Brute-force baseline

For each column `i`, scan left to find `max(height[0..i])`, then scan right to find `max(height[i..n-1])`, and add `max(0, min(left_max, right_max) - height[i])` to the total.

- **Time:** `O(n^2)` — two linear scans per column.
- **Space:** `O(1)`.

The DP variant precomputes both prefix arrays once, dropping to `O(n)` time and `O(n)` space. The two-pointer variant further drops space to `O(1)`.

---

## Common mistakes

- Forgetting the bounding invariant and trying to move the **taller** pointer inward. Symmetrically wrong to LeetCode 11 (Container With Most Water) — but here moving the taller side cannot constrain the water level at the smaller side, so the algorithm under-counts water.
- Updating `left_max` / `right_max` **before** computing the contribution, which double-counts the wall itself as if it could trap water above its own top.
- Using `min(height) - height[i]` as the contribution instead of `min(left_max, right_max) - height[i]`. The global minimum height is irrelevant; only the local bounding walls matter.
- Edge-casing `n < 3` after the loop instead of before. The loop body is safe on empty input, but readers expect the trivial-case short-circuit at the top.

---

## Failure cases

1. **`height = [3, 0, 0, 3]`** — plateau bottom with equal walls. Naive "move whichever side is lower" needs to handle `height[left] == height[right]` deterministically (either branch is fine, but the code must pick one). Trapped = `6`.
2. **`height = [4, 2, 0, 3, 2, 5]`** — non-monotonic with a deeper valley between asymmetric walls. The right wall (5) dominates, but the left wall (4) is what bounds the leftmost columns. Trapped = `9`. A brute-force "rolling window of size 3" approach misses the long-range bounding effect entirely.

---

## Interview follow-ups

- *"Solve it in `O(1)` space."* — the two-pointer solution above. Explain the bounding-wall invariant: whichever side is shorter, its water level is fully determined regardless of what comes from the taller side.
- *"What if the input is a 2D elevation map?"* → LeetCode 407 (Trapping Rain Water II). The 1D two-pointer trick does not generalise; the canonical solution is a min-heap over the boundary cells, sweeping inward.
- *"Stack-based solution?"* — monotonic decreasing stack of heights; when a taller bar arrives, pop and add the bounded rectangular slice. Same `O(n)` time, `O(n)` space, but trickier to get right under interview pressure.
- *"What if heights can be negative?"* — the problem assumes `height[i] >= 0`. Negative heights model a depressed terrain below the baseline; the algorithm still works if "trapped water" is redefined to include the negative region, but the formulation changes.

---

## Bilingual summary

**English.** Two pointers from both ends; whichever side has the lower current height bounds the water level for that column, because the opposite wall is already at least as tall as `max` on the lower side. Maintain running `left_max` / `right_max`, add `running_max - height[i]` when `height[i]` is below the running max, otherwise update the running max. `O(n)` time, `O(1)` space.

**中文。** 左右双指针；当前高度较低的一侧决定其列的水位，因为对面墙至少和"较低一侧已见最大值"一样高。维护 `left_max` / `right_max`，当 `height[i]` 低于该侧 running max 时累加差值，否则更新 running max。时间 `O(n)`，空间 `O(1)`。
