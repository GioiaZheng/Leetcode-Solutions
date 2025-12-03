# 242. Valid Anagram

**Difficulty:** Easy  
**Topics:** Hash Table, Sorting, Counting  
**Link:** https://leetcode.com/problems/valid-anagram/

---

## Problem Description

Given two strings `s` and `t`, return `true` if `t` is an anagram of `s`, and `false` otherwise.

Two strings are anagrams when they contain the same characters in the same frequencies, possibly in different orders.

---

## Examples

### Example 1
```

Input: s = "anagram", t = "nagaram"
Output: true

```

### Example 2
```

Input: s = "rat", t = "car"
Output: false

```

---

## Key Insight

Two strings are anagrams if:

```

sorted(s) == sorted(t)

```

or

```

frequency_count(s) == frequency_count(t)

```

---

## Approaches

###  1. Sorting (Simple)
Sort both strings and compare.

- **Time:** O(n log n)
- **Space:** O(1)–O(n)
- Very easy to write and understand.

---

###  2. Counter (Optimal, Unicode-safe)
Use `collections.Counter` to count character frequencies.

- **Time:** O(n)
- **Space:** O(1) for fixed alphabet, O(n) for unicode
- Works for **any language**, including emojis and Chinese characters.

This is generally the preferred solution.

---

## Follow-Up: Unicode

If the characters are not limited to lowercase letters (e.g., `你好`, `🙂😂`), the Counter-based solution automatically handles them.

---

## Summary

- Sorting is simple and effective.
- Using a frequency counter is optimal and handles Unicode naturally.
