# 28. Find the Index of the First Occurrence in a String

**Difficulty:** Easy  
**Topics:** String, Two Pointers, Pattern Matching  
**Link:** https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/

---

##  Problem Description

Given two strings `haystack` and `needle`, return the **index of the first occurrence** of `needle` in `haystack`.  
If `needle` is **not found**, return `-1`.

You must search for `needle` as a **continuous substring**.

---

##  Examples

### Example 1
```

Input: haystack = "sadbutsad", needle = "sad"
Output: 0
Explanation:
"sad" appears at indexes 0 and 6.
The first occurrence is at index 0.

```

### Example 2
```

Input: haystack = "leetcode", needle = "leeto"
Output: -1
Explanation:
"leeto" does not appear in "leetcode".

```

---

##  Key Idea

We want to find the first index `i` such that:

```

haystack[i : i + len(needle)] == needle

````

There are multiple possible approaches:

1. **Use Python's built-in `.find()`**  
2. **Manual substring matching using a sliding window**  
3. (Optional for advanced) **KMP algorithm**

For this problem, solutions 1 and 2 are fully acceptable.

---

##  Approach 1 — Using `.find()` (Python Built-in)

### Concept
- Python provides a highly optimized method: `string.find(substring)`
- Returns the index of the first match, or -1 if not found

### Time complexity
- Worst case: O(m * n), but CPython has optimizations

---

##  Approach 2 — Sliding Window / Two Pointers

### Concept

For every possible start position `i`, compare substring of length `len(needle)`.

Check:

```
haystack[i : i + n] == needle
```

If equal → return i.

### Time Complexity

* O((m - n + 1) * n)
* Works well since constraints are small.

---

## ✔ Summary

| Method         | Description                  | Time             | Space |
| -------------- | ---------------------------- | ---------------- | ----- |
| `.find()`      | Fastest & simplest           | O(m·n) optimized | O(1)  |
| Sliding Window | Manual, easy to understand   | O((m-n+1)·n)     | O(1)  |
| KMP (optional) | Best theoretical performance | O(m+n)           | O(n)  |

For LeetCode 28, **both provided solutions are fully sufficient and accepted**.

---

##  Repository Files

```
28-find-the-index-of-the-first-occurrence-in-a-string/
│── README.md
│── solution1.py   # Built-in .find()
└── solution2.py   # Sliding window manual match
```


