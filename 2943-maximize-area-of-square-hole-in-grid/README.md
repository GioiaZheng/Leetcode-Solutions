# **LeetCode 2943 – Maximize Area of Square Hole in Grid**

**Difficulty:** Medium  
**Tags:** Greedy, Geometry, Sorting  
**Link:** https://leetcode.com/problems/maximize-area-of-square-hole-in-grid/

---

## **Problem Summary**

You are given a rectangular grid formed by:

- `n + 2` **horizontal bars**
- `m + 2` **vertical bars**

These bars form **1 × 1 unit cells**.

Some bars can be removed:
- `hBars` → removable horizontal bars
- `vBars` → removable vertical bars

All other bars are fixed.

Your task is to **remove some (possibly none) of the removable bars** to create a **square-shaped hole** with the **maximum possible area**, and return that area.

---

## **Key Insight**

Removing bars allows adjacent unit cells to **merge**.

### Important Observation

- Removing **k consecutive horizontal bars** merges **k + 1 vertical cells**
- Removing **t consecutive vertical bars** merges **t + 1 horizontal cells**

Therefore, the **maximum square side length** is:

```

min(
longest_consecutive(hBars) + 1,
longest_consecutive(vBars) + 1
)

```

The **area** is simply the square of this side length.

---

## **Approach**

### Step 1: Find Longest Consecutive Sequence

For both `hBars` and `vBars`:
1. Sort the array
2. Scan to find the longest run of consecutive integers

This tells us the maximum number of bars we can remove in one continuous block.

---

### Step 2: Compute Maximum Square Area

```

side = min(max_h + 1, max_v + 1)
area = side × side

```

---

## **Example**

### Example 1

```

Input:
n = 2, m = 1
hBars = [2,3]
vBars = [2]

Output:
4

```

Explanation:
- Horizontal: removing bars `[2,3]` → height = `3`
- Vertical: removing bar `[2]` → width = `2`
- Largest square side = `min(3,2) = 2`
- Area = `2 × 2 = 4`

---

### Example 2

```

Input:
n = 1, m = 1
hBars = [2]
vBars = [2]

Output:
4

````

Removing one horizontal and one vertical bar creates a `2 × 2` square.

---

## **Why This Works**

* Only **consecutive bar removals** can enlarge a hole
* Horizontal and vertical expansions are independent
* The limiting dimension determines the largest possible square
* No grid simulation is required

---

## **Complexity Analysis**

Let `H = len(hBars)` and `V = len(vBars)`.

| Aspect | Complexity               |
| ------ | ------------------------ |
| Time   | **O(H log H + V log V)** |
| Space  | **O(1)**                 |

---

## **What I Learned**

* Grid problems often reduce to **interval analysis**
* Consecutive sequences can replace costly simulations
* Understanding how removals affect geometry is key
* Simple greedy logic can outperform complex DP

---

## **Related Problems**

* 221. Maximal Square
* 84. Largest Rectangle in Histogram
* 85. Maximal Rectangle

---

## **One-Line Interview Summary**

> “The largest square hole is formed by removing the longest consecutive horizontal and vertical bars; the side length is the minimum of those lengths plus one.”
