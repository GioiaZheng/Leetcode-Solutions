# **LeetCode 756 – Pyramid Transition Matrix**

**Difficulty:** Medium  
**Tags:** DFS, Backtracking, Memoization, Hash Table  
**Link:** [https://leetcode.com/problems/pyramid-transition-matrix/](https://leetcode.com/problems/pyramid-transition-matrix/)

---

## **Problem Summary**

You are stacking blocks to form a pyramid.

* Each block has a color represented by a single letter.
* Each upper block is placed on top of **two adjacent blocks** below it.
* Only specific triangular patterns are allowed, given in `allowed`.

Each pattern is a string `"ABC"` meaning:

```
  C
 A B
```

You are given:

* A base string `bottom`
* A list of allowed patterns `allowed`

Return `true` if you can build the pyramid all the way to the top (one block), otherwise return `false`.

---

## **Key Insight**

* The pyramid is built **level by level**, from bottom to top.
* Each level is a string, and the next level is constructed from **adjacent pairs**.
* This is a classic **DFS + backtracking** problem.

**Critical detail**:
Without memoization, the same intermediate strings are recomputed many times, leading to **Time Limit Exceeded**.

---

## **Core Challenge**

Different construction paths may lead to the **same intermediate level**.

Example:

```
"ABBB"
```

If `"ABBB"` has already been proven **impossible** to build upwards,
there is **no need to recompute it again**.

This is why **memoization is essential**.

---

## **Approach**

### Step 1: Preprocessing

Convert `allowed` into a mapping:

```
(left, right) → list of possible top blocks
```

This allows O(1) lookup during DFS.

---

### Step 2: DFS with Backtracking

* Each DFS state is a string representing the current level.
* Try all possible ways to build the next level.
* If any path reaches length `1`, return `true`.

---

### Step 3: Memoization (Key Optimization)

* Use a dictionary:

  ```
  memo[level_string] = True / False
  ```
* If a level has been evaluated before, return the cached result immediately.

This avoids exponential recomputation and guarantees performance.

---

## **Example**

### Example 1

```
Input:
bottom = "BCD"
allowed = ["BCC","CDE","CEA","FFF"]

Output: true
```

Explanation:

```
BCD → CE → A
```

All triangular patterns used are allowed.

---

### Example 2

```
Input:
bottom = "AAAA"
allowed = ["AAB","AAC","BCD","BBE","DEF"]

Output: false
```

Explanation:

```
All possible constructions eventually fail before reaching the top.
```

---

## **Why This Works**

* DFS explores all valid constructions.
* Backtracking ensures all combinations are tried.
* Memoization prevents re-evaluating the same failed states.
* The number of unique states is small due to:

  * Small alphabet size (A–F)
  * Maximum length of 6

---

## **Complexity**

| Aspect | Complexity                               |
| ------ | ---------------------------------------- |
| Time   | **Exponential (pruned heavily by memo)** |
| Space  | **O(number of unique level strings)**    |

In practice, the memoized solution runs fast and passes all test cases.

---

## **What I Learned**

* DFS alone is not enough for problems with overlapping subproblems.
* Memoization is crucial when different paths lead to the same state.
* This problem is a textbook example of **DFS + memoization**.
* Always watch out for TLE when the input allows dense transitions.

---

###  Notes

Without memoization, this solution **will TLE** on dense `allowed` inputs.

This problem is often used to test:

* Whether you recognize overlapping subproblems
* Whether you know when to add memoization to DFS

---

## **One-Line Interview Summary**

> “Use DFS with backtracking to build the pyramid level by level, and memoize intermediate levels to avoid recomputation.”
