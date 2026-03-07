# **LeetCode 1888 – Minimum Number of Flips to Make the Binary String Alternating**

**Difficulty:** Medium  
**Tags:** Sliding Window, String, Greedy  
**Link:** [https://leetcode.com/problems/minimum-number-of-flips-to-make-the-binary-string-alternating/](https://leetcode.com/problems/minimum-number-of-flips-to-make-the-binary-string-alternating/)

---

## **Problem Summary**

You are given a binary string `s`.

You can perform two types of operations:

1. **Type-1:** Remove the first character of the string and append it to the end
   (this is equivalent to a **rotation**).
2. **Type-2:** Flip any character (`0 → 1` or `1 → 0`).

A string is **alternating** if no two adjacent characters are the same.

Your task is to compute the **minimum number of flips (Type-2 operations)** needed so that **some rotation of `s` becomes an alternating string**.

---

## **Key Insight**

There are only **two valid alternating patterns** for a binary string:

```
Pattern A: 010101...
Pattern B: 101010...
```

The difficulty comes from **Type-1 operations**, which allow the string to be **rotated any number of times**.

Instead of simulating rotations explicitly, we can use a trick:

> Concatenate the string with itself and examine every window of length `n`.

This allows us to represent every possible rotation.

```
s = "111000"
ss = "111000111000"
```

Each length-`n` window in `ss` corresponds to one rotation of `s`.

---

## **Even vs Odd Length Observation**

### Even Length

If `n` is even, rotating the string **does not change the parity positions**.

That means the optimal answer is simply:

* mismatches with `"0101..."`
* mismatches with `"1010..."`

Take the minimum.

---

### Odd Length

If `n` is odd, rotations **shift parity positions**, meaning the pattern alignment changes.

Therefore we must check **all rotations**.

We achieve this using:

* `ss = s + s`
* A **sliding window of length `n`**
* Count mismatches against both alternating patterns.

---

## **Algorithm**

1. Let `n = len(s)`
2. Construct `ss = s + s`
3. Maintain mismatch counters for:

   * `"010101..."`
   * `"101010..."`
4. Use a **sliding window of size `n`** across `ss`
5. Update mismatch counts when the window moves
6. Track the minimum flips needed.

---

## **Example**

### Example 1

```
Input: s = "111000"

Possible rotation:
"100011"

Target pattern:
"101010"

Flips needed:
2
```

Output:

```
2
```

---

### Example 2

```
Input: s = "010"

Already alternating.
```

Output:

```
0
```

---

### Example 3

```
Input: s = "1110"

Best transformation:
1110 → 1010
```

Output:

```
1
```

---

## **Complexity Analysis**

| Aspect | Complexity |
| ------ | ---------- |
| Time   | **O(n)**   |
| Space  | **O(n)**   |

* The sliding window scans `2n` characters once.
* Only constant additional tracking variables are used.

---

## **Common Mistakes**

* Actually rotating the string `n` times (`O(n²)`)
* Checking only the original string
* Forgetting there are **two alternating patterns**

Using **string doubling + sliding window** efficiently checks every rotation.

---

## **One-Line Interview Summary**

> Double the string to simulate rotations and use a sliding window to count mismatches against the two alternating patterns.
