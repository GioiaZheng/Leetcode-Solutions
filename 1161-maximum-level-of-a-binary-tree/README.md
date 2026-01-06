# **LeetCode 1161 – Maximum Level Sum of a Binary Tree**

**Difficulty:** Medium  
**Tags:** Tree, Breadth-First Search, Binary Tree  
**Link:** [https://leetcode.com/problems/maximum-level-sum-of-a-binary-tree/](https://leetcode.com/problems/maximum-level-sum-of-a-binary-tree/)

---

## **Problem Summary**

You are given the root of a binary tree.

* The root is at **level 1**
* Its children are at **level 2**, and so on

For each level, compute the **sum of node values** at that level.

Return the **smallest level number** that has the **maximum sum**.

---

## **Key Insight**

* This is a classic **level-order traversal (BFS)** problem.
* Each level can be processed independently.
* BFS naturally processes levels from top to bottom, which helps ensure:

  * If multiple levels have the same maximum sum,
  * The **smallest level index** is returned automatically.

---

## **Approach**

1. Use a queue to perform **Breadth-First Search**.
2. Initialize:

   * `level = 1`
   * `max_sum = -∞`
   * `answer_level = 1`
3. While the queue is not empty:

   * Process all nodes currently in the queue (one full level)
   * Compute the sum of their values
   * Compare with `max_sum`:

     * If greater, update `max_sum` and `answer_level`
4. Increment level counter and continue.

---

## **Example**

### Example 1

```
Input: root = [1,7,0,7,-8,null,null]
Output: 2
```

Explanation:

```
Level 1 sum = 1
Level 2 sum = 7 + 0 = 7
Level 3 sum = 7 + (-8) = -1
```

Maximum sum is `7` at **level 2**.

---

### Example 2

```
Input: root = [989,null,10250,98693,-89388,null,null,null,-32127]
Output: 2
```

---

## **Why This Works**

* BFS guarantees nodes are grouped by level.
* Each node is visited exactly once.
* Tracking the maximum sum during traversal is efficient and safe.
* No recursion is needed, avoiding stack overflow for deep trees.

---

## **Complexity**

Let `n` be the number of nodes.

| Aspect | Complexity |
| ------ | ---------- |
| Time   | **O(n)**   |
| Space  | **O(n)**   |

The queue may store up to one full level of nodes.

---

## **What I Learned**

* How BFS naturally fits level-based tree problems.
* Why level-order traversal simplifies aggregation tasks.
* Handling ties by relying on traversal order.
* A clean pattern for many binary tree level problems.

---

###  Notes

This problem pairs well with other BFS-based tree problems such as:

* 102. Binary Tree Level Order Traversal
* 199. Binary Tree Right Side View
* 637. Average of Levels in Binary Tree

---

## **One-Line Interview Summary**

> “Perform BFS, compute the sum at each level, and return the smallest level with the maximum sum.”
