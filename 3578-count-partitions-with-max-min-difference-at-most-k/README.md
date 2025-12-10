# 3578. Count Partitions With Max-Min Difference at Most K

**Difficulty:** Medium  
**Topics:** Sliding Window, Monotonic Queue, Dynamic Programming, Prefix Sum  
**Link:** https://leetcode.com/problems/count-partitions-with-max-min-difference-at-most-k/

---

## Problem Description

You are given an integer array `nums` and an integer `k`.  
Your task is to partition `nums` into **one or more non-empty contiguous segments**, such that:

```

max(segment) - min(segment) <= k

```

Return the **number of valid ways** to partition the array.  
Since the answer can be large, return it modulo `1e9 + 7`.

---

## Examples

### Example 1
```

Input: nums = [9,4,1,3,7], k = 4
Output: 6

```

Valid partitions include:
```

[[9], [4], [1], [3], [7]]
[[9], [4], [1], [3, 7]]
[[9], [4], [1, 3], [7]]
[[9], [4, 1], [3], [7]]
[[9], [4, 1], [3, 7]]
[[9], [4, 1, 3], [7]]

```

### Example 2
```

Input: nums = [3,3,4], k = 0
Output: 2

```

Valid partitions:
```

[[3], [3], [4]]
[[3, 3], [4]]

```

---

## Key Insight

A segment `[l..r]` is valid if:

```

max(nums[l..r]) - min(nums[l..r]) <= k

```

For each `r`, we find the smallest `l` such that `[l..r]` is valid.  
All starting points `l..r` produce valid partitions.

Let `dp[i]` = number of valid ways to partition `nums[0..i-1]`.

Then:
```

dp[r+1] = dp[l] + dp[l+1] + ... + dp[r]

```

We can compute this sum using prefix sums.

To find the valid window `[l..r]`, we use:

- A **monotonic decreasing deque** to track the max  
- A **monotonic increasing deque** to track the min  

This gives O(n) window expansion.

---

## Algorithm

1. Use two monotonic queues to maintain max/min in window `[l..r]`.
2. Slide `r` from left to right; move `l` until `max - min <= k`.
3. For each `r`, all starts from `l..r` are valid.
4. Use prefix sums to compute:
```

dp[r+1] = sum(dp[l..r])

```
5. Update prefix sum and continue.

---

## Complexity

```

Time:  O(n)
Space: O(n)

```

---

## Summary

- Sliding window ensures all valid segments.
- Monotonic queues maintain max/min in O(1).
- DP + prefix sums count partitions efficiently.
- Works within constraints up to 5 * 10^4.
