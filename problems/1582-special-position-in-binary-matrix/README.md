# **LeetCode 1582 – Special Positions in a Binary Matrix**

**Difficulty:** Easy  
**Tags:** Array, Matrix  
**Link:** [https://leetcode.com/problems/special-positions-in-a-binary-matrix/](https://leetcode.com/problems/special-positions-in-a-binary-matrix/)

---

## **Problem Summary**

You are given an `m x n` binary matrix `mat`.

A position `(i, j)` is called **special** if:

* `mat[i][j] == 1`
* All other elements in **row `i`** are `0`
* All other elements in **column `j`** are `0`

Return the **number of special positions** in the matrix.

---

## **Key Insight**

For a cell `(i, j)` to be **special**, it must be the **only `1` in both its row and its column**.

Therefore:

* The **sum of row `i`** must be `1`
* The **sum of column `j`** must be `1`

If both conditions hold and `mat[i][j] == 1`, then `(i, j)` is a special position.

---

## **Why This Approach Works**

Instead of checking the entire row and column every time we find a `1`, we can **precompute**:

* The number of `1`s in each **row**
* The number of `1`s in each **column**

Then we simply check whether:

```
row_sum[i] == 1 and col_sum[j] == 1
```

This avoids repeated scans and keeps the solution efficient.

---

## **Algorithm**

1. Compute the number of `1`s in each row.
2. Compute the number of `1`s in each column.
3. Traverse the matrix again.
4. For each cell `(i, j)`:

   * If `mat[i][j] == 1`
   * And `row_sum[i] == 1`
   * And `col_sum[j] == 1`
   * Then increment the answer.
5. Return the total count.

---

## **Example**

### Example 1

```
Input:
mat = [
 [1,0,0],
 [0,0,1],
 [1,0,0]
]

Row sums: [1,1,1]
Col sums: [2,0,1]

Only (1,2) has:
mat[i][j] == 1
row_sum[i] == 1
col_sum[j] == 1

Output: 1
```

---

### Example 2

```
Input:
mat = [
 [1,0,0],
 [0,1,0],
 [0,0,1]
]

Row sums: [1,1,1]
Col sums: [1,1,1]

All diagonal elements satisfy the condition.

Output: 3
```

---

## **Complexity Analysis**

| Aspect | Complexity   |
| ------ | ------------ |
| Time   | **O(m × n)** |
| Space  | **O(m + n)** |

* We scan the matrix twice.
* Extra space stores row and column counts.

---

## **Common Mistakes**

* Checking the entire row and column for every `1` (inefficient).
* Forgetting that the cell itself should not be counted twice.
* Not precomputing row/column sums.

Using row and column counts simplifies the check.

---

## **One-Line Interview Summary**

> “Count the number of `1`s in each row and column, then a cell is special if it is `1` and both its row and column contain exactly one `1`.”
