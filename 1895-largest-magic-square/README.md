# **LeetCode 1895 – Largest Magic Square**

**Difficulty:** Medium  
**Tags:** Prefix Sum, Matrix, Enumeration  
**Link:** https://leetcode.com/problems/largest-magic-square/

---

## **Problem Summary**

A **k × k magic square** is a square subgrid where:

- All **row sums** are equal  
- All **column sums** are equal  
- The **two diagonal sums** are equal  

> The values do **not** need to be distinct.  
> Every `1 × 1` grid is trivially a magic square.

Given an `m × n` integer grid, return the **largest possible side length `k`** of a magic square contained in the grid.

---

## **Key Insight**

The brute-force idea is simple:

- Enumerate all possible square sizes `k`
- For each position `(i, j)`, check whether the `k × k` subgrid is magic

However, **naively computing sums would be too slow**.

### Optimization Trick  
Use **prefix sums** to compute:

- Any row sum
- Any column sum
- Any diagonal sum  

in **O(1)** time.

This makes the brute-force approach efficient enough.

---

## **Prefix Sum Preparation**

We precompute:

### 1️⃣ Row prefix sums
```

rowSum[i][j] = sum of grid[i][0..j-1]

```

### 2️⃣ Column prefix sums
```

colSum[i][j] = sum of grid[0..i-1][j]

````

This allows:
- Row sum in `[j, j+k)` → `rowSum[i][j+k] - rowSum[i][j]`
- Column sum in `[i, i+k)` → `colSum[i+k][j] - colSum[i][j]`

---

## **Checking a k × k Magic Square**

For a square with top-left corner `(r, c)` and size `k`:

1. Compute the **target sum** using the first row
2. Check:
   - All `k` row sums
   - All `k` column sums
3. Check the two diagonals:
   - Main diagonal
   - Anti-diagonal

If all match → it's a magic square.

---

## **Approach**

### Step 1: Precompute prefix sums

- `rowSum`
- `colSum`

---

### Step 2: Enumerate square sizes

- Try sizes from **largest to smallest**
- First valid square → return immediately

This guarantees we return the **maximum k**.

---

### Step 3: Fallback

If no square larger than `1 × 1` is valid, return `1`.

---

## **Example**

### Example 1

```
Input:
[
 [7,1,4,5,6],
 [2,5,1,6,4],
 [1,5,4,3,2],
 [1,2,7,3,4]
]

Output: 3
```

Explanation:

* A `3 × 3` subgrid exists where all row, column, and diagonal sums equal `12`.

---

## **Why This Works**

* Prefix sums reduce sum checks from `O(k)` to `O(1)`
* Enumeration is feasible because `m, n ≤ 50`
* Checking largest sizes first avoids unnecessary work

---

## **Complexity Analysis**

Let `K = min(m, n)`.

| Aspect      | Complexity               |
| ----------- | ------------------------ |
| Prefix sums | `O(mn)`                  |
| Enumeration | `O(K × m × n)`           |
| Total       | **O(m × n × min(m, n))** |
| Space       | **O(mn)**                |

This fits comfortably within constraints.

---

## **What I Learned**

* Prefix sums are extremely powerful for matrix problems
* Checking constraints first (largest `k`) improves performance
* Geometry + prefix sums is a common interview pattern
* Always optimize sum queries before brute force

---

## **Related Problems**

* 840. Magic Squares In Grid
* 221. Maximal Square
* 3047. Largest Square Inside Two Rectangles

---

## **One-Line Interview Summary**

> “Precompute row and column prefix sums, then enumerate square sizes from largest to smallest and verify row, column, and diagonal sums in O(1) time.”
