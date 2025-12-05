# **LeetCode 27 – Remove Element**

**Difficulty:** Easy  
**Tags:** Array, Two Pointers  
**Link:** [https://leetcode.com/problems/remove-element/](https://leetcode.com/problems/remove-element/)

---

## **Problem Summary**

You are given an array `nums` and an integer `val`.
Your task is to remove all occurrences of `val` **in-place** and return the number of elements that remain.

The order of the remaining elements does not need to be preserved.
You must perform the operation using constant extra space.

---

## **Key Insight**

Since the order of the remaining elements does not matter:

* We do **not** need to shift all later elements forward.
* Instead, when encountering `val`, we can replace it with the last valid element and shrink the effective array size.

This allows us to achieve optimal performance using two pointers:

* One pointer scans the array.
* The other pointer tracks the current valid array boundary.

---

## **Approach**

1. Initialize a pointer `k` to track the current valid length (start with `len(nums)`).
2. Iterate through the array with index `i`.
3. Whenever `nums[i] == val`:

   * Replace `nums[i]` with `nums[k - 1]`.
   * Reduce `k` by 1.
   * Do **not** increment `i`, because the swapped value must be checked.
4. If `nums[i] != val`, simply move to the next index.
5. The value of `k` after the loop is the number of remaining elements.

This approach minimizes data movement and keeps complexity linear.

---

## **Example**

**Input**

```
nums = [3, 2, 2, 3]
val = 3
```

**Explanation**

* Remove all `3`s.
* Remaining elements may be `[2, 2]`.

**Output**

```
2
```

---

## **Why This Works**

Because the problem explicitly allows the remaining elements to be in any order, the swap-with-end strategy is permissible and optimal.

This avoids the costly operation of shifting elements after each deletion, reducing the time complexity to linear.

The two-pointer technique ensures that:

* Only necessary swaps occur.
* The algorithm maintains constant space usage.
* No extra array is required.

---

## **Complexity**

* **Time:** `O(n)`
* **Space:** `O(1)`

---

## **What I Learned**

* How relaxing ordering constraints enables more efficient solutions.
* Why swapping with the end is a powerful method for element removal.
* How two-pointer techniques adapt to differing problem constraints.
