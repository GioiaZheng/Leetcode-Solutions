# 451. Sort Characters By Frequency

**Difficulty:** Medium  
**Topics:** Hash Table, String, Sorting, Heap  
**Link:** https://leetcode.com/problems/sort-characters-by-frequency/

---

## Problem Description

You are given a string `s`.  
Your task is to **sort the characters** in decreasing order based on their frequency.

- Characters with higher frequency must appear earlier.
- If two characters have the same frequency, their relative order does not matter.
- Uppercase and lowercase letters are treated as different characters.

Return **any valid sorted string**.

---

## Examples

### Example 1
```

Input: s = "tree"
Output: "eert"

Explanation:
'e' appears twice, while 't' and 'r' appear once.
So any string starting with "ee" is valid.

```

### Example 2
```

Input: s = "cccaaa"
Output: "aaaccc"

Explanation:
Both 'c' and 'a' appear 3 times.
Any arrangement grouping same letters together is valid.

```

### Example 3
```

Input: s = "Aabb"
Output: "bbAa"

Explanation:
'A' and 'a' are counted separately.

```

---

## Key Insight

To sort characters by frequency:

1. Count the frequency of each character  
2. Sort characters by their frequency (highest first)  
3. Build the output string by repeating each character according to its count  

For example:

```

"tree" → {'t':1, 'r':1, 'e':2}

Sorted order: ['e', 't', 'r']

Result: "ee" + "t" + "r" = "eert"

```

---

## Algorithm

1. Use `Counter` to compute frequencies  
2. Sort characters by frequency using `sorted()` with a custom key  
3. Build the output string by multiplying each character by its count  

---

## Complexity

```

Time:   O(n log n)
Space:  O(n)

```

Where  
- `n` = length of the string

Optimized solutions exist (bucket sort, O(n)),  
but the sorting approach is clear, reliable, and commonly accepted.

---

## Summary

* Count each character's frequency  
* Sort by frequency in descending order  
* Concatenate repeated characters to form the final answer  

A clean and intuitive solution for frequency-based string sorting.
