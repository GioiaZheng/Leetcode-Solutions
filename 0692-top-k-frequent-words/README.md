# 692. Top K Frequent Words

**Difficulty:** Medium  
**Topics:** Hash Table, String, Sorting, Heap  
**Link:** https://leetcode.com/problems/top-k-frequent-words/

---

## Problem Description

You are given an array of strings `words` and an integer `k`.  
Your task is to return the **k most frequent words**.

The result must be sorted:

1. **By frequency** (higher → lower)  
2. If two words have the same frequency, sort them in **lexicographical order** (alphabetically ascending)

---

## Examples

### Example 1
```

Input:
words = ["i","love","leetcode","i","love","coding"], k = 2

Output:
["i","love"]

Explanation:
Both "i" and "love" appear twice.
Between them, "i" comes first alphabetically.

```

### Example 2
```

Input:
words = ["the","day","is","sunny","the","the","the","sunny","is","is"], k = 4

Output:
["the","is","sunny","day"]

Explanation:
Frequencies:
the   → 4
is    → 3
sunny → 2
day   → 1

```

---

## Key Insight

We need a **custom sorting rule**:

- Higher frequency → earlier  
- If same frequency → lexicographically smaller word first  

Python’s `sorted()` allows a tuple as key:

```

key = lambda w: (-frequency[w], w)

```

Here:
- `-frequency[w]` sorts by highest frequency first  
- `w` sorts alphabetically for ties  

This gives exactly the required ordering.

---

## Algorithm

1. Count frequencies using `Counter`
2. Sort the unique words using the custom key:
```

(-freq[word], word)

```
3. Return the first `k` words from the sorted list

---

## Complexity

```

Time:  O(n log n)
Space: O(n)

```

`n` is the number of words.

---

## Summary

- Use `Counter` to count word frequency  
- Use a **compound sort key** to apply both rules  
- Slice the first `k` elements  
- Clean and reliable solution  
