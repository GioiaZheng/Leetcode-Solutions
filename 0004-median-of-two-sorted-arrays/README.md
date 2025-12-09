# **LeetCode 4 – Median of Two Sorted Arrays**

**Difficulty:** Hard  
**Tags:** Binary Search, Divide and Conquer, Partitioning  
**Link:** [https://leetcode.com/problems/median-of-two-sorted-arrays/](https://leetcode.com/problems/median-of-two-sorted-arrays/)

---

## **Problem Summary**

You are given two sorted arrays `nums1` and `nums2`, of sizes `m` and `n` respectively.
Your task is to compute the **median** of the two arrays when they are merged into one sorted array.

However, you must achieve this in:

```
O(log(m + n)) time complexity.
```

A direct merge or full sort would require `O(m + n)` or `O((m+n) log(m+n))`,
and therefore **cannot** be used.

---

## **Key Insight**

The classical merge approach is too slow because the arrays may include up to 2000 elements.
To meet the logarithmic time requirement, we need a strategy that eliminates half of the search space each step.

The key idea is to treat the problem as finding the correct **partition** of the two arrays such that:

```
All elements on the left side of the partition 
≤ 
All elements on the right side.
```

If we find such a partition, then:

* For odd total length:
  The median is the **minimum** of the right partition.
* For even total length:
  The median is the **average** of:

  * The **maximum** value from the left partition
  * The **minimum** value from the right partition

We apply **binary search** on the smaller array to find the correct partition position.

This reduces the search space at every step and gives the required `O(log(m+n))`.

---

## **Approach**

1. Always binary-search on the **shorter array** to simplify partitioning logic.
2. Let:

   ```
   total = m + n
   half = total // 2
   ```
3. Perform binary search on `nums1` for a partition index `i`.
4. Partition `nums2` accordingly:

   ```
   j = half - i
   ```
5. Extract the border values:

   ```
   nums1_left, nums1_right
   nums2_left, nums2_right
   ```

   Using `+inf` or `-inf` for out-of-bounds indices.
6. Check if the partition is valid:

   ```
   nums1_left <= nums2_right
   and 
   nums2_left <= nums1_right
   ```
7. If valid:

   * If total length is odd → return min(right values)
   * If even → return (max(left values) + min(right values)) / 2
8. Otherwise adjust binary search range:

   * If nums1_left > nums2_right → move left
   * Else → move right

This guarantees logarithmic time complexity.

---

## **Example**

**Input**

```
nums1 = [1, 2]
nums2 = [3, 4]
```

Merged array would be:

```
[1, 2, 3, 4]
```

Left partition and right partition:

```
Left:  [1, 2]
Right: [3, 4]
```

Median:

```
(2 + 3) / 2 = 2.5
```

**Output**

```
2.5
```

---

## **Why This Works**

The key observation is:

### Median depends only on the boundary between the left half and the right half.

By searching for the correct boundary using binary search:

* We avoid merging arrays.
* We avoid full sorting.
* We eliminate half of the search space each iteration.
* We treat both arrays as contributing to a single combined sorted order.

The use of `±∞` for edge cases ensures clean comparisons without extra conditionals.

This is one of the most elegant applications of binary search in algorithm design.

---

## **Complexity**

| Metric    | Value               |
| --------- | ------------------- |
| **Time**  | `O(log(min(m, n)))` |
| **Space** | `O(1)`              |

---

## **What I Learned**

* How binary search can be applied to partition boundaries instead of numeric targets.
* Why median problems often reduce to balancing left and right partitions.
* How to use conceptual “virtual merge” instead of explicitly building arrays.
* The importance of always binary-searching the shorter array to avoid invalid partitions.
* How to represent out-of-bounds values with `±∞` to simplify logic.
