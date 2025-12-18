# **LeetCode 8 – String to Integer (atoi)**

**Difficulty:** Medium  
**Tags:** String, Parsing  
**Link:** [https://leetcode.com/problems/string-to-integer-atoi/](https://leetcode.com/problems/string-to-integer-atoi/)

---

## **Problem Summary**

You are given a string `s` and must convert it into a **32-bit signed integer**.

The conversion follows these rules:

1. Ignore any **leading whitespace**.
2. Determine the **sign** (`+` or `-`), if present.
3. Read digits until a **non-digit character** is encountered.
4. If no digits are read, return `0`.
5. If the result exceeds the 32-bit signed integer range:

```
[-2^31, 2^31 - 1]
```

clamp it to the nearest bound.

---

## **Key Insight**

* The string must be processed **character by character**.
* Only **one optional sign** is allowed, and it must appear **before digits**.
* Parsing stops immediately when a non-digit character is encountered.
* Overflow must be checked **before multiplying by 10**.

The core operation during parsing is:

```text
result = result * 10 + digit
```

but only if it stays within the valid integer range.

---

## **Approach**

1. Skip all leading whitespace characters.
2. Check for an optional `'+'` or `'-'` sign.
3. Initialize `result = 0`.
4. While the current character is a digit:

   * Convert it to an integer.
   * Check for overflow **before** updating `result`.
   * Append the digit to `result`.
5. Apply the sign.
6. Return the final value.

---

## **Example**

### Example 1

```
Input: s = "42"
Output: 42
```

---

### Example 2

```
Input: s = "   -042"
Output: -42
```

---

### Example 3

```
Input: s = "1337c0d3"
Output: 1337
```

---

### Example 4

```
Input: s = "0-1"
Output: 0
```

---

### Example 5

```
Input: s = "words and 987"
Output: 0
```

---

## **Why This Works**

* The string is scanned exactly once.
* Parsing rules are applied in a strict and deterministic order.
* Overflow is prevented **before it happens**, not corrected afterward.
* No built-in integer conversion functions are used.

---

## **Complexity**

| Aspect | Complexity |
| ------ | ---------- |
| Time   | **O(n)**   |
| Space  | **O(1)**   |

---

## **What I Learned**

* How to implement a robust string-to-integer parser.
* Why overflow checks must be done **before multiplication**.
* How to handle malformed input safely.
* How many edge cases can exist in seemingly simple parsing problems.
