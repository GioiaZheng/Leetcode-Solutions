# **LeetCode 1411 – Number of Ways to Paint N × 3 Grid**

**Difficulty:** Hard  
**Tags:** Dynamic Programming, Combinatorics  
**Link:** [https://leetcode.com/problems/number-of-ways-to-paint-n-3-grid/](https://leetcode.com/problems/number-of-ways-to-paint-n-3-grid/)

---

## **Problem Summary**

You are given a grid of size `n × 3`.

You want to paint each cell using **exactly one** of three colors:

* Red
* Yellow
* Green

Rules:

* No two **adjacent cells** (horizontally or vertically) can have the same color.
* Return the **number of valid painting ways**.
* The result should be returned modulo `10^9 + 7`.

---

## **Key Insight**

Although the grid has `n` rows, each row has **only two valid color patterns**:

### 1️. ABA pattern (two colors)

```
A B A
```

* First and third cells share the same color
* Middle cell is different

Number of possibilities for one row:

```
3 choices for A × 2 choices for B = 6
```

---

### 2. ABC pattern (three colors)

```
A B C
```

* All three cells have different colors

Number of possibilities for one row:

```
3 × 2 × 1 = 6
```

These are the **only** valid row configurations.

---

## **DP State Definition**

Let:

* `aba` = number of ways where the current row has an **ABA** pattern
* `abc` = number of ways where the current row has an **ABC** pattern

We only need these **two states**.

---

## **DP Transition**

When adding a new row:

```
new_aba = aba * 3 + abc * 2
new_abc = aba * 2 + abc * 2
```

Explanation:

* Each previous pattern can transition to the next row in a **fixed number of valid ways**
* Transitions respect both **horizontal** and **vertical** constraints
* The coefficients (`3`, `2`) come from valid color choices per pattern

---

## **Initialization**

For `n = 1`:

```
aba = 6
abc = 6
```

---

## **Final Answer**

After processing all `n` rows:

```
answer = aba + abc
```

---

## **Example**

### Example 1

```
Input: n = 1
Output: 12
```

Explanation:

```
6 ABA patterns + 6 ABC patterns
```

---

### Example 2

```
Input: n = 5000
Output: 30228214
```

Explanation:

```
Efficient DP with O(n) time handles large n
```

---

## **Why This Works**

* The problem has **huge input size (n ≤ 5000)**.
* Direct grid DP would be too slow.
* Observing that each row reduces to **only two pattern types** drastically simplifies the state space.
* Constant-state DP gives a clean and optimal solution.

---

## **Complexity**

| Aspect | Complexity |
| ------ | ---------- |
| Time   | **O(n)**   |
| Space  | **O(1)**   |

---

## **What I Learned**

* How to reduce a complex grid problem to a small number of states.
* The power of **pattern classification** in DP.
* How combinatorics and DP work together.
* A textbook example of **state compression DP**.

---

###  Notes

This is a **classic Hard DP problem** that often appears in discussions of:

* Grid coloring
* State compression
* Transition counting

Understanding this problem greatly improves DP modeling skills.

---

## **One-Line Interview Summary**

> “Each row has only two valid color patterns (ABA and ABC), so we use constant-state DP with fixed transitions.”
