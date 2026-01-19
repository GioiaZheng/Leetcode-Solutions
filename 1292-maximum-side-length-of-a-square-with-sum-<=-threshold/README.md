# **LeetCode 1292 – Maximum Side Length of a Square with Sum ≤ Threshold**

**Difficulty:** Medium  
**Tags:** Prefix Sum, Binary Search, Matrix  
**Link:** https://leetcode.com/problems/maximum-side-length-of-a-square-with-sum-less-than-or-equal-to-threshold/

---

## **Problem Summary**

You are given:
- An `m × n` matrix `mat`
- An integer `threshold`

Your task is to find the **maximum side length `k`** of a **square submatrix** such that:

```

sum of all elements in the k × k square ≤ threshold

```

If no such square exists, return `0`.

---

## **Key Insight**

This is a **2D prefix sum + binary search** problem.

Why?

- Checking the sum of a square can be done in **O(1)** using prefix sums
- The feasibility of a square of size `k` is **monotonic**:
  - If a square of size `k` is valid, then all smaller sizes are also valid
- This allows us to **binary search on the side length**

---

## **Prefix Sum Preparation**

We build a 2D prefix sum array `ps`:

```

ps[i][j] = sum of mat[0..i-1][0..j-1]

```

So the sum of a square with:
- top-left corner `(r, c)`
- side length `k`

is:

```

squareSum =
ps[r+k][c+k] - ps[r][c+k] - ps[r+k][c] + ps[r][c]

```

This computation is **O(1)**.

---

## **Approach**

### Step 1: Build 2D Prefix Sum
Precompute prefix sums for fast square sum queries.

---

### Step 2: Binary Search on Side Length

Search range:
```

left = 0
right = min(m, n)

```

For a candidate side length `mid`:
- Check all `mid × mid` squares
- If **any** square has sum ≤ threshold → `mid` is feasible

---

### Step 3: Return the Maximum Valid Length

If no square is valid, return `0`.

---

## **Example Walkthrough**

### Example 1
```

mat =
[
[1,1,3,2,4,3,2],
[1,1,3,2,4,3,2],
[1,1,3,2,4,3,2]
]
threshold = 4

````

- `1 × 1` squares → OK
- `2 × 2` square with sum = 4 → OK
- `3 × 3` squares → sum > 4 → NOT OK

✅ Answer = `2`

---

## **Why This Works**

* Prefix sums allow **constant-time square sum checks**
* Feasibility is monotonic → binary search applies
* Total operations remain within limits even for `300 × 300` matrices

---

## **Complexity Analysis**

Let `K = min(m, n)`.

| Aspect            | Complexity      |
| ----------------- | --------------- |
| Prefix sum build  | `O(mn)`         |
| Feasibility check | `O(mn)`         |
| Binary search     | `O(log K)`      |
| **Total Time**    | **O(mn log K)** |
| Space             | **O(mn)**       |

---

## **Common Pitfalls**

* ❌ Forgetting `+1` padding in prefix sum
* ❌ Off-by-one errors in square boundaries
* ❌ Trying brute force sum computation (`O(k²)`)
* ❌ Missing binary search optimization

---

## **What I Learned**

* 2D prefix sums are essential for matrix sum queries
* Binary search can be applied to **answer space**, not just arrays
* Monotonic properties simplify complex matrix problems
* Always precompute when repeated queries are needed

---

## **Related Problems**

* 221. Maximal Square
* 3047. Largest Area of Square Inside Two Rectangles
* 1895. Largest Magic Square

---

## **One-Line Interview Summary**

> “Use a 2D prefix sum to compute square sums in O(1) and binary search on the side length to find the largest square whose sum is within the threshold.”
