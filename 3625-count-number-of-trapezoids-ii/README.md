# 3625. Count Number of Trapezoids II

**Difficulty:** Hard  
**Topics:** Geometry, Combinatorics, Hash Map  
**Link:** https://leetcode.com/problems/count-number-of-trapezoids-ii/

---

##  Problem Description

You are given a list of 2D points.  
A **trapezoid** is a convex quadrilateral having **at least one pair of parallel sides**.

Two line segments are parallel if and only if they have the **same slope**:

```

slope = (y2 - y1) / (x2 - x1)

```

Return the number of **unique** trapezoids that can be formed using **any four distinct points**.

---

##  Examples

### Example 1
```

Input: points = [[-3,2],[3,0],[2,3],[3,2],[2,-3]]
Output: 2

```

### Example 2
```

Input: points = [[0,0],[1,0],[0,1],[2,1]]
Output: 1

```

---

#  Key Insight

A valid trapezoid requires:

- Two line segments that are **parallel**
- Those two segments must **not share endpoints**
- Any two non-overlapping parallel segments automatically form a convex quadrilateral, guaranteed by the problem constraints

Therefore, the problem reduces to:

#  Count all pairs of **parallel** segments  
#  Exclude pairs that share endpoints  
#  Each remaining pair corresponds to one trapezoid

---

##  Mathematical Breakdown

### Step 1 — Enumerate all point pairs  
For each pair `(i, j)`:

1. Compute reduced slope `(dy/g, dx/g)`
2. Normalize sign so slopes are comparable
3. Group segments by slope

Example:

```

slope_groups[(dy, dx)] = list of segments with this slope

```

---

### Step 2 — For each slope group:

Suppose this slope has `k` segments.

### Total segment pairs:

```

total_pairs = C(k, 2)

```

### Invalid pairs (segments sharing endpoints):

For each point p:

```

deg[p] = number of segments connected to p
invalid_pairs += C(deg[p], 2)

```

### Valid trapezoids contributed by this slope =

```

valid = total_pairs - invalid_pairs

```

---

#  Complexity Analysis

- Maximum n = 500  
- Total point pairs = ~125k  
- Hashing and counting are efficient  

Overall complexity:

```

O(n^2)

````

Fully acceptable.

---

#  Summary

To count trapezoids:

1. Compute slope for every point pair
2. Group segments by slope
3. For each slope group:

   * Compute all possible segment pairs
   * Subtract pairs that share endpoints
4. Sum across all slopes

This transforms a geometry problem into a clean combinatorics one.
