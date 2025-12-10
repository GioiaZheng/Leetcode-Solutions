# **LeetCode 49 – Group Anagrams**

**Difficulty:** Medium  
**Tags:** Array, Hash Table, String  
**Link:** [https://leetcode.com/problems/group-anagrams/](https://leetcode.com/problems/group-anagrams/)

---

## **Problem Summary**

You are given an array of strings.
Your task is to group the strings into collections where each group consists of strings that are **anagrams** of one another.

Two strings are anagrams if they contain the same characters with identical frequencies, regardless of order.

The output should be a list of groups, where each group contains all strings belonging to the same anagram class.

---

## **Key Insight**

Two strings are anagrams if and only if they share the same **canonical representation**.
Common canonical forms include:

1. Sorting the characters in the string
2. Building a character-frequency signature

For example:

* `"eat"` → `"aet"`
* `"tea"` → `"aet"`
* `"tan"` → `"ant"`

Thus, grouping strings by their canonical forms naturally produces sets of anagrams.

A hash map allows efficient grouping by mapping:

```
canonical_form → list of strings
```

---

## **Approach**

1. Create an empty hash map.
2. For each word:

   * Compute its canonical representation.
     (Most commonly, sort the string.)
   * Insert the word into the hash map under its canonical key.
3. After processing all strings, the values of the hash map represent the anagram groups.
4. Return all groups.

This approach ensures that all words sharing the same canonical form end up in the same group.

---

## **Example**

**Input**

```
["eat", "tea", "tan", "ate", "nat", "bat"]
```

**Explanation**
The strings group by sorted canonical forms:

* `"aet"` → `["eat", "tea", "ate"]`
* `"ant"` → `["tan", "nat"]`
* `"abt"` → `["bat"]`

**Output**

```
[["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]
```

---

## **Why This Works**

The set of characters in a string, together with their counts, uniquely identifies an anagram class.
Sorting the characters provides a simple and deterministic canonical form.

Using the canonical representation as a hash key ensures:

* All true anagrams map to the same bucket
* No non-anagrams can appear in the same group

This converts what seems like a pairwise comparison problem into a classification problem based on hashing.

---

## **Complexity**

Using sorting as the canonical form:

* **Time:** `O(n * k log k)`
  where `n` is the number of strings and `k` is the maximum string length
* **Space:** `O(n * k)` for storing grouped strings

Using character frequency counting instead of sorting improves the canonical computation to `O(k)`.

---

## **What I Learned**

* How canonical representations simplify grouping tasks.
* Why hashing enables efficient classification of objects by structural similarity.
* How string anagram relationships reduce to frequency analysis or sorting.
