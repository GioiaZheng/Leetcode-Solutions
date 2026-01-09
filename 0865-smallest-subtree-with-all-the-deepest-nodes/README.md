# **LeetCode 865 – Smallest Subtree with all the Deepest Nodes**

**Difficulty:** Medium  
**Tags:** Tree, Depth-First Search, Binary Tree, Lowest Common Ancestor  
**Link:** [https://leetcode.com/problems/smallest-subtree-with-all-the-deepest-nodes/](https://leetcode.com/problems/smallest-subtree-with-all-the-deepest-nodes/)

---

## **Problem Summary**

You are given the root of a binary tree.

* The **depth** of a node is the number of edges from the root to that node.
* A node is called **deepest** if it has the **maximum depth** in the tree.

Your task is to return the **smallest subtree** that contains **all deepest nodes**.

The subtree must include:

* The chosen root node
* All of its descendants

---

## **Key Insight**

This problem is equivalent to finding the:

> **Lowest Common Ancestor (LCA) of all deepest leaves**

Key observations:

* If all deepest nodes are in **one subtree**, the answer lies there.
* If deepest nodes appear in **both left and right subtrees**, the current node is the answer.

This naturally suggests a **bottom-up DFS** approach.

---

## **Approach**

Use a DFS that returns **two pieces of information** for each node:

1. The **maximum depth** of its subtree
2. The **node** that represents the smallest subtree containing all deepest nodes

### DFS logic:

For a given node:

* Recursively compute `(depth, subtree_root)` for left and right children
* Compare left and right depths:

  * If `left > right`: return left result
  * If `right > left`: return right result
  * If equal: current node is the answer

---

## **Example**

### Example 1

```
Input: root = [3,5,1,6,2,0,8,null,null,7,4]
Output: [2,7,4]
```

Explanation:

* Deepest nodes are `7` and `4`
* Their lowest common ancestor is node `2`
* Subtree rooted at `2` is the smallest subtree containing all deepest nodes

---

### Example 2

```
Input: root = [1]
Output: [1]
```

---

### Example 3

```
Input: root = [0,1,3,null,2]
Output: [2]
```

---

## **Why This Works**

* DFS computes subtree depth information efficiently
* The comparison of left and right depths identifies where deepest nodes are located
* When depths are equal, the current node is the LCA of deepest nodes
* Each node is processed exactly once

---

## **Complexity**

Let `n` be the number of nodes and `h` the height of the tree.

| Aspect | Complexity |
| ------ | ---------- |
| Time   | **O(n)**   |
| Space  | **O(h)**   |

Space complexity comes from the recursion stack.

---

## **What I Learned**

* How to combine depth computation with result propagation
* A clean way to find LCA using bottom-up DFS
* Why returning multiple values from recursion simplifies tree problems
* The close relationship between depth-based problems and LCA

---

### Notes

This problem is identical to:

* **1123. Lowest Common Ancestor of Deepest Leaves**

It also relates closely to:

* 236. Lowest Common Ancestor of a Binary Tree
* 1339. Maximum Product of Splitted Binary Tree

---

## **One-Line Interview Summary**

> “Use bottom-up DFS returning (depth, node); when left and right depths are equal, the current node is the smallest subtree containing all deepest nodes.”
