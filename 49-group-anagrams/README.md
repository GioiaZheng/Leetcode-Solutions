# 49. Group Anagrams

**Difficulty:** Medium  
**Topics:** Hash Table, String, Sorting  
**Link:** https://leetcode.com/problems/group-anagrams/

---

## Problem Description

You are given an array of strings `strs`.  
Your task is to **group all anagrams together**.

Two strings are anagrams if one can be rearranged to form the other.  
The output order does not matter.

---

## Examples

### Example 1
```

Input: strs = ["eat","tea","tan","ate","nat","bat"]

Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

```

---

### Example 2
```

Input: strs = [""]
Output: [[""]]

```

### Example 3
```

Input: strs = ["a"]
Output: [["a"]]

```

---

## Key Insight

Two strings are anagrams if:

```

sorted(s1) == sorted(s2)

```

So:

- Sort each string
- Use the sorted result as a **key**
- Store all strings with the same key in a dictionary

Example:

```

"eat" -> "aet"
"tea" -> "aet"
"ate" -> "aet"

```

Thus they belong to the same group.

---

## Algorithm

1. Create a dictionary `anagram_map`
2. For each string:
   - Sort it and use the result as a key
   - Append the original string to that key's list
3. Return all values of the dictionary

---

## Complexity

```

Time:   O(n * k log k)
Space:  O(n * k)

```

Where  
- `n` = number of strings  
- `k` = max length of a string  

---

## Summary

* Sorting provides a unique signature for each anagram group  
* Hash map groups strings efficiently  
* Clean and widely accepted solution  
