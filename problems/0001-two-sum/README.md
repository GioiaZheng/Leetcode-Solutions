# LeetCode 1 – Two Sum
**Difficulty:** Easy 
**Tags:** Array, Hash Table 
**Link:** [https://leetcode.com/problems/two-sum/](https://leetcode.com/problems/two-sum/)

---

## Problem Summary
Given an integer array `nums` and an integer `target`, return **indices** of the two numbers such that their sum equals `target`.

Constraints:

* You must use **two different elements**.
* Each input has **exactly one solution**.
* The answer may be returned in any order.

---

## Key Insight
The key relationship is:

$$
\text{num}_i + \text{num}_j = \text{target}
$$

Which implies:

$$
\text{num}_j = \text{target} - \text{num}_i
$$

So for each number, we check if its **complement** already appeared earlier.

A hash map lets us check this in **O(1)** time.

---

## Approach
1. Create a hash map (`seen`) that stores:

 ```
 number → index
 ```
2. Loop through the array:

 * Compute complement: `target - num`
 * If complement exists in the map → solution found
 * Otherwise, record current number and continue
3. Return the pair of indices.

Because the problem guarantees **exactly one solution**, we do not need extra checks.

---

## Example
### Example 1

```
nums = [2,7,11,15], target = 9
```

Explanation:

* At index 0: 2 → complement = 7 (not seen yet)
* At index 1: 7 → complement = 2 (seen at index 0)

Result:

```
[0, 1]
```

---

### Example 2

```
nums = [3,2,4], target = 6
Output: [1,2]
```

### Example 3

```
nums = [3,3], target = 6
Output: [0,1]
```

---

## Why This Works
* A hash map allows **O(1)** lookup for the complement.
* Each element is processed exactly once → **O(n)** time.
* This avoids the slow brute-force approach (**O(n²)**).

This is the classic optimal solution for Two Sum.

---

## Complexity
| Aspect | Complexity |
| ------ | ------------------------------------------- |
| Time | **O(n)** |
| Space | **O(n)** (hash map storing visited numbers) |

---

## What I Learned
* How hashing helps reduce a quadratic problem to linear time.
* The concept of computing a **complement** for target sum problems.
* Why storing value → index is enough to retrieve the correct pair.

<!--
Sections below are the optional "study card" extension. The problem
carries `"study_card_status": "reviewed"` in metadata.json. See
CONTRIBUTING.md section "Optional Problem README Sections (Study Card)".
-->

---

## Brute-force baseline

Two nested loops over all index pairs `(i, j)` with `j > i`, checking `nums[i] + nums[j] == target`.

- **Time:** `O(n^2)` — `n(n-1)/2` pair checks in the worst case.
- **Space:** `O(1)` — only loop counters.

The hash-map solution above trades `O(n)` extra space for `O(n)` time.

---

## Common mistakes

- Returning the **values** `[nums[i], nums[j]]` instead of the **indices** `[i, j]`. The problem asks for indices.
- Seeding the map with the current element **before** the lookup. With `target = 2 * nums[i]` (e.g. `[3, 3]`), inserting `nums[i]` first would return `[i, i]`, which the problem forbids ("two different elements").
- Sorting the array as a preprocessing step. Sorting destroys the original indices, which are the required answer.

---

## Failure cases

1. **`nums = [3, 3]`, `target = 6`** — a "store first, look up later" variant returns `[0, 0]` (same index twice). The canonical solution avoids this by checking the complement against the map **before** inserting the current element.
2. **`nums = [3, 2, 4]`, `target = 6`** — a two-pointer approach borrowed from "Two Sum II (sorted)" requires sorting, which destroys the original indices. Hashing is the only `O(n)` option on the unsorted variant.

---

## Interview follow-ups

- *"What if the array is sorted?"* — switch to two pointers from both ends: `O(n)` time, `O(1)` space.
- *"What if there are multiple valid pairs?"* — collect all pairs instead of returning early; watch for duplicate index pairs when values repeat.
- *"Generalise to k-sum."* — sort, then recursively reduce to (k-1)-sum, or fix two pointers per recursion level: `O(n^{k-1})` worst case.
- *"What if the array does not fit in memory?"* — stream the input twice (first pass builds a hash sketch, second pass finds complements), or shard by hash of value and process shards independently.

---

## Bilingual summary

**English.** Single-pass hash map keyed by value → first-seen index. For each element, check whether `target - value` is already in the map; the first complement hit returns both indices. `O(n)` time, `O(n)` space.

**中文。** 一次遍历的哈希表，键是数值、值是首次出现的索引。对每个元素检查 `target − 当前值` 是否已在表中；命中即返回这对索引。时间 `O(n)`，空间 `O(n)`。
