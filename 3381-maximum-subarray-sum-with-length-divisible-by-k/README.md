# **LeetCode 3381 – Maximum Subarray Sum With Length Divisible by K**

**Difficulty:** Medium  
**Tags:** Array, Prefix Sum, Hash Map  
**Link:** [https://leetcode.com/problems/maximum-subarray-sum-with-length-divisible-by-k/](https://leetcode.com/problems/maximum-subarray-sum-with-length-divisible-by-k/)

---

## **Problem Summary**

You are given an integer array and an integer `k`.
The task is to find the **maximum subarray sum** among all subarrays whose **length is divisible by `k`**.

A subarray is defined as a contiguous part of the array.

---

## **Key Insight**

The length constraint introduces a modular condition:

```
(subarray length) % k == 0
```

A subarray from index `i+1` to `j` has length:

```
j - i
```

Thus, we require:

```
(j - i) % k == 0
→ j % k == i % k
```

This implies that valid subarrays must begin and end at positions whose indices share the same remainder modulo `k`.

For each remainder class, if we keep track of the **smallest prefix sum** seen so far, the difference between the current prefix sum and this minimum gives the best subarray ending at the current index.

---

## **Approach**

1. Compute prefix sums:

   ```
   prefix[j] = nums[0] + nums[1] + ... + nums[j]
   ```
2. Group indices by their remainder `j % k`.
3. For each remainder group:

   * Track the smallest prefix sum encountered.
   * For each new index `j`, compute:

     ```
     candidate = prefix[j] - min_prefix_in_group
     ```

     which represents a subarray length divisible by `k`.
4. Update the result with the maximum such candidate.
5. Return the largest sum found.

This uses the fact that subtracting two prefix sums yields a subarray sum.

---

## **Example**

**Input**

```
nums = [3, -1, 2, 5, -4]
k = 2
```

**Explanation**
Valid subarrays must have even length.
Among all even-length subarrays, the maximum sum occurs for the subarray `[3, -1, 2, 5] = 9`.

**Output**

```
9
```

---

## **Why This Works**

A subarray's sum is given by:

```
prefix[j] - prefix[i]
```

and its length is divisible by `k` if:

```
i % k == j % k
```

Thus, each remainder class can be treated independently, allowing us to use a classical prefix-sum maximization strategy within each class.

By keeping track of the smallest prefix sum in each class, the algorithm efficiently computes the best matching subarray ending at each index.

---

## **Complexity**

* **Time:** `O(n)`
* **Space:** `O(k)` for storing prefix minima by remainder class

---

## **What I Learned**

* How modular arithmetic applies to subarray length constraints.
* How prefix sums transform subarray-sum problems into difference calculations.
* How grouping indices by modulo classes enables efficient subarray maximization.
