# **LeetCode 2435 – Paths in Matrix Whose Sum Is Divisible by K**

**Difficulty:** Hard  
**Tags:** Dynamic Programming, Matrix, Prefix Sum  
**Link:** [https://leetcode.com/problems/paths-in-matrix-whose-sum-is-divisible-by-k/](https://leetcode.com/problems/paths-in-matrix-whose-sum-is-divisible-by-k/)

---

## **Problem Summary**

You are given a 2D grid of integers and an integer `k`.
A path starts at the top-left cell and ends at the bottom-right cell.
At each step, you may only move **right** or **down**.

The task is to count how many such paths have a total sum divisible by `k`.
The answer must be returned modulo (10^9 + 7).

---

## **Key Insight**

The classic path-counting DP only tracks the number of ways to reach each cell.
In this problem, the sum along the path affects the validity of the result, so each DP state must also track the **sum modulo `k`**.

If two partial paths arrive at the same cell with the same remainder modulo `k`, they are fundamentally equivalent for extension.

Thus, the DP state becomes:

```
dp[r][c][rem] = number of ways to reach (r, c) with sum % k = rem
```

This additional dimension allows us to distinguish paths based on their modular sum up to that point.

---

## **Approach**

1. Initialize a 3D DP array where:

   * `r` and `c` index the cell,
   * `rem` is the sum modulo `k`.

2. At the start cell `(0, 0)`:

   * Let `initial = grid[0][0] % k`
   * Set `dp[0][0][initial] = 1`

3. For each cell `(r, c)`:

   * Paths may come from above `(r-1, c)` or from the left `(r, c-1)`.

4. When transitioning:

   * Suppose a previous remainder is `prev_rem`.
   * After adding `grid[r][c]`, the new remainder is:

     ```
     new_rem = (prev_rem + grid[r][c]) % k
     ```
   * Add all ways leading to `prev_rem` into `dp[r][c][new_rem]`.

5. At the final cell `(m-1, n-1)`:

   * The answer is `dp[m-1][n-1][0]`,
     since we want paths where sum % k = 0.

---

## **Example**

**Input**

```
grid = [[5, 2, 4],
        [3, 0, 5],
        [0, 7, 2]]
k = 3
```

**Explanation**
Every path's sum is computed, and the number of valid paths where the total is divisible by `3` is counted.

**Output**

```
2
```

---

## **Why This Works**

The key observation is that modulo arithmetic preserves path validity:

* Whether a path’s sum is divisible by `k` depends only on its final sum modulo `k`.
* The modulo space is limited to `0 ... k-1`, so dynamic programming over these states is efficient.
* Movement is restricted (right or down), which ensures an acyclic grid and allows DP traversal.

By tracking remainder states, we avoid recomputing sums and ensure each partial path is represented uniquely.

---

## **Complexity**

* **Time:** `O(m * n * k)`
* **Space:** `O(m * n * k)`
  Can be optimized to `O(n * k)` with rolling arrays.

---

## **What I Learned**

* How to extend classical path DP with modular arithmetic.
* Why modulo-based DP states are powerful when sum divisibility is required.
* How dimensional DP grows with problem constraints and how to manage complexity.

**0026 – Remove Duplicates from Sorted Array**
