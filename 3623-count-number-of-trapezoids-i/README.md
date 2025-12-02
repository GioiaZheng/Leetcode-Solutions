# 3623. Count Number of Trapezoids I

**Difficulty:** Medium  
**Topics:** Geometry, Combinatorics, Hash Map  
**Link:** https://leetcode.com/problems/count-number-of-trapezoids-i/

---

##  Problem Description

You are given a list of points on the 2D plane.  
A **horizontal trapezoid** is a convex quadrilateral with **at least one pair of parallel horizontal sides** (i.e., sides parallel to the x-axis).

Your task is to count how many **distinct horizontal trapezoids** can be formed using **any 4 distinct points** from the input.

Return the count modulo **10⁹ + 7**.

---

##  Examples

### Example 1

Input:
```

points = [[1,0],[2,0],[3,0],[2,2],[3,2]]

```

Output:
```

3

```

Explanation:  
There are three valid ways to select four points that form a trapezoid:

- Points on y=0: 3 points → C(3,2) = 3 ways  
- Points on y=2: 2 points → C(2,2) = 1 way  
- Total trapezoids = 3 × 1 = 3

---

### Example 2

Input:
```

points = [[0,0],[1,0],[0,1],[2,1]]

```

Output:
```

1

```

---

##  Key Insight

A quadrilateral is a **horizontal trapezoid** iff:

- It has **two points on one horizontal line** (same y-value)
- And two points on another **different** horizontal line

Thus:

###  Group points by their `y` coordinate  
Let frequency of each horizontal line be:

```

freq[y] = number of points with y = y_value

```

###  For each horizontal line y:
You can select 2 points in:

```

C(freq[y], 2) = freq[y] * (freq[y] - 1) / 2

```

###  For two different horizontal lines y₁, y₂:
Number of trapezoids formed is:

# **C(freq[y₁], 2) × C(freq[y₂], 2)**

Because the top two points and the bottom two points determine a trapezoid with horizontal bases.

---

##  Efficient Summation

After computing `pairs[y] = C(freq[y], 2)` for each horizontal level:

We need:

```

sum over y1 < y2 of (pairs[y1] * pairs[y2])

```

This can be computed in O(m) using accumulated prefix sum:

```

result += pairs[i] * sum(previous pairs)

```

---

##  Complexity

```

Time:  O(n) + O(unique_y)
Space: O(unique_y)

````

Works for n up to 100,000.

---

##  Summary

* Group points by their y-coordinate
* For each horizontal level, compute number of ways to pick 2 points
* Combine across different levels using pairwise multiplication
* Use prefix sum to avoid O(m²) time
* Return result modulo 10⁹ + 7

This transforms a geometry problem into a clean combinatorics problem.
