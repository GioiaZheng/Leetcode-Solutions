# **LeetCode 12 – Integer to Roman**

**Difficulty:** Medium  
**Tags:** Math, String, Greedy  
**Link:** [https://leetcode.com/problems/integer-to-roman/](https://leetcode.com/problems/integer-to-roman/)

---

## **Problem Summary**

You are given an integer `num` (1 ≤ num ≤ 3999).

Your task is to convert it into a **Roman numeral string** following standard Roman numeral rules:

* Roman numerals are constructed from **largest value to smallest**
* Certain values use **subtractive notation** (e.g. 4 = IV, 9 = IX)
* Only specific subtractive pairs are allowed
* Symbols `I`, `X`, `C`, `M` can repeat at most **three times consecutively**

---

## **Roman Symbols**

| Symbol | Value |
| ------ | ----- |
| I      | 1     |
| V      | 5     |
| X      | 10    |
| L      | 50    |
| C      | 100   |
| D      | 500   |
| M      | 1000  |

Allowed subtractive forms:

* IV (4), IX (9)
* XL (40), XC (90)
* CD (400), CM (900)

---

## **Key Insight**

* Roman numerals can be generated **greedily**.
* Always subtract the **largest possible Roman value** from the remaining number.
* By including subtractive values directly in the mapping, we avoid special-case logic.
* The greedy approach is guaranteed to work due to the problem’s constraints.

---

## **Approach**

1. Prepare an ordered list of `(value, symbol)` pairs:

   * From largest to smallest
   * Include subtractive values (900, 400, 90, etc.)
2. Initialize an empty result string.
3. While `num > 0`:

   * Find the largest value `v` ≤ `num`
   * Append its Roman symbol
   * Subtract `v` from `num`
4. Continue until `num` becomes 0.

---

## **Example**

### Example 1

```
Input: num = 3749
Output: "MMMDCCXLIX"
```

Breakdown:

```
3000 → MMM
 700 → DCC
  40 → XL
   9 → IX
```

---

### Example 2

```
Input: num = 58
Output: "LVIII"
```

---

### Example 3

```
Input: num = 1994
Output: "MCMXCIV"
```

---

## **Why This Works**

* Roman numeral rules are inherently **greedy**
* Subtractive cases are finite and explicitly listed
* Each step reduces `num`, guaranteeing termination
* The constraints ensure the mapping is complete and safe

---

## **Complexity**

| Aspect | Complexity |
| ------ | ---------- |
| Time   | **O(1)**   |
| Space  | **O(1)**   |

Explanation:

* Roman numerals have a fixed maximum length
* The number of symbols processed is constant

---

## **What I Learned**

* How greedy algorithms can simplify rule-based conversions
* Why explicitly encoding edge cases is often cleaner than branching logic
* How to model a real-world numeral system with a deterministic algorithm

---

###  Notes

This is a **classic greedy + mapping problem** and frequently appears in interviews.

Understanding this problem helps with:

* Number representation
* Encoding systems
* Greedy decision-making

---

## **One-Line Interview Summary**

> “Convert the number greedily by repeatedly subtracting the largest possible Roman value.”
