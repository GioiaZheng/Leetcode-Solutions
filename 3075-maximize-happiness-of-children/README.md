# **LeetCode 3075 – Maximize Happiness of Selected Children**

**Difficulty:** Medium  
**Tags:** Array, Greedy, Sorting  
**Link:** [https://leetcode.com/problems/maximize-happiness-of-selected-children/](https://leetcode.com/problems/maximize-happiness-of-selected-children/)

---

## **Problem Summary**

You are given an array `happiness`, where `happiness[i]` represents the happiness value of the `i`-th child.

There are `n` children standing in a queue. You will select **exactly `k` children**, one per turn.

Rules:

* When you select a child, the happiness value of **all unselected children** decreases by `1`.
* Happiness values **cannot go below `0`**.
* The decrease happens only if the value is positive.

Return the **maximum possible sum of happiness values** of the selected children.

---

## **Key Insight**

* Every time you pick a child, all remaining children lose `1` happiness.
* Therefore, if a child is picked at turn `t` (0-indexed), its effective happiness is:

```
max(happiness[i] - t, 0)
```

* To maximize the total happiness:

  * Pick children with **larger initial happiness earlier**
  * So that the reduction affects them as little as possible

This directly suggests a **greedy strategy**.

---

## **Approach**

1. Sort the `happiness` array in **descending order**.
2. Iterate through the first `k` elements:

   * For the `i`-th selected child, add:

     ```
     max(happiness[i] - i, 0)
     ```
3. Accumulate the sum and return it.

---

## **Example**

### Example 1

```
Input: happiness = [1,2,3], k = 2
Output: 4
```

Explanation:

```
Sorted happiness = [3,2,1]

Turn 0: pick 3 → gain 3
Turn 1: pick 2 → effective value = 2 - 1 = 1

Total = 3 + 1 = 4
```

---

### Example 2

```
Input: happiness = [1,1,1,1], k = 2
Output: 1
```

Explanation:

```
Sorted happiness = [1,1,1,1]

Turn 0: pick 1 → gain 1
Turn 1: pick 1 → effective value = 1 - 1 = 0

Total = 1
```

---

### Example 3

```
Input: happiness = [2,3,4,5], k = 1
Output: 5
```

Explanation:

```
Pick the maximum happiness child
```

---

## **Why This Works**

* The happiness reduction depends **only on how many children were picked before**.
* Picking the happiest children earlier minimizes their loss.
* Sorting ensures we always make the locally optimal choice, which leads to a global optimum.
* Once `happiness[i] - i` becomes `0`, further picks do not contribute.

---

## **Complexity**

| Aspect | Complexity               |
| ------ | ------------------------ |
| Time   | **O(n log n)**           |
| Space  | **O(1)** (in-place sort) |

---

## **What I Learned**

* How to convert a dynamic process into a static formula.
* Why greedy works when the cost grows linearly with time.
* A common pattern: **sort first, then apply a decreasing offset**.
* This problem is closely related to scheduling and diminishing-return optimizations.

---

### Notes

This greedy pattern also appears in problems involving:

* Diminishing rewards over time
* Priority selection with penalties
* Scheduling with linear decay
