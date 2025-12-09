# **LeetCode 912 – Sort an Array**

**Difficulty:** Medium  
**Tags:** Sorting, Divide and Conquer  
**Link:** [https://leetcode.com/problems/sort-an-array/](https://leetcode.com/problems/sort-an-array/)

---

## **Problem Summary**

You are given an array `nums` and must return it sorted in **ascending order**.

However:

* You **cannot** use built-in sorting functions.
* The solution must run in **O(n log n)** time.
* Space usage should be as small as possible.

---

## **Key Insight**

The problem explicitly forbids built-in sorting and expects you to implement a classic **O(n log n)** sorting algorithm. Valid choices include:

* **Merge Sort** (stable, simpler to implement)
* **Heap Sort** (O(1) space, but more complex)
* **Quick Sort** (avg O(n log n), but worst-case O(n²))

Among them, **Merge Sort** offers:

* Guaranteed O(n log n)
* Clean recursive structure
* Easy correctness
* Good interview demonstration

Thus, Merge Sort is the ideal approach.

---

## **Approach: Merge Sort**

###  Divide

Split the array into two halves recursively:

$$
\text{left} = \text{nums}[0:\text{mid}], \quad \text{right} = \text{nums}[\text{mid}:]
$$

###  Conquer

Sort each half recursively.

###  Combine

Merge the two sorted halves by comparing elements one by one.

Merge step ensures:

* Correct ascending order
* Linear merging: **O(n)**

Overall complexity remains:

$$
O(n \log n)
$$

---

## **Example**

### Example 1

```
Input:  [5,2,3,1]
Output: [1,2,3,5]
```

### Example 2

```
Input:  [5,1,1,2,0,0]
Output: [0,0,1,1,2,5]
```

---

## **Why This Works**

* Merge Sort guarantees **O(n log n)** in all cases.
* It does not rely on built-ins, satisfying constraints.
* Recursion divides the array into smaller parts until trivially sorted.
* Merging ensures correct ordering with linear additional work.

This algorithm is reliable, predictable, and suitable for large inputs.

---

## **Complexity**

| Aspect    | Complexity                |
| --------- | ------------------------- |
| **Time**  | O(n log n)                |
| **Space** | O(n) due to merge buffers |

(Heap Sort can achieve O(1) space but is significantly more complex.)

---

## **What I Learned**

* How Merge Sort uses divide-and-conquer to achieve optimal sorting time.
* Why built-in sorts are often O(n log n) under the hood.
* How to merge two sorted arrays efficiently.
* The trade-off between speed, stability, and memory in sorting algorithms.
