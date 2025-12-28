# **LeetCode 1351 – Count Negative Numbers in a Sorted Matrix**

**Difficulty:** Easy  
**Tags:** Array, Matrix, Two Pointers  
**Link:** [https://leetcode.com/problems/count-negative-numbers-in-a-sorted-matrix/](https://leetcode.com/problems/count-negative-numbers-in-a-sorted-matrix/)

---

## **Problem Summary**

You are given an `m x n` matrix `grid` where:

* Each row is sorted in **non-increasing order** (left to right)
* Each column is sorted in **non-increasing order** (top to bottom)

Your task is to return the **number of negative numbers** in the matrix.

---

## **Key Insight**

* Because the matrix is sorted both row-wise and column-wise,
  we can count negative numbers **without checking every cell**.
* If a value is negative, then:

  * All values **to its right in the same row** are also negative.
* This allows us to skip large parts of the matrix efficiently.

---

## **Approach (O(m + n))**

1. Start from the **bottom-left corner** of the matrix.
2. If the current value is **negative**:

   * All elements to the right are also negative.
   * Add `n - col` to the count.
   * Move **up** to the previous row.
3. If the current value is **non-negative**:

   * Move **right** to the next column.
4. Continue until all rows or columns are processed.

This guarantees that each row and column is visited at most once.

---

## **Example**

### Example 1

```
Input:
grid = [
  [4, 3, 2, -1],
  [3, 2, 1, -1],
  [1, 1, -1, -2],
  [-1, -1, -2, -3]
]

Output: 8
```

---

### Example 2

```
Input:
grid = [[3,2],[1,0]]

Output: 0
```

---

## **Why This Works**

* The sorted structure ensures monotonic movement.
* No element is visited more than once.
* Large blocks of negative numbers are counted in a single step.
* This improves over the naive `O(m × n)` solution.

---

## **Complexity**

| Aspect | Complexity   |
| ------ | ------------ |
| Time   | **O(m + n)** |
| Space  | **O(1)**     |

Where:

* `m` = number of rows
* `n` = number of columns

---

## **What I Learned**

* How matrix sorting constraints enable efficient scanning.
* Why two-pointer traversal works on 2D monotonic structures.
* A classic example of reducing time complexity using problem structure.
* A high-frequency interview pattern for sorted matrices.

---

###  Notes

Alternative approach:

* Binary search each row to find the first negative number
  → Time complexity: **O(m log n)**

However, the two-pointer approach is strictly better here.
