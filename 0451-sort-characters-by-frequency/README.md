# **LeetCode 451 – Sort Characters by Frequency**

**Difficulty:** Medium  
**Tags:** Hash Table, String, Sorting, Heap  
**Link:** [https://leetcode.com/problems/sort-characters-by-frequency/](https://leetcode.com/problems/sort-characters-by-frequency/)

---

## **Problem Summary**

Given a string `s`, return a new string where its characters are sorted in **descending order by frequency**.
Characters that appear more often should come earlier in the output.
If two characters have the same frequency, their relative order does not matter.

---

## **Key Insight**

The problem is essentially:

1. Count how many times each character appears.
2. Sort characters based on these frequencies.
3. Reconstruct the string accordingly.

A frequency map is required, and sorting by frequency produces the final ordering.

This is not about lexicographical order; the value being sorted is the **count**, not the character itself.

---

## **Approach**

1. Create a frequency map:

   ```
   character → count
   ```
2. Extract all characters into a list.
3. Sort the list by frequency in descending order.
4. Rebuild the output string by repeating each character according to its count.
5. Return the final concatenated string.

This approach guarantees that more frequent characters appear earlier.

---

## **Example**

**Input**

```
s = "tree"
```

**Explanation**

* `'e'` appears twice
* `'t'` and `'r'` appear once
  A valid output is `"eetr"`.

**Output**

```
"eetr"
```

---

## **Why This Works**

The sorting step ensures that characters are ordered by decreasing frequency.
Since no specific tie-breaking rule is required, any stable or unstable sort is acceptable.

The frequency map provides a complete summary of the input string, making reconstruction straightforward.

---

## **Complexity**

* **Time:** `O(n log n)` due to sorting
* **Space:** `O(n)` for storing the frequency map and the output string

---

## **What I Learned**

* How counting-based problems reduce naturally to sorting tasks.
* Why decoupling “character value” from “frequency” is essential in ranked-string problems.
* How histogram construction enables reconstruction of a sorted output.
