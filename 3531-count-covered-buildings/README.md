# **LeetCode 3531 — Count Covered Buildings**

**Difficulty:** Medium  
**Tags:** Hashing, Geometry, Grid, Prefix Min/Max  
**Link:** [https://leetcode.com/problems/count-covered-buildings/](https://leetcode.com/problems/count-covered-buildings/)

---

##  **Problem Summary**

You are given an `n × n` city grid and a list of building coordinates.
Each building is located at **unique** `(x, y)` coordinates.

A building `(x, y)` is considered **covered** if:

* There is at least one building **to the left** → `(x, y_left)` with `y_left < y`
* There is at least one building **to the right** → `(x, y_right)` with `y_right > y`
* There is at least one building **above** → `(x_up, y)` with `x_up < x`
* There is at least one building **below** → `(x_down, y)` with `x_down > x`

 Return **how many buildings are covered** in all four directions.

---

##  **Key Insight**

For a building `(x, y)` to be covered, we need:

###  Row constraints

In row `x`:

* A smaller `y` exists → left
* A larger `y` exists → right

###  Column constraints

In column `y`:

* A smaller `x` exists → above
* A larger `x` exists → below

This means:

> We only need the **minimum and maximum** values in each row and each column.

No sorting, no adjacency lists required.

---

##  Efficient Strategy (O(n))

Let:

* `row_min[x]` = smallest y in row x
* `row_max[x]` = largest y in row x
* `col_min[y]` = smallest x in column y
* `col_max[y]` = largest x in column y

For building `(x, y)`:

```
left   exists if row_min[x] < y
right  exists if row_max[x] > y
above  exists if col_min[y] < x
below  exists if col_max[y] > x
```

If all four are true → the building is covered.

---

##  **Example**

### Input

```
n = 3
buildings = [[1,2],[2,2],[3,2],[2,1],[2,3]]
```

### Output

```
1
```

The only covered building is `(2,2)`, because it has:

* left: `(2,1)`
* right: `(2,3)`
* above: `(1,2)`
* below: `(3,2)`

---

## ⏱ Complexity Analysis

| Operation                       | Complexity |
| ------------------------------- | ---------- |
| Scan to compute min/max         | O(n)       |
| Scan to count covered buildings | O(n)       |
| **Total**                       | **O(n)**   |
| Space                           | O(n)       |

Works within all constraints (`10⁵` buildings).

---

## What I Learned

* How to reduce directional adjacency checks to simple min/max comparisons.
* Why storing only row/column extrema (instead of full lists) is sufficient.
* How grid problems often simplify into 1D constraints on each axis.
* Efficient use of hash maps for sparse grid processing.
