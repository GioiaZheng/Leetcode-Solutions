# **LeetCode 14 – Longest Common Prefix**

**Difficulty:** Easy  
**Tags:** String  
**Link:** [https://leetcode.com/problems/longest-common-prefix/](https://leetcode.com/problems/longest-common-prefix/)

---

## **Problem Summary**

You are given an array of strings `strs`.

Your task is to find the **longest common prefix** shared by all strings in the array.

* If there is no common prefix, return an empty string `""`.

---

## **Key Insight**

* The common prefix must be a prefix of **every** string.
* If we start with the **entire first string** as a candidate prefix,
  we can gradually shrink it until it matches all other strings.
* Once the prefix becomes empty, no common prefix exists.

---

## **Approach**

1. If the input array is empty, return `""`.
2. Initialize `prefix` as the first string in the array.
3. For each remaining string:

   * While the current string does **not start with `prefix`**:

     * Remove the last character from `prefix`
     * If `prefix` becomes empty, return `""`
4. After all strings are processed, return `prefix`.

This is known as the **horizontal scanning** approach.

---

## **Example**

### Example 1

```
Input: strs = ["flower","flow","flight"]
Output: "fl"
```

Explanation:

```
"flower" → "flow" → common prefix = "flo"
"flo" does not match "flight"
Shrink to "fl" → matches all
```

---

### Example 2

```
Input: strs = ["dog","racecar","car"]
Output: ""
```

Explanation:

```
No prefix is common to all strings
```

---

## **Why This Works**

* Any common prefix must be a prefix of the first string.
* Shrinking the prefix guarantees correctness.
* Early termination avoids unnecessary comparisons.
* Simple logic with no extra data structures.

---

## **Complexity**

Let:

* `n` = number of strings
* `m` = length of the shortest string

| Aspect | Complexity   |
| ------ | ------------ |
| Time   | **O(n · m)** |
| Space  | **O(1)**     |

---

## **What I Learned**

* A clean way to solve prefix problems using string operations.
* How greedy shrinking leads to a correct solution.
* A foundational string problem frequently asked in interviews.
* The importance of early termination in simple algorithms.

---

### Notes

Other valid approaches include:

* Vertical scanning
* Sorting the array and comparing first & last strings

However, horizontal scanning is the **clearest and most intuitive**.

---

## **One-Line Interview Summary**

> “Start with the first string as the prefix and shrink it until all strings share it.”
