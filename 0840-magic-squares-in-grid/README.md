# **LeetCode 840 – Magic Squares In Grid**

**Difficulty:** Medium  
**Tags:** Array, Matrix, Brute Force  
**Link:** [https://leetcode.com/problems/magic-squares-in-grid/](https://leetcode.com/problems/magic-squares-in-grid/)

---

## **Problem Summary**

A **3 × 3 magic square** is a grid that satisfies:

* Contains **distinct numbers from 1 to 9**
* Each row, each column, and **both diagonals** have the same sum

You are given a matrix `grid` of size `row × col` where values may range from `0` to `15`.

Return the **number of 3 × 3 subgrids** inside `grid` that are magic squares.

---

## **Key Insight**

* A magic square can **only be 3 × 3** and use numbers `1–9`.
* Therefore, the problem reduces to:

  * Enumerating all possible 3 × 3 subgrids
  * Checking whether each one satisfies magic square properties
* Strong mathematical constraints allow **early pruning**.

---

## **Important Observations**

1. All numbers must be **unique** and in range `1–9`
2. In a valid 3 × 3 magic square using numbers `1–9`,
   the **center must always be `5`**
3. All row sums, column sums, and diagonal sums must be equal

These observations significantly reduce unnecessary checks.

---

## **Approach**

1. Enumerate every possible 3 × 3 subgrid.
2. For each subgrid:

   * Check all values are in `[1, 9]` and distinct
   * Verify the center element is `5`
   * Compute the target sum using the first row
   * Check all rows, columns, and diagonals
3. Count how many subgrids pass all checks.

---

## **Example**

### Example 1

```
Input:
grid = [
  [4,3,8,4],
  [9,5,1,9],
  [2,7,6,2]
]

Output: 1
```

Explanation:

```
Only the left 3×3 subgrid is a valid magic square
```

---

### Example 2

```
Input:
grid = [[8]]

Output: 0
```

Explanation:

```
Grid is too small to contain a 3×3 subgrid
```

---

## **Why This Works**

* The grid size is small (`≤ 10 × 10`)
* Every check is constant time
* Strong constraints (distinct 1–9, center = 5) prune invalid cases early
* The brute-force approach is both simple and efficient here

---

## **Complexity**

| Aspect | Complexity   |
| ------ | ------------ |
| Time   | **O(R × C)** |
| Space  | **O(1)**     |

Where:

* `R = number of rows`
* `C = number of columns`

---

## **What I Learned**

* How mathematical properties simplify brute-force problems
* Why knowing **invariants** (like center = 5) is powerful
* Efficient subgrid validation techniques
* A clean example of “brute force with pruning”

---

### Notes

Why must the center be `5`?

* The sum of numbers `1–9` is `45`
* A 3 × 3 magic square has 3 rows → each row sums to `15`
* The center participates in **4 lines**, and only `5` satisfies all constraints

This property is unique to 3 × 3 magic squares using `1–9`.

---

## **One-Line Interview Summary**

> “Enumerate each 3×3 subgrid and validate it using the fixed properties of a 1–9 magic square, especially the center being 5.”
