# **LeetCode 13 – Roman to Integer**

**Difficulty:** Easy  
**Tags:** Hash Table, Math, String  
**Link:** [https://leetcode.com/problems/roman-to-integer/](https://leetcode.com/problems/roman-to-integer/)

---

## **Problem Summary**

You are given a Roman numeral string `s`, representing an integer in the range `[1, 3999]`.

Roman numerals are composed of the following symbols:

| Symbol | Value |
| ------ | ----- |
| I      | 1     |
| V      | 5     |
| X      | 10    |
| L      | 50    |
| C      | 100   |
| D      | 500   |
| M      | 1000  |

Your task is to **convert the Roman numeral into its corresponding integer value**.

The input is guaranteed to be a **valid Roman numeral**.

---

## **Key Insight**

* Roman numerals are usually written from **largest to smallest**, left to right.
* However, in **subtractive cases**, a smaller value appears before a larger one:

  * IV (4), IX (9)
  * XL (40), XC (90)
  * CD (400), CM (900)

The key rule:

> If a symbol has a **smaller value than the symbol immediately after it**,
> then its value should be **subtracted**, otherwise **added**.

---

## **Approach**

1. Create a mapping from Roman symbols to integer values.
2. Traverse the string from left to right.
3. For each character:

   * If the next character exists and has a **larger value**, subtract the current value.
   * Otherwise, add the current value.
4. Accumulate the total and return it.

---

## **Example**

### Example 1

```
Input: s = "III"
Output: 3
```

Explanation:

```
1 + 1 + 1 = 3
```

---

### Example 2

```
Input: s = "LVIII"
Output: 58
```

Explanation:

```
50 + 5 + 1 + 1 + 1 = 58
```

---

### Example 3

```
Input: s = "MCMXCIV"
Output: 1994
```

Explanation:

```
M  = +1000
C  = -100   (before M)
M  = +1000
X  = -10    (before C)
C  = +100
I  = -1     (before V)
V  = +5
----------------
Total = 1994
```

---

## **Why This Works**

* Roman numerals follow a strict local comparison rule.
* Each symbol’s contribution depends only on its **immediate neighbor**.
* A single linear scan is sufficient.
* The problem guarantees valid input, so no extra validation is needed.

---

## **Complexity**

| Aspect | Complexity |
| ------ | ---------- |
| Time   | **O(n)**   |
| Space  | **O(1)**   |

Where `n` is the length of the Roman numeral string.

---

## **What I Learned**

* How to handle subtractive notation cleanly.
* Why local comparisons can simplify parsing problems.
* How to translate a rule-based numeral system into linear logic.
* A perfect counterpart to the “Integer to Roman” problem.

---

###  Notes

This problem pairs naturally with:

* **12. Integer to Roman**

Together, they form a complete **bidirectional conversion** example.

---

## **One-Line Interview Summary**

> “Scan left to right; subtract a symbol if it’s smaller than the next one, otherwise add it.”
