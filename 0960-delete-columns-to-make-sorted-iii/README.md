# **LeetCode 960 – Delete Columns to Make Sorted III**

**Difficulty:** Hard  
**Tags:** Array, String, Dynamic Programming  
**Link:** [https://leetcode.com/problems/delete-columns-to-make-sorted-iii/](https://leetcode.com/problems/delete-columns-to-make-sorted-iii/)

---

## **Problem Summary**

You are given an array of strings `strs`, where all strings have the same length.

You may delete any number of **column indices**, and for each deleted column,
the character at that index is removed from **every string**.

After deletions, **each individual string (row)** must be in **lexicographic order**, meaning:

```
strs[i][0] <= strs[i][1] <= ... <= strs[i][len-1]
```

⚠️ Note:

* The rows **do not need to be ordered relative to each other**
* Only **each row itself** must be non-decreasing

Return the **minimum number of columns** that must be deleted.

---

## **Key Insight**

* This is **not** a greedy column-deletion problem like 944 or 955.
* We want to **keep a subsequence of columns** such that:

  * For every row, characters are non-decreasing across those columns.
* This becomes a **Longest Non-Decreasing Subsequence (LNDS)** problem across columns,
  **simultaneously for all rows**.

So instead of minimizing deletions, we maximize the number of columns we keep.

---

## **Reformulation**

Let:

* `m` = number of columns

If we find the **maximum number of columns to keep** (`max_keep`),
then:

```
minimum deletions = m - max_keep
```

---

## **Approach (Dynamic Programming)**

Define:

```
dp[j] = length of the longest valid column subsequence ending at column j
```

Transition:

For every pair of columns `i < j`:

* Column `j` can follow column `i` **if and only if**
  for **all rows k**:

```
strs[k][i] <= strs[k][j]
```

If valid:

```
dp[j] = max(dp[j], dp[i] + 1)
```

Initialize:

```
dp[j] = 1   (each column alone is valid)
```

Answer:

```
min deletions = m - max(dp)
```

---

## **Example**

### Example 1

```
Input: strs = ["babca","bbazb"]
Output: 3
```

Explanation:

```
Keep columns [2, 3] → ["bc", "az"]
Delete columns [0, 1, 4]
```

---

### Example 2

```
Input: strs = ["edcba"]
Output: 4
```

Explanation:

```
Only one column can be kept to keep the row sorted
```

---

### Example 3

```
Input: strs = ["ghi","def","abc"]
Output: 0
```

Explanation:

```
All rows already sorted → no deletions needed
```

---

## **Why This Works**

* Each column is treated as a state in DP.
* Valid transitions ensure **all rows remain sorted**.
* This is a classic **LIS-style DP** generalized across multiple strings.
* The solution explores all valid column subsequences.

---

## **Complexity**

| Aspect | Complexity    |
| ------ | ------------- |
| Time   | **O(m² × n)** |
| Space  | **O(m)**      |

Where:

* `n` = number of strings (rows)
* `m` = number of columns

Given constraints (`n, m ≤ 100`), this is feasible.

---

## **What I Learned**

* How LIS-style DP can be generalized to multidimensional constraints.
* Why greedy fails for this version of the problem.
* How to convert a “minimum deletions” problem into a “maximum keep” problem.
* The conceptual progression from 944 → 955 → 960.

---

###  Notes

These three problems form a **perfect learning progression**:

* **944**: simple greedy check
* **955**: greedy + state tracking
* **960**: full dynamic programming (Hard)
