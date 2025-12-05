# **LeetCode 26 – Remove Duplicates from Sorted Array**

**Difficulty:** Easy  
**Tags:** Array, Two Pointers  
**Link:** [https://leetcode.com/problems/remove-duplicates-from-sorted-array/](https://leetcode.com/problems/remove-duplicates-from-sorted-array/)

---

## **Problem Summary**

You are given a sorted array of integers.
Your task is to remove duplicate values **in-place**, ensuring that each unique element appears exactly once.

The function should return the number of unique elements.
The first `k` elements of the array (after modification) should contain the unique values in their original order.

No additional array may be allocated; the operation must be performed using constant extra space.

---

## **Key Insight**

Because the array is already sorted:

* All duplicates appear **next to each other**.
* A single linear scan is enough to identify unique values.
* The **two-pointer technique** allows us to overwrite duplicates while preserving the required elements.

One pointer tracks the **position to write the next unique value**, and the other pointer scans through the array.

---

## **Approach**

1. If the array is empty, the result is `0`.
2. Initialize a write pointer `i` at index `0`.
3. Traverse the array with a read pointer `j`:

   * Whenever `nums[j] != nums[i]`, increment `i` and write `nums[j]` to `nums[i]`.
4. At the end, the number of unique elements is `i + 1`.

This ensures that all unique values are stored at the front of the array in sorted order.

---

## **Example**

**Input**

```
nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
```

**Explanation**

* Unique elements are: `[0, 1, 2, 3, 4]`
* They occupy the first 5 positions in the modified array.

**Output**

```
5
```

---

## **Why This Works**

The sorted property guarantees that:

```
nums[j] != nums[i]
```

implies a new unique value.
By overwriting the next available position, we avoid the need for additional storage and satisfy the in-place requirement.

The two-pointer technique ensures linear time complexity with constant extra memory.

---

## **Complexity**

* **Time:** `O(n)`
* **Space:** `O(1)`

---

## **What I Learned**

* How sorted structure simplifies duplicate detection.
* How the two-pointer technique enables in-place modification.
* Why in-place array rewriting is commonly paired with pointer-based iteration.

**0027 – Remove Element**
