# **LeetCode 66 – Plus One**

**Difficulty:** Easy  
**Tags:** Array, Math  
**Link:** [https://leetcode.com/problems/plus-one/](https://leetcode.com/problems/plus-one/)

---

## **Problem Summary**

You are given an integer represented as an array `digits`, where:

* Each element is a single digit (`0–9`)
* The digits are ordered from **most significant to least significant**
* There are **no leading zeros**

Your task is to **increment the integer by one** and return the resulting array of digits.

---

## **Key Insight**

* Adding one starts from the **least significant digit** (the end of the array).
* If a digit is less than `9`, you can increment it and finish.
* If a digit is `9`, it becomes `0` and produces a **carry** to the left.
* If all digits are `9`, an extra digit `1` must be added at the front.

This is exactly how addition works by hand.

---

## **Approach**

1. Traverse the array from right to left.
2. If the current digit is less than `9`:

   * Increment it by `1`
   * Return the array immediately
3. Otherwise (`digit == 9`):

   * Set it to `0` and continue
4. If all digits were `9`, prepend `1` to the array.

---

## **Example**

### Example 1

```
Input: digits = [1,2,3]
Output: [1,2,4]
```

---

### Example 2

```
Input: digits = [4,3,2,1]
Output: [4,3,2,2]
```

---

### Example 3

```
Input: digits = [9]
Output: [1,0]
```

---

## **Why This Works**

* The carry only propagates while digits are `9`.
* As soon as a digit less than `9` is found, the process stops.
* The algorithm mimics elementary addition exactly.
* No conversion to integer is required, avoiding overflow issues.

---

## **Complexity**

| Aspect | Complexity                           |
| ------ | ------------------------------------ |
| Time   | **O(n)**                             |
| Space  | **O(1)** (in-place, ignoring output) |

Where `n = len(digits)`.

---

## **What I Learned**

* How to simulate arithmetic operations on digit arrays.
* Why handling carry correctly is essential.
* A classic example of right-to-left array processing.
* A very common Easy problem that tests attention to edge cases.

---

### Notes

Edge case to remember:

```
[9, 9, 9] → [1, 0, 0, 0]
```

This happens when the carry propagates through all digits.

---

## **One-Line Interview Summary**

> “Traverse digits from right to left, handle carry from 9s, and prepend 1 if needed.”
