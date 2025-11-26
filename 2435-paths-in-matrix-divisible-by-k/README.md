# 2435. Paths in Matrix Whose Sum Is Divisible by K

**Difficulty:** Hard  
**Topics:** Dynamic Programming  
**LeetCode Link:** https://leetcode.com/problems/paths-in-matrix-whose-sum-is-divisible-by-k/

---

##  Problem Description

You are given an `m x n` integer matrix `grid` and an integer `k`.  
You start at position `(0, 0)` and want to reach `(m-1, n-1)` by moving **only down or right**.

Each path has a total sum of all visited cells.

### **Goal**
Return the **number of paths whose sum is divisible by k**.

Because the answer can be very large, return it modulo **10⁹ + 7**.

---

##  Examples

### Example 1
```

Input:
grid = [[5,2,4],[3,0,5],[0,7,2]],
k = 3

Output: 2

```

Two valid paths:
- `5 + 2 + 4 + 5 + 2 = 18` → 18 % 3 = 0  
- `5 + 3 + 0 + 5 + 2 = 15` → 15 % 3 = 0  

---

### Example 2
```

Input: grid = [[0,0]], k = 5
Output: 1

```

Only one path with sum `0`, and `0 % 5 = 0`.

---

### Example 3
```

Input: grid = [[7,3,4,9],[2,3,6,2],[2,3,7,0]], k = 1
Output: 10

```

Since every number is divisible by 1, **all paths are valid**.

---

##  Key Insight

The path sum can be very large, but we only care about:

```

sum % k (the remainder)

```

So instead of storing the full sum, we store only the remainder.

This gives us a **Dynamic Programming (DP)** approach with state:

```

dp[i][j][r] = number of paths to (i,j)
whose path-sum % k = r

```

---

##  DP Transition

From each cell `(i, j)` you can come from:
- Top: `(i-1, j)`
- Left: `(i, j-1)`

Let:

```

val = grid[i][j] % k
new_r = (r + val) % k

```

Then:

```

dp[i][j][new_r] += dp[i-1][j][r]
dp[i][j][new_r] += dp[i][j-1][r]

```

Take modulo 1e9+7.

---

##  Final Answer

```

dp[m-1][n-1][0]

```

Paths whose sum is divisible by k.

---

##  Complexity

```

Time:  O(m · n · k)
Space: O(m · n · k)

````
---
##  Summary

* Use DP with remainder states.
* State dimension: `(i, j, remainder)`
* Only need to track sum % k.
* Final answer is remainder 0 at bottom-right.

你想继续吗？
