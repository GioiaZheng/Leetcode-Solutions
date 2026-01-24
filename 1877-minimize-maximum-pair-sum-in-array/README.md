# **LeetCode 1877 – Minimize Maximum Pair Sum in Array**

**Difficulty:** Medium
**Tags:** Greedy, Sorting, Two Pointers
**Link:** [https://leetcode.com/problems/minimize-maximum-pair-sum-in-array/](https://leetcode.com/problems/minimize-maximum-pair-sum-in-array/)

---

## **Problem Summary**

You are given an array `nums` of **even length**.

You must pair up all elements such that:

* Each element is used in **exactly one pair**
* The **maximum pair sum** among all pairs is **minimized**

The sum of a pair `(a, b)` is `a + b`.

Return the minimized possible value of the maximum pair sum.

---

## **Key Insight**

This is a classic **greedy pairing** problem.

The goal is **not** to minimize the total sum, but to **balance the largest pair sum**.

The optimal strategy is:

> **Always pair the smallest remaining number with the largest remaining number.**

This balances extremes and prevents any pair from becoming unnecessarily large.

---

## **Why This Greedy Strategy Works**

Assume the array is sorted:

```
a1 ≤ a2 ≤ ... ≤ a(n-1) ≤ an
```

* The largest element `an` must be paired with **some** element.
* To minimize the largest pair sum:

  * Pairing `an` with the **smallest** element `a1` gives the smallest possible sum involving `an`.
* Any other pairing would only increase (or not reduce) the maximum pair sum.

By repeating this logic, pairing extremes is always optimal.

---

## **Algorithm**

1. Sort the array `nums`
2. Use two pointers:

   * Left pointer starts at the beginning
   * Right pointer starts at the end
3. Pair `nums[left]` with `nums[right]`
4. Track the maximum pair sum
5. Move both pointers inward
6. Return the maximum pair sum encountered

---

## **Example**

### Example 1

```
Input: nums = [3,5,2,3]

Sorted: [2,3,3,5]

Pairs:
(2,5) → 7
(3,3) → 6

Answer: 7
```

---

### Example 2

```
Input: nums = [3,5,4,2,4,6]

Sorted: [2,3,4,4,5,6]

Pairs:
(2,6) → 8
(3,5) → 8
(4,4) → 8

Answer: 8
```

---

## **Complexity Analysis**

| Aspect       | Complexity                |
| ------------ | ------------------------- |
| Sorting      | **O(n log n)**            |
| Pairing scan | **O(n)**                  |
| Total Time   | **O(n log n)**            |
| Extra Space  | **O(1)** (excluding sort) |

---

## **Common Mistakes**

* ❌ Pairing adjacent elements after sorting
* ❌ Trying to minimize each pair sum individually
* ❌ Using DP or unnecessary data structures

The greedy extreme-pairing strategy is sufficient and optimal.

---

## **One-Line Interview Summary**

> “Sort the array and pair the smallest and largest elements together; the maximum of these pair sums is minimized.”
