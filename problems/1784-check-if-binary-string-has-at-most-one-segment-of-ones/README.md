# LeetCode 1784 – Check if Binary String Has at Most One Segment of Ones
**Difficulty:** Easy 
**Tags:** String, Greedy 
**Link:** [https://leetcode.com/problems/check-if-binary-string-has-at-most-one-segment-of-ones/](https://leetcode.com/problems/check-if-binary-string-has-at-most-one-segment-of-ones/)

---

## Problem Summary
You are given a binary string `s` **without leading zeros**.

Return `true` if the string contains **at most one contiguous segment of `1`s**. Otherwise, return `false`.

A contiguous segment means all the `1`s appear together without being separated by `0`s.

---

## Key Insight
Because the string **always starts with `1`**, the first segment of `1`s begins at the start of the string.

The only way to have **more than one segment of `1`s** is:

```
...1 0 ... 1
```

This means after encountering the **first `0`**, there should **never be another `1`**.

Equivalently:

> If the string contains the substring `"01"` followed later by a `1`, then there are multiple segments of ones.

A simpler observation:

> A valid string must look like: `111...1100...00`

---

## Why This Works
If `1`s form only one contiguous segment, the structure of the string must be:

```
[1...1][0...0]
```

Once the sequence of `1`s ends and a `0` appears, encountering another `1` later would create a **second segment of ones**, which violates the requirement.

Therefore, we simply check whether a `1` appears **after the first `0`**.

---

## Algorithm
1. Traverse the string from left to right
2. Track whether a `0` has appeared
3. If a `1` appears after a `0`, return `false`
4. If the traversal finishes without this happening, return `true`

---

## Example
### Example 1

```
Input: s = "1001"

Process:
1 → start of first segment
0 → segment of ones ends
0 → still zeros
1 → new segment appears

Output: false
```

---

### Example 2

```
Input: s = "110"

Process:
1 → first segment
1 → still same segment
0 → segment ends

Output: true
```

---

## Complexity Analysis
| Aspect | Complexity |
| ------ | ---------- |
| Time | **O(n)** |
| Space | **O(1)** |

* We only scan the string once.

---

## Common Mistakes
* Counting total number of `1`s instead of checking **continuity**
* Treating separated `1`s as a single segment
* Using unnecessary data structures

A single linear scan is enough.

---

## One-Line Interview Summary
> “Since the string starts with `1`, the string is valid if no `1` appears after the first `0`.”
