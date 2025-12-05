# **LeetCode 692 – Top K Frequent Words**

**Difficulty:** Medium
**Tags:** String, Hash Table, Heap, Sorting
**Link:** [https://leetcode.com/problems/top-k-frequent-words/](https://leetcode.com/problems/top-k-frequent-words/)

---

## **Problem Summary**

You are given an array of strings `words` and an integer `k`.
Your task is to return the **k most frequent words**.

The ordering rules are:

1. Words with **higher frequency** appear earlier.
2. If two words have the **same frequency**, the word with **lower lexicographical order** appears earlier.

The result should contain exactly `k` words.

---

## **Key Insight**

This is a frequency-ranking problem with a **tie-breaker**:

* Primary key: frequency (descending)
* Secondary key: lexicographical order (ascending)

A frequency map allows counting occurrences.
Sorting with a custom comparator ensures the correct ordering of results.

The presence of lexicographical comparison means numeric sorting tricks (such as negative frequencies alone) are insufficient; the ordering must consider both dimensions.

---

## **Approach**

1. Build a frequency map:

   ```
   word → count
   ```
2. Extract all unique words.
3. Sort them using the following ordering:

   * By descending frequency
   * If frequencies match, by lexicographical order (ascending)
4. Return the first `k` words of this sorted list.

This ensures all ordering constraints are satisfied.

---

## **Example**

**Input**

```
words = ["i", "love", "leetcode", "i", "love", "coding"]
k = 2
```

**Explanation**

* Frequencies:

  * `"i"` → 2
  * `"love"` → 2
  * `"leetcode"` → 1
  * `"coding"` → 1
* `"i"` and `"love"` both have the highest frequency.
* `"i"` appears before `"love"` lexicographically.

**Output**

```
["i", "love"]
```

---

## **Why This Works**

Word frequency ranking is enabled by hashing.
The lexicographical tiebreaker ensures deterministic ordering for words with equal counts.

Sorting by a composite key:

```
(-frequency, word)
```

captures both constraints cleanly.

This transforms the problem into a straightforward sorting task once the frequency data is computed.

---

## **Complexity**

* **Time:** `O(n log n)` due to sorting
* **Space:** `O(n)` for storing distinct words and their frequencies

---

## **What I Learned**

* How lexical ordering interacts with frequency-based ranking.
* How to construct composite sort keys to enforce multiple ordering constraints.
* Why hash maps paired with sorting provide a flexible toolkit for frequency-analysis problems.
