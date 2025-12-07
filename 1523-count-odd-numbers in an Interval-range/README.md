# **LeetCode 1523 – Count Odd Numbers in an Interval Range**

**Difficulty:** Easy  
**Tags:** Math  
**Link:** [https://leetcode.com/problems/count-odd-numbers-in-an-interval-range/](https://leetcode.com/problems/count-odd-numbers-in-an-interval-range/)

---

## **Problem Summary**

Given two integers `low` and `high`, return the number of **odd integers** within the inclusive interval:

```
[low, high]
```

Example:
`low = 3`, `high = 7` → odd numbers are `[3, 5, 7]` → result is `3`.

---

## **Key Insight**

The naive approach—looping from `low` to `high` and checking each number—fails for large ranges (up to `10^9`).
We need a **mathematical** O(1) solution.

### ✔ Count of odd numbers from 0 to x:

$$
\left\lfloor \frac{x + 1}{2} \right\rfloor
$$

### ✔ Therefore, number of odds in the interval ([low, high]):

$$
\text{odds in [low, high]} =
\frac{high + 1}{2} - \frac{low}{2}
$$

This computes the answer in **constant time**, with no loops.

---

## **Approach**

### **1. Count odds from 0 to high**

We use:

$$
\left\lfloor \frac{high + 1}{2} \right\rfloor
$$

This counts all odd numbers up to `high`.

---

### **2. Count odds from 0 to low − 1**

We use:

$$
\left\lfloor \frac{low}{2} \right\rfloor
$$

This automatically excludes `low` itself, whether it is odd or even.

---

### **3. Subtract results**

Final result:

$$
(high + 1) // 2 - (low // 2)
$$

---

## **Example Walkthrough**

### Example 1

```
Input: low = 3, high = 7
```

```
Odds up to 7: (7 + 1) // 2 = 4     → [1, 3, 5, 7]
Odds up to 2: 3 // 2 = 1           → [1]
```

```
4 - 1 = 3
```

---

### Example 2

```
Input: low = 8, high = 10
```

```
Odds up to 10: (10 + 1) // 2 = 5   → [1, 3, 5, 7, 9]
Odds up to 7: 8 // 2 = 4           → [1, 3, 5, 7]
```

```
5 - 4 = 1
```

---

## **Why This Works**

* Odd numbers appear every 2 steps: 1, 3, 5, 7, …
* Integer division naturally counts how many such values exist in a range.
* This converts a potentially huge iteration into a simple formula.
* Runs in **O(1)** time and **O(1)** space.

---

## **Complexity Analysis**

| Operation | Complexity |
| --------- | ---------- |
| Time      | **O(1)**   |
| Space     | **O(1)**   |

This is the optimal solution.

---

## **What I Learned**

* How parity-based problems can often be solved using integer patterns instead of loops.
* Why interval problems can be computed using prefix-style counting (`count(0..high) − count(0..low−1)`).
* How mathematical reasoning avoids time-limit exceed in large input ranges.

告诉我即可！
