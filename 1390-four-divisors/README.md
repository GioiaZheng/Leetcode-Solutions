# **LeetCode 1390 – Four Divisors**

**Difficulty:** Medium  
**Tags:** Math, Number Theory, Enumeration  
**Link:** [https://leetcode.com/problems/four-divisors/](https://leetcode.com/problems/four-divisors/)

---

## **Problem Summary**

You are given an integer array `nums`.

For each number in `nums`:

* If it has **exactly four positive divisors**, add the **sum of its divisors** to the result.
* Otherwise, ignore it.

Return the total sum of divisors for all numbers in `nums` that have exactly four divisors.

If no such number exists, return `0`.

---

## **Key Insight**

A number has **exactly four divisors** if and only if it is in **one of the following forms**:

1. `p³`, where `p` is a prime

   * Divisors: `1, p, p², p³`
2. `p × q`, where `p` and `q` are **distinct primes**

   * Divisors: `1, p, q, p×q`

Instead of explicitly checking prime properties, we can **enumerate divisors directly** and count them.

---

## **Approach**

For each number `x` in `nums`:

1. Enumerate all divisors up to `√x`
2. For each divisor `d`:

   * Add both `d` and `x / d` to the count
   * Accumulate their sum
3. If the divisor count exceeds `4`, stop early (pruning)
4. If the final count is exactly `4`, add the sum to the answer

---

## **Example**

### Example 1

```
Input: nums = [21, 4, 7]
Output: 32
```

Explanation:

```
21 → divisors: 1, 3, 7, 21 (sum = 32)
4  → divisors: 1, 2, 4 (ignored)
7  → divisors: 1, 7 (ignored)
```

---

### Example 2

```
Input: nums = [21, 21]
Output: 64
```

---

### Example 3

```
Input: nums = [1, 2, 3, 4, 5]
Output: 0
```

---

## **Why This Works**

* Divisors always come in **pairs**
* Enumerating only up to `√x` is sufficient
* Early stopping prevents unnecessary work
* No explicit primality testing is required

---

## **Complexity**

Let `n = len(nums)` and `M = max(nums[i])`

| Aspect | Complexity    |
| ------ | ------------- |
| Time   | **O(n · √M)** |
| Space  | **O(1)**      |

Given `M ≤ 10^5`, this is efficient.

---

## **What I Learned**

* How divisor count characterizes number structure
* The usefulness of early pruning in enumeration
* Translating number theory observations into simple code
* A clean example of math-based filtering problems

---

###  Notes

This problem pairs well with other divisor-based problems such as:

* 2427. Number of Common Factors
* 507. Perfect Number
* 172. Factorial Trailing Zeroes

---

## **One-Line Interview Summary**

> “Enumerate divisors up to sqrt(n) and sum them only if the count is exactly four.”
