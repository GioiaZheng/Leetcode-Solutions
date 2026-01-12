# **LeetCode 1266 – Minimum Time Visiting All Points**

**Difficulty:** Easy  
**Tags:** Geometry, Greedy, Math  
**Link:** https://leetcode.com/problems/minimum-time-visiting-all-points/

---

## **Problem Summary**

You are given a list of points on a 2D plane, where  
`points[i] = [xi, yi]`.

You must **visit all points in the given order**, starting from the first point.

In **1 second**, you can:
- Move **vertically** by 1 unit  
- Move **horizontally** by 1 unit  
- Move **diagonally** (1 unit horizontally + 1 unit vertically)

Your task is to compute the **minimum total time** required to visit all points.

---

## **Key Insight**

The optimal way to move between two points is to:

> **Use as many diagonal moves as possible**, then finish with straight moves.

For two points  
`(x1, y1) → (x2, y2)`:

- Horizontal distance: `dx = |x2 - x1|`
- Vertical distance: `dy = |y2 - y1|`

Each diagonal move reduces **both `dx` and `dy` by 1**, so:

```

Minimum time = max(dx, dy)

```

This single formula fully captures the optimal movement.

---

## **Approach**

### Step 1: Traverse Consecutive Points

Since points must be visited **in order**, we only care about moving from:
```

points[i-1] → points[i]

```

---

### Step 2: Compute Time Between Two Points

For each consecutive pair:

1. Compute:
```

dx = |x2 - x1|
dy = |y2 - y1|

```
2. Add:
```

time += max(dx, dy)

```

This automatically accounts for:
- Diagonal moves (when both dx and dy > 0)
- Straight moves (when one axis remains)

---

### Step 3: Accumulate Total Time

Repeat for all consecutive point pairs and sum the results.

---

## **Example**

### Example 1

```

Input:
points = [[1,1],[3,4],[-1,0]]

Output:
7

```

**Explanation:**

- From (1,1) → (3,4):  
  `dx = 2`, `dy = 3` → time = `3`
- From (3,4) → (-1,0):  
  `dx = 4`, `dy = 4` → time = `4`

**Total time = 3 + 4 = 7**

---

## **Why This Works**

- Diagonal movement is always optimal when both x and y differ
- Any remaining distance must be covered with straight moves
- The formula `max(dx, dy)` exactly models this behavior
- No path simulation is needed — just math

---

## **Complexity**

Let `n` be the number of points.

| Aspect | Complexity |
|------|------------|
| Time | **O(n)** |
| Space | **O(1)** |

---

## **What I Learned**

- How diagonal movement simplifies grid distance problems
- Greedy strategies can often be reduced to simple formulas
- Chebyshev distance (`max(dx, dy)`) naturally arises in 8-direction movement
- Avoiding simulation leads to cleaner and faster solutions

---

## **Related Problems**

- 62. Unique Paths  
- 64. Minimum Path Sum  
- 675. Cut Off Trees for Golf Event  

---

## **One-Line Interview Summary**

> “The minimum time between two points equals `max(|dx|, |dy|)` because diagonal moves reduce both coordinates simultaneously.”
