# **LeetCode 85 – Maximal Rectangle**

**Difficulty:** Hard  
**Tags:** Dynamic Programming, Stack, Monotonic Stack  
**Link:** https://leetcode.com/problems/maximal-rectangle/

---

## **Problem Summary**

You are given a binary matrix filled with `'0'` and `'1'`.

Your task is to find the **largest rectangle containing only `1`s** and return its **area**.

The rectangle must be fully contained within the matrix and aligned with the grid.

---

## **Key Insight**

This problem is a **2D extension of the Largest Rectangle in Histogram problem**.

The main idea:

- Treat **each row** as the base of a histogram.
- For every column, maintain the **height of consecutive `1`s** ending at the current row.
- For each row’s histogram, compute the **largest rectangle area** using a **monotonic stack**.

Thus, we reduce a 2D problem into multiple efficient 1D problems.

---

## **Approach**

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

## **Example**

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

## **Why This Works**

- Converts a complex 2D problem into multiple well-understood 1D problems
- Histogram representation captures vertical continuity
- Monotonic stack guarantees optimal area calculation in linear time
- Each cell is processed a constant number of times

---

## **Complexity**

Let:

- `R = number of rows`
- `C = number of columns`

| Aspect | Complexity |
|------|------------|
| Time | **O(R × C)** |
| Space | **O(C)** |

---

## **What I Learned**

- How to transform 2D matrix problems into histogram-based solutions
- Using monotonic stacks to compute maximal areas efficiently
- Reusing classic problems (Largest Rectangle in Histogram) as subroutines
- Designing solutions that scale to large grids

---

## **Related Problems**

- 84. Largest Rectangle in Histogram  
- 221. Maximal Square  
- 1504. Count Submatrices With All Ones  

---

## **One-Line Interview Summary**

> “Treat each row as a histogram of consecutive ones and apply the Largest Rectangle in Histogram algorithm using a monotonic stack.”
