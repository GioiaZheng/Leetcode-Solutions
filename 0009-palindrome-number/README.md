# **LeetCode 9 – Palindrome Number**

**Difficulty:** Easy  
**Tags:** Math  
**Link:** [https://leetcode.com/problems/palindrome-number/](https://leetcode.com/problems/palindrome-number/)

---

## **Problem Summary**

You are given an integer `x`.

Return `true` if `x` is a **palindrome**, and `false` otherwise.

A palindrome number reads the **same forward and backward**.

---

## **Key Insight**

* **Negative numbers** are never palindromes:

  * `-121` reversed becomes `121-`
* Numbers ending with `0` (except `0` itself) are not palindromes:

  * `10` → `01`
* To avoid converting the number to a string, we can:

  * **Reverse only half of the number**
  * Compare the two halves

This avoids overflow and unnecessary computation.

---

## **Approach**

1. If `x < 0`, return `false`.
2. If `x` ends with `0` and `x != 0`, return `false`.
3. Initialize `reversed_half = 0`.
4. While `x > reversed_half`:

   * Extract the last digit of `x`
   * Append it to `reversed_half`
   * Remove the last digit from `x`
5. Compare:

   * `x == reversed_half` (even number of digits)
   * `x == reversed_half // 10` (odd number of digits)

---

## **Example**

### Example 1

```
Input: x = 121
Output: true
```

---

### Example 2

```
Input: x = -121
Output: false
```

---

### Example 3

```
Input: x = 10
Output: false
```

---

## **Why This Works**

* Only **half of the digits** are reversed.
* No string conversion is used.
* Overflow is impossible because we stop at half.
* Handles both even- and odd-length numbers cleanly.

---

## **Complexity**

| Aspect | Complexity     |
| ------ | -------------- |
| Time   | **O(log10 n)** |
| Space  | **O(1)**       |

---

## **What I Learned**

* How to check palindromes using pure arithmetic.
* Why reversing the entire number is unnecessary.
* How early exits simplify logic and improve performance.
* A common interview pattern for numeric palindrome problems.
