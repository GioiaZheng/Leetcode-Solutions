# LeetCode 85 – Maximal Rectangle
**Difficulty:** Hard 
**Tags:** Dynamic Programming, Stack, Monotonic Stack 
**Link:** https://leetcode.com/problems/maximal-rectangle/

---

## Problem Summary
You are given a binary matrix filled with `'0'` and `'1'`.

Your task is to find the **largest rectangle containing only `1`s** and return its **area**.

The rectangle must be fully contained within the matrix and aligned with the grid.

---

## Key Insight
This problem is a **2D extension of the Largest Rectangle in Histogram problem**.

The main idea:

- Treat **each row** as the base of a histogram.
- For every column, maintain the **height of consecutive `1`s** ending at the current row.
- For each row’s histogram, compute the **largest rectangle area** using a **monotonic stack**.

Thus, we reduce a 2D problem into multiple efficient 1D problems.

---

## Approach
### Step 1: Build Heights Array

For each row:

- If `matrix[r][c] == '1'` → `height[c] += 1`
- Else → `height[c] = 0`

This builds a histogram of vertical consecutive `1`s.

---

### Step 2: Largest Rectangle in Histogram

For the `height` array:

1. Use a **monotonic increasing stack**
2. Iterate through bars:
 - While the current height is **smaller** than the stack top:
 - Pop and compute area
3. Append a sentinel `0` to flush remaining bars

This guarantees all possible rectangles are considered.

---

### Step 3: Track Maximum Area

Repeat for each row and keep the global maximum.

---

## Example
### Example 1

```

Input:
[
["1","0","1","0","0"],
["1","0","1","1","1"],
["1","1","1","1","1"],
["1","0","0","1","0"]
]

Output:
6

```

Explanation:

The largest rectangle of `1`s has area **6**.

---

## Why This Works
- Converts a complex 2D problem into multiple well-understood 1D problems
- Histogram representation captures vertical continuity
- Monotonic stack guarantees optimal area calculation in linear time
- Each cell is processed a constant number of times

---

## Complexity
Let:

- `R = number of rows`
- `C = number of columns`

| Aspect | Complexity |
|------|------------|
| Time | **O(R × C)** |
| Space | **O(C)** |

---

## What I Learned
- How to transform 2D matrix problems into histogram-based solutions
- Using monotonic stacks to compute maximal areas efficiently
- Reusing classic problems (Largest Rectangle in Histogram) as subroutines
- Designing solutions that scale to large grids

---

## Related Problems
- 84. Largest Rectangle in Histogram 
- 221. Maximal Square 
- 1504. Count Submatrices With All Ones 

---

## One-Line Interview Summary
> “Treat each row as a histogram of consecutive ones and apply the Largest Rectangle in Histogram algorithm using a monotonic stack.”

<!--
Sections below are the optional "study card" extension. The problem
carries `"study_card_status": "reviewed"` in metadata.json. See
CONTRIBUTING.md section "Optional Problem README Sections (Study Card)".
-->

---

## Brute-force baseline

Two naive options:

1. Enumerate every `(top, bottom, left, right)` quadruple and check whether the enclosed rectangle is filled with `'1'`. `O(R^3 \cdot C^3)` worst case --- `O(R^2 \cdot C^2)` corner pairs times `O(R \cdot C)` verification each.
2. For every pair of rows `(top, bottom)`, compress the column ranges to "is this column all `'1'` between row `top` and row `bottom`?", then find the widest all-true span. `O(R^2 \cdot C)`.

The histogram + monotonic stack approach above is `O(R \cdot C)` time, `O(C)` space --- one pass per row, each cell touched a constant number of times by the stack.

---

## Common mistakes

- Conflating **Maximal Rectangle** (LeetCode 85, 2D binary matrix, arbitrary rectangle) with **Maximal Square** (LeetCode 221, same input but rectangle must be square). They look identical but require different DPs.
- Comparing the input as `matrix[r][c] == 1` when the LeetCode signature uses **character matrix** (`'0'` / `'1'`). The `==` returns `False` silently, leading to "heights always zero" bugs that pass empty-matrix tests but fail on non-empty input.
- Forgetting the sentinel `0` at the end of the histogram. Without it, bars still in the stack after the inner loop are never popped, so the rectangles they bound never enter the maximum.
- Resetting `heights` between rows. Heights accumulate downward; they only reset to `0` on a `'0'` cell, not on a row boundary.
- Off-by-one on the popped-rectangle width: when popping the bar at index `j` with new stack top `k`, the width is `i - k - 1` (or `i` if the stack becomes empty), not `i - j`.

---

## Failure cases

1. **`matrix = [["0"]]`** --- a single zero cell. Expected `0`. Implementations that fail to handle "histogram is all zeros" cleanly (e.g. divide-by-zero or uninitialised return) trip here.
2. **`matrix = [["1","1"],["1","1"]]`** --- the full `2 \times 2` all-ones rectangle, expected `4`. Tests that heights accumulate downward correctly *and* that the inner histogram routine finds the full-width rectangle (sentinel-flush working).
3. **Canonical example** `matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]` --- expected `6`. Exercises the interaction between vertical accumulation (heights builds up the 3-tall column of ones at row 2) and horizontal stack popping (the rectangle spans columns 2--4 of row 2 with height 2, area 6).

---

## Interview follow-ups

- *"Warmup: solve LeetCode 84 (Largest Rectangle in Histogram) first."* The inner routine of LC 85 *is* LC 84 applied to each row's histogram. Solving LC 84 cleanly is effectively a prerequisite.
- *"What if the matrix is sparse?"* The `heights` array is already O(C); zeros reset to `0`, so vertical-extension stays cheap. Time stays `O(R \cdot C)` even on adversarial sparsity patterns.
- *"Maximal Square instead of Maximal Rectangle."* → LeetCode 221. Different DP: `dp[r][c] = min(dp[r-1][c], dp[r][c-1], dp[r-1][c-1]) + 1` when `matrix[r][c] == '1'`. No stack needed; simpler in code, less general (only squares).
- *"Can the space be reduced below O(C)?"* The heights array is the irreducible state; the monotonic stack is bounded by `C` worst case. `O(C)` is the floor without changing the algorithm class.

---

## Bilingual summary

**English.** Per-row histogram of vertical consecutive ones: `heights[c] += 1` on `'1'`, `heights[c] = 0` on `'0'`. For each row, run Largest Rectangle in Histogram on the running `heights` array (monotonic increasing stack with a sentinel-`0` flush), keep the global max. `O(R \cdot C)` time, `O(C)` space.

**中文。** 每一行维护"竖直方向连续 `1`"的直方图：遇 `'1'` 就 `heights[c] += 1`，遇 `'0'` 重置为 `0`。对每一行的 `heights` 数组跑"直方图最大矩形"（单调递增栈 + 末尾哨兵 `0` 清空），取全局最大。时间 `O(R \cdot C)`，空间 `O(C)`。
