# **LeetCode 1975 – Maximum Matrix Sum**

**Difficulty:** Medium  
**Tags:** Matrix, Greedy, Math  
**Link:** [https://leetcode.com/problems/maximum-matrix-sum/](https://leetcode.com/problems/maximum-matrix-sum/)

---

## **Problem Summary**

You are given an `n × n` integer matrix.

You may perform the following operation **any number of times**:

* Choose **two adjacent cells** (sharing a side)
* Multiply **both values by -1**

Your task is to **maximize the sum of all elements** in the matrix after performing any sequence of valid operations.

Return the maximum possible matrix sum.

---

## **Key Insight**

* Flipping two adjacent cells changes the **sign of exactly two elements**.
* Therefore, the **parity (even/odd)** of the number of negative elements **never changes**.
* This means:

  * If the total number of negative elements is **even**, all values can be made non-negative.
  * If the total number of negative elements is **odd**, exactly **one value must remain negative**.

Thus, the optimal strategy depends only on:

1. The **sum of absolute values**
2. The **minimum absolute value**
3. The **parity of negative elements**

---

## **Approach**

1. Initialize:

   * `total` = sum of absolute values of all elements
   * `neg_count` = number of negative elements
   * `min_abs` = minimum absolute value in the matrix
2. If `neg_count` is even:

   * All elements can be made positive
   * Return `total`
3. If `neg_count` is odd:

   * One element must remain negative
   * Subtract `2 × min_abs` from `total`

---

## **Example**

### Example 1

```
Input: matrix = [[1,-1],[-1,1]]
Output: 4
```

Explanation:

```
Absolute sum = 4
Negative count = 2 (even)
→ All values can be positive
```

---

### Example 2

```
Input: matrix = [[1,2,3],[-1,-2,-3],[1,2,3]]
Output: 16
```

Explanation:

```
Absolute sum = 18
Negative count = 3 (odd)
Minimum absolute value = 1
→ 18 - 2 × 1 = 16
```

---

## **Why This Works**

* The operation preserves the parity of negative numbers.
* Flipping signs does not change absolute values.
* To maximize the sum:

  * Make as many values positive as possible
  * If one must stay negative, choose the **smallest absolute value**

This turns a matrix operation problem into a **simple greedy calculation**.

---

## **Complexity**

Let `n` be the matrix size.

| Aspect | Complexity |
| ------ | ---------- |
| Time   | **O(n²)**  |
| Space  | **O(1)**   |

---

## **What I Learned**

* How invariants (parity of negatives) restrict possible outcomes
* Turning a complex operation problem into a greedy math solution
* Why absolute values often simplify optimization problems
* A good example of reducing a matrix problem to scalar reasoning

---

### Notes

This is a **classic trick problem** where the operation looks complex, but the solution depends on a key invariant.

Understanding this idea helps with many similar problems involving:

* Sign flips
* Parity constraints
* Greedy optimization

---

## **One-Line Interview Summary**

> “The operation preserves the parity of negatives, so the maximum sum is the total of absolute values minus twice the smallest absolute value if negatives are odd.”
