# **LeetCode 3583 – Count Special Triplets**

**Difficulty:** Medium  
**Tags:** Hash Map, Prefix/Suffix Frequency, Combinatorics  
**Link:** [https://leetcode.com/problems/count-special-triplets/](https://leetcode.com/problems/count-special-triplets/)

---

## **Problem Summary**

You are given an integer array `nums`.

A *special triplet* is a tuple `(i, j, k)` such that:

* `0 ≤ i < j < k < n`
* `nums[i] == nums[j] * 2`
* `nums[k] == nums[j] * 2`

Your task is to count all such special triplets and return the result modulo `(10^9 + 7)`.

---

## **Key Insight**

For each middle index `j`, the triplet `(i, j, k)` is valid only if:

```
nums[i] = 2 * nums[j]   for i < j
nums[k] = 2 * nums[j]   for k > j
```

Thus, the number of valid triplets centered at index `j` is:

```
count_left(2 * nums[j])  ×  count_right(2 * nums[j])
```

This naturally leads to a **prefix–suffix frequency** technique:

* Use a **left counter** to track values in the prefix `[0…j-1]`.
* Use a **right counter** for the suffix `[j+1…n-1]`.

As we move from left to right, we dynamically update these frequency tables, allowing us to compute contributions for each `j` in **O(1)** time.

This transforms the entire problem into **O(n)** complexity.

---

## **Approach**

1. Build a frequency table `rightCount` containing all numbers in `nums`.
   This represents all possible `k > j`.

2. Initialize an empty `leftCount`, representing all `i < j`.

3. Iterate through the array with index `j`.
   For each `j`:

   * Remove `nums[j]` from `rightCount` (it cannot serve as `k` anymore).
   * Let `need = 2 × nums[j]`.
   * Count valid prefixes and suffixes:

     ```
     leftCount[need]  → number of valid i
     rightCount[need] → number of valid k
     ```
   * Multiply the two counts and add to the answer.
   * Add `nums[j]` to `leftCount`, since it will be part of prefixes for future indices.

4. Return the total count modulo `(10^9 + 7)`.

This method avoids any nested loops and leverages hash maps for constant-time lookups.

---

## **Example**

**Input**

```
nums = [8, 4, 2, 8, 4]
```

Valid triplets:

1. `(0, 1, 3)` → `8 = 4*2`
2. `(1, 2, 4)` → `4 = 2*2`

**Output**

```
2
```

Each valid triplet arises from matching the middle element with correct values on both sides.

---

## **Why This Works**

This strategy succeeds because:

* The constraint `i < j < k` naturally splits the problem into **left** and **right** segments.
* The equation `nums[i] = nums[j] * 2` and `nums[k] = nums[j] * 2` depends only on **frequency**, not order.
* Maintaining prefix and suffix frequency tables allows constant-time evaluation per index.
* The entire process runs in **one linear scan**, making it optimal for arrays up to size `10^5`.

The key idea is recognizing that each `j`'s contribution is fully determined by how many required values exist on each side—turning an apparent triple nested loop into a simple linear pass.

---

## **Complexity**

* **Time:** `O(n)` — single pass with constant-time hash map operations.
* **Space:** `O(n)` — two frequency tables.

---

## **What I Learned**

* How a triplet-counting problem can be transformed using prefix–suffix counting.
* How to apply combinatorics (`count_left × count_right`) to avoid nested loops.
* Why hash maps enable linear-time solutions in frequency-dependent problems.
* A powerful pattern: **Fix the middle element → count valid left and right values**.
