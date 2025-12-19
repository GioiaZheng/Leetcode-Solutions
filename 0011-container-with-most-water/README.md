# **LeetCode 11 – Container With Most Water**

**Difficulty:** Medium  
**Tags:** Array, Two Pointers  
**Link:** [https://leetcode.com/problems/container-with-most-water/](https://leetcode.com/problems/container-with-most-water/)

---

## **Problem Summary**

You are given an integer array `height` of length `n`.

Each element represents a vertical line drawn at position `i` with height `height[i]`.

Choose **two lines** such that together with the x-axis they form a container,
and the container holds the **maximum amount of water**.

You may **not slant** the container.

---

## **Key Insight**

* The amount of water is determined by:

  * the **distance** between two lines
  * the **shorter height** of the two lines
* The area formula is:

```text
area = (right - left) * min(height[left], height[right])
```

* To maximize the area efficiently:

  * Start with the **widest container**
  * Gradually shrink the width
  * Always move the pointer at the **shorter line**

---

## **Approach**

1. Initialize two pointers:

   * `left` at the beginning
   * `right` at the end
2. Compute the area formed by the two pointers.
3. Update the maximum area.
4. Move the pointer with the **smaller height** inward.
5. Repeat until the pointers meet.

This guarantees that all potential maximum containers are considered.

---

## **Example**

### Example 1

```
Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
```

---

### Example 2

```
Input: height = [1,1]
Output: 1
```

---

## **Why This Works**

* The width decreases at every step.
* The height is always limited by the **shorter line**.
* Moving the taller line cannot increase the area.
* Moving the shorter line is the **only chance** to find a larger container.

This leads to a linear-time solution.

---

## **Complexity**

| Aspect | Complexity |
| ------ | ---------- |
| Time   | **O(n)**   |
| Space  | **O(1)**   |

---

## **What I Learned**

* How to optimize brute-force problems using two pointers.
* Why greedy pointer movement works in this scenario.
* A classic example of reducing `O(n²)` to `O(n)`.
* One of the most important two-pointer patterns in interviews.

---

###  Notes

This problem is a cornerstone of the **Two Pointers** technique.

Understanding it helps with problems such as:

* Trapping Rain Water
* 3Sum
* Sliding Window optimizations
