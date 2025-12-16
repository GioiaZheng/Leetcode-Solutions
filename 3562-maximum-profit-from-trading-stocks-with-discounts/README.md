# **LeetCode 3562 – Maximum Profit from Trading Stocks with Discounts**

**Difficulty:** Hard  
**Tags:** Tree DP, Knapsack, Dynamic Programming, DFS  
**Link:** [https://leetcode.com/problems/maximum-profit-from-trading-stocks-with-discounts/](https://leetcode.com/problems/maximum-profit-from-trading-stocks-with-discounts/)

---

## **Problem Summary**

You are given a company hierarchy with `n` employees, where:

* Each employee can buy **at most one stock** today at price `present[i]`
* The stock can be sold tomorrow at price `future[i]`
* Employee `1` is the CEO (root of the tree)
* The hierarchy forms a **tree**, with edges from boss → subordinate
* You have a fixed **budget**

### Discount Rule

If an employee’s **direct boss** buys their stock, the employee can buy their stock at **half price**:

```
floor(present[i] / 2)
```

### Goal

Choose a subset of employees to buy stocks such that:

* Total cost ≤ budget
* Total profit is maximized
* Profit = sum(future[i] − buying_price[i])

Return the **maximum achievable profit**.

---

## **Key Observations**

1. The hierarchy is a **tree**:

   * Acyclic
   * Connected
   * Rooted at employee `1`

2. Whether an employee gets a discount depends **only on whether their parent buys**.

3. Whether a child gets a discount depends **only on whether the current node buys**, not on the grandparent.

4. This naturally suggests **Tree Dynamic Programming**.

5. Budget constraints introduce a **knapsack-style DP** at each node.

---

## **Core Idea – Tree DP with Knapsack**

We process the tree using **DFS**, and for each node `u`, we compute two DP arrays:

```
dp0[b] = maximum profit with budget b
         when parent of u is NOT bought

dp1[b] = maximum profit with budget b
         when parent of u IS bought
```

These arrays fully describe the optimal choices in the subtree rooted at `u`.

---

## **DP State Breakdown**

For a node `u`, there are **two independent decisions**:

1. **Whether `u` is bought**
2. **How the budget is distributed among its children**

### Step 1: Merge Children (Group Knapsack)

We first compute an intermediate DP:

```
sub[u_buy][b]
```

* `u_buy = 0`: u is NOT bought
* `u_buy = 1`: u IS bought
* `b`: total budget spent on all children

Each child subtree is treated as a **group** in a group-knapsack:

* If `u` is bought → child can use `dp1`
* If `u` is not bought → child must use `dp0`

---

### Step 2: Decide Whether to Buy `u`

After merging all children:

* If parent of `u` is **not bought**:

  * Buying `u` costs `present[u]`
* If parent of `u` **is bought**:

  * Buying `u` costs `floor(present[u] / 2)`

Profit is always:

```
future[u] − buying_price
```

We update `dp0` and `dp1` accordingly.

---

## **Why This Is Tricky (Common Pitfalls)**

This problem is hard because of **state semantics**:

###  Common Mistakes

1. Mixing up:

   * “parent is bought”
   * “current node is bought”

2. Allowing discount propagation beyond one level

3. Forcing or forbidding negative-profit nodes incorrectly
   (Negative profit nodes may still be optimal if they unlock large discounts downstream.)

###  Correct Rule

> Discounts propagate **only one level down**,
> and DP states must strictly separate:
>
> * parent decision
> * current node decision
> * child decisions

---

## **Algorithm Steps**

1. Build the tree from the hierarchy
2. Run DFS from the root
3. At each node:

   * Merge children using group knapsack
   * Decide whether to buy the current node
4. The final answer is:

   ```
   max(dp0[b]) for the root
   ```

   (The root has no parent, so no discount applies.)

---

## **Complexity Analysis**

* **Time Complexity:**
  [
  O(n \times budget^2)
  ]

  * `n` nodes
  * Knapsack merge per node

* **Space Complexity:**
  [
  O(n \times budget)
  ]

  * DP arrays for recursion

Given constraints (`n ≤ 160`, `budget ≤ 160`), this is acceptable.

---

## **What I Learned from This Problem**

* How to correctly model **discount propagation on trees**
* How to combine **Tree DP** with **Group Knapsack**
* Why DP state semantics matter more than formulas
* How negative-profit decisions can still be globally optimal

This is a classic example of a **high-quality Hard DP problem** where correctness depends on **precise state definitions**, not just coding skill.
