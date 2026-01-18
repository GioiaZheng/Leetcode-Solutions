# **LeetCode 2872 – Maximum Number of K-Divisible Components**

**Difficulty:** Hard  
**Tags:** Tree, DFS, Greedy, Graph  
**Link:** https://leetcode.com/problems/maximum-number-of-k-divisible-components/

---

## **Problem Summary**

You are given an **undirected tree** with `n` nodes (`0` to `n-1`).

- Each node `i` has a value `values[i]`
- You may **remove any number of edges**
- After removing edges, the tree splits into **connected components**
- A split is **valid** if **every component’s total value is divisible by `k`**

Your task is to return the **maximum number of components** achievable with a valid split.

> It is guaranteed that the **sum of all values is divisible by `k`**.

---

## **Key Insight**

This is a **tree DP / DFS + greedy cut** problem.

### Core observation:

> If a subtree has a total sum divisible by `k`,  
> then **cutting it off increases the number of valid components by 1**.

So the goal is to:
- Traverse the tree bottom-up
- **Cut every subtree whose sum is divisible by `k`**
- Count how many such components we can form

---

## **Important Tree Property**

Because the graph is a **tree**:
- There is exactly **one path** between any two nodes
- DFS traversal naturally aggregates subtree sums
- Cutting an edge cleanly separates components

---

## **Strategy**

### Step 1: Build the tree
- Use adjacency list from `edges`

---

### Step 2: DFS from any root (e.g., node `0`)
For each node:
1. Compute the sum of its subtree
2. Add contributions from all children
3. If the subtree sum is divisible by `k`:
   - **Cut here**
   - Count this as **one valid component**
   - Return `0` to parent (do not propagate sum upward)
4. Otherwise:
   - Return the subtree sum to parent

---

### Step 3: Count components
- Each successful “cut” contributes **+1**
- The root itself will also count if divisible (guaranteed by problem)

---

## **Why Greedy Works**

- Cutting earlier (lower in the tree) **never hurts**
- A divisible subtree is **self-contained**
- Keeping it attached would only reduce the number of components
- Therefore, **always cut when possible**

This greedy strategy is optimal.

---

## **Example Walkthrough (Example 1)**

```

values = [1,8,1,4,4], k = 6

````

DFS discovers:
- Subtree {1,3} → sum = 12 → divisible → cut → +1
- Remaining subtree {0,2,4} → sum = 6 → divisible → +1

✅ Maximum components = `2`

---

## **Why This Works**

* DFS ensures each node is processed once
* Subtree sums are computed efficiently
* Greedy cuts maximize component count
* Tree structure guarantees no conflicts

---

## **Complexity Analysis**

| Aspect | Complexity |
| ------ | ---------- |
| Time   | **O(n)**   |
| Space  | **O(n)**   |

Efficient enough for `n ≤ 3 × 10⁴`.

---

## **Common Pitfalls**

* ❌ Trying all subsets of edges (exponential)
* ❌ Using DP on subsets
* ❌ Forgetting to reset subtree sum after a cut
* ❌ Thinking this is knapsack-like (it’s not)

---

## **What I Learned**

* Tree problems often reduce to **DFS + local greedy decisions**
* Divisibility constraints pair naturally with subtree sums
* Cutting as early as possible is often optimal in trees
* “Maximum components” usually hints at **greedy cuts**

---

## **Related Problems**

* 1245. Tree Diameter
* 2246. Longest Path With Different Adjacent Characters
* 2581. Count Number of Possible Root Nodes

---

## **One-Line Interview Summary**

> “Use DFS to compute subtree sums and greedily cut every subtree whose sum is divisible by `k` to maximize the number of components.”
