# **LeetCode 961 – N-Repeated Element in Size 2N Array**

**Difficulty:** Easy  
**Tags:** Array, Hash Table  
**Link:** [https://leetcode.com/problems/n-repeated-element-in-size-2n-array/](https://leetcode.com/problems/n-repeated-element-in-size-2n-array/)

---

## **Problem Summary**

You are given an integer array `nums` with the following properties:

* `nums.length == 2 * n`
* `nums` contains exactly `n + 1` **distinct elements**
* **One element is repeated exactly `n` times**
* All other elements appear exactly once

Return the element that is repeated `n` times.

---

## **Key Insight**

* Because there is **only one repeated element**, and it appears **n times**,
  it must appear **very frequently** in the array.
* While scanning the array, the **first element that appears twice**
  must be the repeated one.
* Therefore, we do **not** need to count frequencies or sort the array.

A simple hash set is sufficient.

---

## **Approach**

1. Create an empty set `seen`.
2. Traverse the array:

   * If the current element is already in `seen`, return it immediately.
   * Otherwise, add it to `seen`.
3. The first repeated element encountered is guaranteed to be the answer.

---

## **Example**

### Example 1

```
Input: nums = [1,2,3,3]
Output: 3
```

---

### Example 2

```
Input: nums = [2,1,2,5,3,2]
Output: 2
```

---

### Example 3

```
Input: nums = [5,1,5,2,5,3,5,4]
Output: 5
```

---

## **Why This Works**

* The problem guarantees exactly one element is repeated `n` times.
* Any duplicate detected during traversal **must be the answer**.
* Early exit avoids unnecessary computation.
* This leverages the strong constraints of the problem.

---

## **Complexity**

| Aspect | Complexity |
| ------ | ---------- |
| Time   | **O(n)**   |
| Space  | **O(n)**   |

Where `n = nums.length / 2`.

---

## **What I Learned**

* How strong problem constraints can simplify solutions.
* When early termination is safe and optimal.
* A clean use case for hash sets in array problems.
* An example where frequency counting is unnecessary.

---

###  Notes

Alternative solutions exist (e.g., random sampling or adjacent comparison),
but the hash set approach is:

* The clearest
* The safest
* The easiest to reason about

Especially suitable for interviews and clean code repositories.

---

## **One-Line Interview Summary**

> “Scan the array and return the first element that appears twice using a hash set.”
