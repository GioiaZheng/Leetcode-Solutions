# **LeetCode 10 – Regular Expression Matching**

**Difficulty:** Hard  
**Tags:** String, Dynamic Programming  
**Link:** [https://leetcode.com/problems/regular-expression-matching/](https://leetcode.com/problems/regular-expression-matching/)

---

## **Problem Summary**

You are given a string `s` and a pattern `p`.

Implement regular expression matching with support for:

* `.` → matches **any single character**
* `*` → matches **zero or more of the preceding element**

The matching must cover the **entire string** (not partial matching).

---

## **Key Insight**

* This problem cannot be solved greedily.
* The correct approach is **Dynamic Programming**.
* We define a DP table where each state represents whether a prefix of `s`
  matches a prefix of `p`.

The main challenge is handling `*`, which can represent:

* **zero occurrences**
* **one or more occurrences** of the preceding character

---

## **Approach**

Define:

```text
dp[i][j] = whether s[0:i] matches p[0:j]
```

Steps:

1. Initialize `dp[0][0] = True` (empty string matches empty pattern).
2. Pre-fill cases where patterns like `"a*"`, `"a*b*"` match an empty string.
3. Fill the DP table:

   * If current characters match (`.` or same letter):

     * inherit from `dp[i-1][j-1]`
   * If current pattern character is `'*'`:

     * Case 1: treat `*` as **zero occurrences**
     * Case 2: treat `*` as **one or more occurrences**
4. The final answer is `dp[len(s)][len(p)]`.

---

## **Example**

### Example 1

```
Input: s = "aa", p = "a"
Output: false
```

---

### Example 2

```
Input: s = "aa", p = "a*"
Output: true
```

---

### Example 3

```
Input: s = "ab", p = ".*"
Output: true
```

---

## **Why This Works**

* Each DP state represents a **complete and unambiguous subproblem**.
* `*` is handled by separating **zero occurrences** and **multiple occurrences**.
* The solution checks **all valid matching paths**, guaranteeing correctness.
* The DP table size is small due to tight constraints.

---

## **Complexity**

| Aspect | Complexity   |
| ------ | ------------ |
| Time   | **O(m × n)** |
| Space  | **O(m × n)** |

Where:

* `m = len(s)`
* `n = len(p)`

---

## **What I Learned**

* How to model regex matching as a DP problem.
* Why `*` must always refer to the **previous character**.
* How to systematically cover all matching cases without backtracking.
* A classic interview-level string DP pattern.

---

###  Notes

This is one of the most important **string dynamic programming** problems.
Understanding this solution makes it much easier to solve:

* Wildcard Matching
* Edit Distance
* Pattern Matching variants
