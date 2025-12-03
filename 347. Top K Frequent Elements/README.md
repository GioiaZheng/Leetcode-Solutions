# 347. Top K Frequent Elements

**Difficulty:** Medium  
**Topics:** Array, Hash Map, Heap, Bucket Sort  
**Link:** https://leetcode.com/problems/top-k-frequent-elements/

---

##  Problem Description

Given an integer array `nums` and an integer `k`, return the **k most frequent elements**.  
The answer may be returned **in any order**.

---

##  Examples

### Example 1
```

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]

```

### Example 2
```

Input: nums = [1], k = 1
Output: [1]

```

### Example 3
```

Input: nums = [1,2,1,2,1,2,3,1,3,2], k = 2
Output: [1,2]

```

---

##  Constraints
- \( 1 \le \text{nums.length} \le 10^5 \)
- \( -10^4 \le \text{nums}[i] \le 10^4 \)
- \( 1 \le k \le \) number of unique elements
- The answer is guaranteed to be unique.

---

##  Follow-Up

Your algorithm must be **better than** `O(n log n)`, where `n` is the length of `nums`.

---

##  Key Insight

We need the `k` elements with the highest frequency.

Three valid approaches:

---

##  **Solution 1 — HashMap + Counter (Most Pythonic)**
Uses `collections.Counter`.

**Complexity:**  
- Time: `O(n log k)`  
- Space: `O(n)`

---

##  **Solution 2 — HashMap + Sorting**
Sort keys by frequency.

**Complexity:**  
- Time: `O(n log n)`  
- Space: `O(n)`

---

##  **Solution 3 — Bucket Sort (Best, O(n))**
Because frequency ranges from `1` to `n`, we can place numbers into buckets indexed by frequency.

**Complexity:**  
- Time: `O(n)`  
- Space: `O(n)`

This is the optimal solution required by the follow-up.

---

##  Summary

| Method | Time | Space | Notes |
|--------|--------|--------|----------------|
| Counter | O(n log k) | O(n) | Clean + fast |
| Sorting | O(n log n) | O(n) | Simple, accepted |
| Bucket Sort | O(n) | O(n) | Best solution |
