# **LeetCode 1925 – Count Square Sum Triples**

**Difficulty:** Easy  
**Tags:** Math, Number Theory  
**Link:** [https://leetcode.com/problems/count-square-sum-triples/](https://leetcode.com/problems/count-square-sum-triples/)

---

## **Problem Summary**

A **square triple** is a triple `(a, b, c)` of positive integers such that:

$$
a^2 + b^2 = c^2
$$

Given an integer `n`, return the number of square triples satisfying:

$$
1 \le a, b, c \le n
$$

Note: Triples `(a, b, c)` and `(b, a, c)` are treated as **different** because the order matters.

---

## **Key Insight**

A brute-force solution checks all possible `(a, b, c)` combinations using **three nested loops**, which results in:

[
O(n^3)
]

This is too slow for `n = 250`.

---

### ✔ Optimization via Math

We can eliminate the third loop by solving for `c` directly:

$$
c = \sqrt{a^2 + b^2}
$$

If:

1. `c` is an integer
2. `c ≤ n`

then `(a, b, c)` is a valid square triple.

This reduces the complexity to:

[
O(n^2)
]

---

## **Approach**

### **1. Loop over all values of a and b**

Both `a` and `b` run from `1` to `n`.

### **2. Compute the only possible c**

$$
c = \sqrt{a^2 + b^2}
$$

We cast it to `int` before checking.

### **3. Check if c is a valid integer**

A perfect square condition:

$$
c^2 = a^2 + b^2
$$

### **4. Ensure c is within range**

$$
c \le n
$$

### **5. Count the triple**

Since `(a, b, c)` and `(b, a, c)` are both valid, we allow all pair permutations.

---

## **Example**

### Example 1

```
Input: n = 5
Output: 2
```

Valid triples:

* (3, 4, 5)
* (4, 3, 5)

---

### Example 2

```
Input: n = 10
Output: 4
```

Valid triples:

* (3, 4, 5)
* (4, 3, 5)
* (6, 8, 10)
* (8, 6, 10)

---

## **Why This Works**

* We compute `c` directly instead of testing all possible values.
* Checking whether a number is a perfect square is extremely fast.
* The order of `(a, b)` matters, matching the problem's definition.
* The approach runs comfortably within limits for `n ≤ 250`.

---

## **Complexity**

| Aspect | Complexity |
| ------ | ---------- |
| Time   | **O(n²)**  |
| Space  | **O(1)**   |

This is optimal for the constraints.

---

## **What I Learned**

* How mathematical transformation reduces algorithmic complexity.
* Why eliminating loops dramatically improves performance.
* How to detect perfect squares efficiently using integer arithmetic.
* The importance of understanding problem constraints—order matters.
