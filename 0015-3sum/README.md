# **LeetCode 15 – 3Sum**

**Difficulty:** Medium  
**Tags:** Array, Two Pointers, Sorting  
**Link:** [https://leetcode.com/problems/3sum/](https://leetcode.com/problems/3sum/)

---

## **Problem Summary**

You are given an integer array `nums`.

Your task is to find **all unique triplets** `[nums[i], nums[j], nums[k]]` such that:

* `i ≠ j`, `i ≠ k`, `j ≠ k`
* `nums[i] + nums[j] + nums[k] == 0`

The solution **must not contain duplicate triplets**.

The order of triplets and the order of numbers inside a triplet do **not** matter.

---

## **Key Insight**

* Sorting the array allows:

  * Efficient searching using the **two-pointer technique**
  * Easy handling of **duplicate values**
* Once sorted:

  * Fix one number
  * Reduce the problem to a **2Sum** search on the remaining array

This transforms a brute-force `O(n³)` problem into an `O(n²)` solution.

---

## **Approach**

1. **Sort** the array.
2. Iterate through the array with index `i`:

   * Skip duplicate values for `nums[i]`
3. For each `i`, use two pointers:

   * `left = i + 1`
   * `right = n - 1`
4. Compute the sum:

   * If sum == 0 → record the triplet
   * If sum < 0 → move `left` forward
   * If sum > 0 → move `right` backward
5. After finding a valid triplet:

   * Skip duplicates for both `left` and `right`

---

## **Example**

### Example 1

```
Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
```

Explanation:

Sorted array:

```
[-4, -1, -1, 0, 1, 2]
```

Valid triplets:

```
-1 + -1 + 2 = 0
-1 +  0 + 1 = 0
```

---

### Example 2

```
Input: nums = [0,1,1]
Output: []
```

---

### Example 3

```
Input: nums = [0,0,0]
Output: [[0,0,0]]
```

---

## **Why This Works**

* Sorting enables deterministic pointer movement.
* Two-pointer search efficiently finds pairs with a target sum.
* Skipping duplicates ensures:

  * Each triplet is unique
  * No redundant results
* Each valid combination is explored exactly once.

---

## **Complexity**

Let `n = len(nums)`.

| Aspect | Complexity                  |
| ------ | --------------------------- |
| Time   | **O(n²)**                   |
| Space  | **O(1)** (excluding output) |

---

## **What I Learned**

* How sorting simplifies multi-sum problems.
* Correct and careful handling of duplicates.
* Applying two-pointer techniques beyond 2Sum.
* A foundational pattern for many array problems.

---

### Notes

This problem is the foundation for many related problems:

* 16. 3Sum Closest
* 18. 4Sum
* 611. Valid Triangle Number

Mastering **3Sum** makes these much easier.

---

## **One-Line Interview Summary**

> “Sort the array, fix one element, then use two pointers to find pairs summing to the target while skipping duplicates.”
