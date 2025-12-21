# **LeetCode 955 – Delete Columns to Make Sorted II**

**Difficulty:** Medium
**Tags:** Array, String, Greedy
**Link:** [https://leetcode.com/problems/delete-columns-to-make-sorted-ii/](https://leetcode.com/problems/delete-columns-to-make-sorted-ii/)

---

## **Problem Summary**

You are given an array of strings `strs`, where all strings have the same length.

You may delete any number of **column indices**, and for each deleted column,
the character at that index is removed from **every string**.

After deletions, the array must satisfy:

```
strs[0] <= strs[1] <= strs[2] <= ... <= strs[n - 1]
```

Return the **minimum number of columns** that must be deleted to achieve this.

---

## **Key Insight**

* Columns are processed **from left to right**.
* Once the lexicographic order between two adjacent strings is **confirmed**,
  future columns **do not need to compare that pair anymore**.
* A column must be deleted **only if it breaks the order for any unresolved pair**.

The challenge is **tracking which adjacent pairs are already sorted**.

---

## **Approach**

1. Maintain an array `sorted_pairs` of size `n - 1`:

   * `sorted_pairs[i] = True` means `strs[i] < strs[i+1]` has already been confirmed.
2. Iterate through columns from left to right:

   * Check if the current column causes a violation for any unresolved pair.
   * If yes, delete this column.
   * Otherwise, use this column to mark newly sorted pairs.
3. Continue until all columns are processed.

---

## **Example**

### Example 1

```
Input: strs = ["ca","bb","ac"]
Output: 1
```

Explanation:

```
Delete column 0 → ["a","b","c"]
```

---

### Example 2

```
Input: strs = ["xc","yb","za"]
Output: 0
```

Explanation:

```
Already lexicographically sorted
```

---

### Example 3

```
Input: strs = ["zyx","wvu","tsr"]
Output: 3
```

Explanation:

```
Every column must be deleted
```

---

## **Why This Works**

* Lexicographic order is determined **left to right**.
* Once a pair is ordered, later characters cannot change that order.
* Greedy deletion ensures the minimum number of columns are removed.
* All comparisons are local and efficient.

---

## **Complexity**

| Aspect | Complexity   |
| ------ | ------------ |
| Time   | **O(n × m)** |
| Space  | **O(n)**     |

Where:

* `n` = number of strings
* `m` = length of each string

---

## **What I Learned**

* How to track partial ordering in lexicographic problems.
* Why greedy decisions work when processing from left to right.
* The importance of maintaining state between iterations.
* The difference between this problem and its simpler version (944).

---

###  Notes

This problem is part of a sequence:

* 944. Delete Columns to Make Sorted
* 955. Delete Columns to Make Sorted II
* 960. Delete Columns to Make Sorted III

Together, they form a great study set for **greedy string ordering**.
