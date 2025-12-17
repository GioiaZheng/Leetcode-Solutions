# **LeetCode 7 – Reverse Integer**

**Difficulty:** Medium  
**Tags:** Math  
**Link:** [https://leetcode.com/problems/reverse-integer/](https://leetcode.com/problems/reverse-integer/)

---

## **Problem Summary**

You are given a **signed 32-bit integer** `x`.

Your task is to **reverse its digits** and return the reversed integer.

If reversing `x` causes the value to go outside the signed 32-bit integer range:

```
[-2^31, 2^31 - 1]
```

you must return **0**.

Assume the environment does not allow you to store **64-bit integers**, so overflow must be handled manually.

---

## **Key Insight**

* Reversing an integer can be done by **extracting digits one by one**.
* Each step:

  * Take the last digit using modulo (`% 10`)
  * Remove the last digit using integer division (`// 10`)
  * Append it to the reversed number
* The **main difficulty** is preventing overflow **before it happens**.

The core operation is:

```text
rev = rev * 10 + digit
```

---

## **Approach**

1. Determine the sign of the number.
2. Work with the absolute value of `x`.
3. Initialize `rev = 0`.
4. While `x != 0`:

   * Extract the last digit.
   * Remove the last digit from `x`.
   * **Check for overflow** before updating `rev`.
   * Append the digit to `rev`.
5. Restore the original sign.
6. Return the result (or `0` if overflow occurs).

---

## **Overflow Check**

Let:

```python
INT_MAX = 2**31 - 1
INT_MIN = -2**31
```

Before executing:

```python
rev = rev * 10 + digit
```

We must ensure it will not exceed `INT_MAX`.

A safe check is:

```python
rev > INT_MAX // 10
or (rev == INT_MAX // 10 and digit > 7)
```

Because:

```text
INT_MAX = 2147483647
```

---

## **Example**

### Example 1

```
Input: x = 123
Output: 321
```

---

### Example 2

```
Input: x = -123
Output: -321
```

---

### Example 3

```
Input: x = 120
Output: 21
```

---

## **Why This Works**

* Each digit is processed exactly once.
* Overflow is prevented **before it occurs**, respecting the 32-bit constraint.
* The algorithm uses only **constant extra space**.
* No string conversion or 64-bit integers are required.

---

## **Complexity**

| Aspect | Complexity     |
| ------ | -------------- |
| Time   | **O(log10 n)** |
| Space  | **O(1)**       |

---

## **What I Learned**

* How to reverse integers using pure arithmetic operations.
* Why overflow must be checked **before multiplication**.
* How to handle signed integers cleanly.
* How low-level integer constraints affect algorithm design.
