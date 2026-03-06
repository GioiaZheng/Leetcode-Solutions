# **LeetCode 1758 – Minimum Changes To Make Alternating Binary String**

**Difficulty:** Easy
**Tags:** String, Greedy
**Link:** [https://leetcode.com/problems/minimum-changes-to-make-alternating-binary-string/](https://leetcode.com/problems/minimum-changes-to-make-alternating-binary-string/)

---

## **Problem Summary**

You are given a binary string `s` consisting only of `'0'` and `'1'`.

In one operation, you can **flip any character**:

* `'0' → '1'`
* `'1' → '0'`

A string is **alternating** if **no two adjacent characters are the same**.

Return the **minimum number of operations** needed to make `s` alternating.

---

## **Key Insight**

An alternating binary string can only have **two possible patterns**:

```
Pattern A: 010101...
Pattern B: 101010...
```

So the problem becomes:

> Count how many characters must change to match each pattern, and take the minimum.

---

## **Why This Works**

For every index `i`:

* In **Pattern A**:

  * even index → `'0'`
  * odd index → `'1'`

* In **Pattern B**:

  * even index → `'1'`
  * odd index → `'0'`

We compare the current character with the expected character for each pattern and count mismatches.

Each mismatch represents **one operation** (flip).

Finally:

```
answer = min(changes_for_pattern_A, changes_for_pattern_B)
```

---

## **Algorithm**

1. Initialize two counters:

   * `start_with_0`
   * `start_with_1`
2. Traverse the string
3. For each index:

   * Check if it matches pattern `"0101..."`
   * Check if it matches pattern `"1010..."`
4. Count mismatches for both patterns
5. Return the smaller count

---

## **Example**

### Example 1

```
Input: s = "0100"

Pattern A: 0101
           0100
                ↑ mismatch → 1 change

Pattern B: 1010
           0100
           ↑ ↑ ↑ mismatches → 3 changes

Answer: 1
```

---

### Example 2

```
Input: s = "10"

Already alternating

Answer: 0
```

---

### Example 3

```
Input: s = "1111"

Pattern A: 0101
           1111
           ↑   ↑ → 2 changes

Pattern B: 1010
           1111
             ↑   ↑ → 2 changes

Answer: 2
```

---

## **Complexity Analysis**

| Aspect | Complexity |
| ------ | ---------- |
| Time   | **O(n)**   |
| Space  | **O(1)**   |

We scan the string once and use only constant extra space.

---

## **Common Mistakes**

* Trying to flip characters greedily without considering both patterns
* Only checking one alternating pattern (`0101...`)
* Using unnecessary extra arrays

Since only **two valid alternating patterns exist**, checking both is sufficient.

---

## **One-Line Interview Summary**

> “An alternating binary string can only be `0101...` or `1010...`, so count mismatches for both patterns and return the minimum.”
