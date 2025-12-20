# **LeetCode 944 – Delete Columns to Make Sorted**

**Difficulty:** Easy
**Tags:** Array, String
**Link:** [https://leetcode.com/problems/delete-columns-to-make-sorted/](https://leetcode.com/problems/delete-columns-to-make-sorted/)

---

## **Problem Summary**

You are given an array of strings `strs`, where:

* All strings have the **same length**
* Each string represents **one row** in a grid

You want to delete the columns that are **not sorted lexicographically** from top to bottom.

A column is sorted if:

```
strs[0][col] ≤ strs[1][col] ≤ ... ≤ strs[n-1][col]
```

Return the **number of columns** that need to be deleted.

---

## **Key Insight**

The problem is **column-oriented**, not row-oriented.

For each column, we only need to check whether the characters:

```
strs[0][c], strs[1][c], ..., strs[n-1][c]
```

are in **non-decreasing order**.

If at any point:

$$
strs[r][c] < strs[r-1][c]
$$

then the column is **not sorted** and must be deleted.

---

## **Approach**

1. Let:

   * `rows = len(strs)`
   * `cols = len(strs[0])`
2. For each column `c` from `0` to `cols - 1`:

   * Compare characters row by row
   * If any character is smaller than the one above it:

     * Mark this column as invalid
     * Increase the deletion count
     * Stop checking this column
3. Return the total number of invalid columns.

---

## **Example**

### Example 1

```
strs = ["cba", "daf", "ghi"]
```

Grid:

```
c b a
d a f
g h i
```

Explanation:

* Column 0: `c → d → g` ✅ sorted
* Column 1: `b → a` ❌ not sorted
* Column 2: `a → f → i` ✅ sorted

Result:

```
1
```

---

### Example 2

```
strs = ["a", "b"]
Output: 0
```

Only one column, already sorted.

---

### Example 3

```
strs = ["zyx", "wvu", "tsr"]
Output: 3
```

All columns are decreasing → all must be deleted.

---

## **Why This Works**

* Each column is **independent** of the others.
* We only need a **single top-down scan** per column.
* Early stopping (`break`) avoids unnecessary checks.
* No sorting or extra data structures are required.

This leads to a clean and efficient solution.

---

## **Complexity**

| Aspect | Complexity   |
| ------ | ------------ |
| Time   | **O(n × m)** |
| Space  | **O(1)**     |

Where:

* `n` = number of strings
* `m` = length of each string

---

## **Code**

```python
class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        rows = len(strs)
        cols = len(strs[0])
        deletions = 0

        for c in range(cols):
            for r in range(1, rows):
                if strs[r][c] < strs[r - 1][c]:
                    deletions += 1
                    break

        return deletions
```

---

## **What I Learned**

* How to shift perspective from **rows to columns**
* How early termination simplifies logic and improves efficiency
* That many string problems reduce to simple **ordering checks**
* This pattern appears frequently in **grid + string** problems
