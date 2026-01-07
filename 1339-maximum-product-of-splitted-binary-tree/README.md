# **LeetCode 1339 – Maximum Product of Splitted Binary Tree**

**Difficulty:** Medium  
**Tags:** Tree, Depth-First Search, Binary Tree, Math  
**Link:** [https://leetcode.com/problems/maximum-product-of-splitted-binary-tree/](https://leetcode.com/problems/maximum-product-of-splitted-binary-tree/)

---

## **Problem Summary**

You are given the root of a binary tree.

You may **remove exactly one edge** to split the tree into **two subtrees**.

Let:

* `sum1` = sum of values in the first subtree
* `sum2` = sum of values in the second subtree

Your goal is to **maximize**:

```
sum1 × sum2
```

Return the maximum product **modulo 10^9 + 7**.

⚠️ Important:
The product must be maximized **before** taking the modulo.

---

## **Key Insight**

* Removing an edge is equivalent to:

  * Choosing a subtree with sum `s`
  * The remaining part has sum `total_sum − s`
* For each possible split, the product is:

  ```
  s × (total_sum − s)
  ```
* Therefore:

  * If we know the **sum of every subtree**
  * We can try all possible splits and take the maximum

This turns the problem into a **tree traversal + math optimization** task.

---

## **Approach**

1. Use **DFS** to compute:

   * The sum of each subtree
   * The total sum of the tree
2. Store all subtree sums in a list
3. For each subtree sum `s`:

   * Compute `s × (total_sum − s)`
   * Track the maximum product
4. Return the maximum product modulo `10^9 + 7`

---

## **Example**

### Example 1

```
Input: root = [1,2,3,4,5,6]
Output: 110
```

Explanation:

```
Total sum = 21
Best split:
  Subtree sum = 11
  Remaining sum = 10
  Product = 110
```

---

### Example 2

```
Input: root = [1,null,2,3,4,null,null,5,6]
Output: 90
```

---

## **Why This Works**

* Every possible split corresponds to exactly **one subtree**
* DFS ensures:

  * Each node is visited once
  * Each possible subtree sum is considered
* The formula `s × (total − s)` is evaluated for all candidates
* The optimal split is guaranteed to be found

---

## **Complexity**

Let `n` be the number of nodes.

| Aspect | Complexity |
| ------ | ---------- |
| Time   | **O(n)**   |
| Space  | **O(n)**   |

Space is used to store subtree sums.

---

## **What I Learned**

* How tree structure maps naturally to partition problems
* Using subtree sums to evaluate global optimization
* Separating computation (DFS) from optimization logic
* A classic pattern for “remove one edge” tree problems

---

###  Notes

This problem is closely related to:

* 124. Binary Tree Maximum Path Sum
* 543. Diameter of Binary Tree
* 1161. Maximum Level Sum of a Binary Tree

All of them rely on **DFS with aggregation**.

---

## **One-Line Interview Summary**

> “Compute all subtree sums with DFS, then maximize `s × (total − s)` over all subtrees.”
