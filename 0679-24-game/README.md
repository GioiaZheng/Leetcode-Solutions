# **LeetCode 679 – 24 Game**

**Difficulty:** Hard  
**Tags:** Backtracking, DFS, Math  
**Link:** https://leetcode.com/problems/24-game/

---

## **Problem Summary**

You are given **4 cards**, each with an integer value between **1 and 9**.

Your goal is to determine whether it is possible to **use all four numbers exactly once**, together with:

- Arithmetic operators: `+  -  *  /`
- Parentheses `(` `)`

to form an expression that evaluates to **24**.

---

### **Rules & Constraints**

- Division `/` is **real division**
- Every operation must be **binary** (no unary minus)
- **No concatenation** of numbers
- Each card must be used **exactly once**
- Floating-point results are allowed

---

## **Key Insight**

This is a **pure search problem**.

The number of cards is fixed (**4**), so we can:

> **Try all possible ways to combine two numbers at a time using the four operators, reduce the problem size, and recurse.**

This naturally leads to a **DFS + Backtracking** solution.

---

## **Core Idea**

At each step:

1. Pick **two distinct numbers** `a` and `b`
2. Combine them using all valid operations:
   - `a + b`
   - `a - b`, `b - a`
   - `a * b`
   - `a / b`, `b / a` (if divisor ≠ 0)
3. Replace `a` and `b` with the result
4. Recurse on the new list

When only **one number remains**, check if it is approximately **24**.

---

## **Why Floating-Point Tolerance Is Needed**

Division creates floating-point values.

So instead of checking:
```

value == 24

```

we check:
```

|value - 24| < 1e-6

````

This avoids precision errors.

---

## **Approach**

### Step 1: Convert to Floats
Convert all numbers to `float` to support real division.

---

### Step 2: DFS + Backtracking

- If only one number remains → check if it equals 24
- Otherwise:
  - Try all ordered pairs `(a, b)`
  - Try all operations
  - Recurse with the reduced list
  - Backtrack if unsuccessful

## **Example**

### Example 1

```
Input: [4,1,8,7]
Output: true
```

Explanation:

```
(8 - 4) * (7 - 1) = 24
```

---

### Example 2

```
Input: [1,2,1,2]
Output: false
```

No valid expression evaluates to 24.

---

## **Why This Works**

* Total state space is very small
* All valid expressions are explored
* Backtracking avoids unnecessary work
* Floating-point tolerance ensures correctness

---

## **Complexity Analysis**

Since the number of cards is fixed:

| Aspect | Complexity                |
| ------ | ------------------------- |
| Time   | **O(1)** (bounded search) |
| Space  | **O(1)**                  |

---

## **What I Learned**

* How to systematically explore all arithmetic expressions
* Handling non-commutative operations (`-` and `/`)
* Managing floating-point precision safely
* Designing DFS with clean backtracking

---

## **Related Problems**

* 282. Expression Add Operators
* 241. Different Ways to Add Parentheses
* 772. Basic Calculator III

---

## **One-Line Interview Summary**

> “Use DFS and backtracking to try all pairwise combinations of numbers with four arithmetic operations until checking whether 24 can be reached within floating-point tolerance.”
