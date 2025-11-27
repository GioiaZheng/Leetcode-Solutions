# 3381. Maximum Subarray Sum With Length Divisible by K

**Difficulty:** Medium  
**Topics:** Prefix Sum, Modular Arithmetic  
**Link:** https://leetcode.com/problems/maximum-subarray-sum-with-length-divisible-by-k/

---

##  Problem Description

Given an integer array `nums` and an integer `k`, return the **maximum sum of any subarray whose length is divisible by k**.

A subarray must be continuous.

---

##  Examples

### Example 1
```

Input: nums = [1,2], k = 1
Output: 3

```
Subarray `[1,2]` has length 2, and `2 % 1 == 0`.

---

### Example 2
```

Input: nums = [-1,-2,-3,-4,-5], k = 4
Output: -10

```
Best valid subarray is:
```

[-1, -2, -3, -4]

```
Length 4, `4 % 4 == 0`.

---

### Example 3
```

Input: nums = [-5,1,2,-3,4], k = 2
Output: 4

```
Best valid subarray:
```

[1, 2, -3, 4]

```
Length = 4, divisible by 2, sum = 4.

---

##  Key Insight

Let:

```

prefix[i] = sum(nums[0..i-1])

```

Subarray (l, r) satisfies:
```

(r - l + 1) % k == 0

```

This implies:
```

(r+1) % k == l % k

```

Therefore:

 subarray sum = `prefix[r+1] - prefix[l]`  
 **prefix indices must have the same remainder modulo k**

So we:

1. Compute prefix sums
2. Split prefix indices by `(index % k)`
3. For each group, compute:
```

max(prefix[i] - min_prefix_in_same_group)

```

This finds the maximum subarray sum with length divisible by k.

---

##  Complexity

```

Time:  O(n)
Space: O(k)

````

## ✔ Summary

* Convert problem to prefix sums
* Use index modulo k to group valid subarrays
* Track minimum prefix per group
* Compute max(prefix[i] – min_prefix[group])

Efficient and elegant O(n) solution.


