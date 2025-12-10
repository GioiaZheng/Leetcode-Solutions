# **LeetCode 28 – Find the Index of the First Occurrence in a String**

**Difficulty:** Easy  
**Tags:** String, Two Pointers, Pattern Matching  
**Link:** [https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/](https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/)

---

## **Problem Summary**

Given two strings `haystack` and `needle`, determine the index of the first occurrence of `needle` in `haystack`.

If `needle` does not occur in `haystack`, return `-1`.

This task is equivalent to substring searching, a fundamental string-processing operation.

---

## **Key Insight**

A match begins at position `i` in `haystack` if:

```
haystack[i : i + len(needle)] == needle
```

The simplest solution checks every possible starting index up to:

```
len(haystack) - len(needle)
```

While advanced algorithms such as KMP improve worst-case performance, a direct scan is typically sufficient.

---

## **Approach**

1. Let `m = len(haystack)` and `n = len(needle)`.
2. If `n > m`, return `-1` immediately.
3. Iterate through all valid starting positions `i` from `0` to `m - n`:

   * Compare the substring of length `n` starting at `i` with `needle`.
   * If they match, return `i`.
4. If no match is found, return `-1`.

This approach ensures correctness in linear-time substring scanning.

---

## **Example**

**Input**

```
haystack = "sadbutsad"
needle = "sad"
```

**Explanation**

* A match occurs at index `0`.
* The next match at index `6` is later, but we return the first occurrence.

**Output**

```
0
```

---

## **Why This Works**

A substring of length `n` can only begin at positions where there are enough characters remaining.
By checking each such position exactly once, we avoid unnecessary work.

Pattern matching reduces to comparing fixed-length slices, making the algorithm straightforward and efficient for typical inputs.

---

## **Complexity**

* **Time:** `O(m * n)` in the worst case
  (can be improved to `O(m + n)` with KMP, though not required)
* **Space:** `O(1)`

---

## **What I Learned**

* How basic substring searching works through sequential comparison.
* Why boundary checks (`m - n`) are essential for avoiding invalid indexing.
* How more advanced algorithms improve theoretical performance, even if not needed for this problem.
