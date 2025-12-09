# **LeetCode 164 – Maximum Gap**

**Difficulty:** Medium  
**Tags:** Bucket Sort, Pigeonhole Principle, Sorting  
**Link:** [https://leetcode.com/problems/maximum-gap/](https://leetcode.com/problems/maximum-gap/)

---

## **Problem Summary**

You are given an unsorted integer array `nums`.
You must return the **maximum difference between two successive elements** in its **sorted** order.

If `nums` contains fewer than two elements, return `0`.

A key constraint of the problem is:

```
You must write an algorithm that runs in linear time and uses linear extra space.
```

This rules out comparison-based sorting (`O(n log n)`), even though such a solution may pass on LeetCode.

---

## **Key Insight**

The classical approach would be to sort the array and check adjacent pairs.
However, sorting costs `O(n log n)`, which violates the problem’s requirement.

To solve this in **linear time**, we rely on:

### **Pigeonhole Principle + Bucketization**

For an array with:

```
min_val = min(nums)
max_val = max(nums)
n = len(nums)
```

If we create **n − 1 buckets** evenly distributed between `[min_val, max_val]`, then:

> **The maximum gap cannot occur inside a single bucket.
> It must occur between two consecutive non-empty buckets.**

Each bucket only needs to store:

* The smallest number placed in it
* The largest number placed in it

This makes the algorithm linear.

---

## **Approach**

1. If the array has fewer than two elements, return 0.
2. Compute `min_val` and `max_val`.
   If they are equal, return 0 (all elements identical → no gap).
3. Compute bucket size:

```
bucket_size = max(1, (max_val - min_val) // (n - 1))
```

4. Determine total buckets:

```
bucket_count = (max_val - min_val) // bucket_size + 1
```

5. Create arrays `bucket_min` and `bucket_max`, initializing:

   * `bucket_min` to +∞
   * `bucket_max` to −∞
6. For each element in nums:

   * Compute its bucket index
   * Update that bucket's min and max
7. Finally, scan through buckets:

   * Track the previous bucket’s max
   * The maximum gap is:

```
bucket_min[current] - bucket_max[previous]
```

8. Return the maximum gap.

---

## **Example**

**Input**

```
nums = [3, 6, 9, 1]
```

Sorted order:

```
[1, 3, 6, 9]
```

Adjacent differences:

```
(1,3) = 2
(3,6) = 3
(6,9) = 3
```

**Output**

```
3
```

---

## **Why This Works**

The pigeonhole principle guarantees that:

* If numbers are spread across a range,
* And if we create `n−1` intervals (buckets),
* Then **at least one bucket will be "wide enough" to enforce that adjacent sorted values fall into different buckets**.

Since each bucket has a limited internal range, **the maximum gap must be found between buckets**, not within one.

Thus:

* We avoid sorting
* We achieve true **O(n)** complexity
* We maintain correctness via mathematical reasoning instead of comparison sorting

---

## **Complexity**

* **Time:** `O(n)` — iterate through all elements twice (bucketing + scanning)
* **Space:** `O(n)` — bucket min/max arrays

---

## **What I Learned**

* How to use the pigeonhole principle to eliminate the need for sorting.
* Why maximum gap cannot occur inside a bucket when buckets are sized optimally.
* How bucket sort principles apply to numeric-range problems.
* The difference between “LeetCode Accepted” and “algorithmically correct under constraints.”
* How to design linear-time algorithms using mathematical insights instead of comparison operations.
