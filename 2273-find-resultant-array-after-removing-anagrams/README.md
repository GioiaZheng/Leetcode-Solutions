# **LeetCode 2273 – Find Resultant Array After Removing Anagrams**

**Difficulty:** Easy
**Tags:** Array, String, Hashing
**Link:** [https://leetcode.com/problems/find-resultant-array-after-removing-anagrams/](https://leetcode.com/problems/find-resultant-array-after-removing-anagrams/)

---

## **Problem Summary**

You are given an array of words.
You must build a new array by iterating through the list from left to right and removing any word that is an **anagram** of the most recently kept word.

Two words are anagrams if they contain the same characters in any order.

The output should preserve the order of appearance and only keep the first word from each sequence of anagrams.

---

## **Key Insight**

The critical idea is that **only the previous kept word matters**.

* When processing word `i`, compare it only to the most recent word stored in the result.
* If `word[i]` is an anagram of that previous valid word:

  * It should be removed.
* Otherwise:

  * It should be added to the result.

Anagrams can be detected by comparing character frequency signatures or sorted character sequences.

---

## **Approach**

1. Initialize an empty result list.
2. Add the first word to the result.
3. For each subsequent word:

   * Compute its anagram signature (such as sorted characters).
   * Compare it with the signature of the last kept word.
   * If they differ, append the word to the result.
   * Otherwise, skip it.
4. Return the list of kept words.

This ensures that from any consecutive group of anagrams, only the **first** one appears in the final result.

---

## **Example**

**Input**

```
["abba", "baba", "bbaa", "cd", "cd"]
```

**Explanation**

* "abba", "baba", "bbaa" are all anagrams → keep only "abba".
* "cd" and "cd" are anagrams → keep only the first "cd".

**Output**

```
["abba", "cd"]
```

---

## **Why This Works**

Two words are anagrams if and only if:

```
sorted(word1) == sorted(word2)
```

or equivalently, if their character frequency maps match.

Comparing each word only with the last accepted word ensures correctness because earlier words cannot affect future decisions once removed.

This reduces the problem to a simple linear scan.

---

## **Complexity**

* **Time:** `O(n * k log k)` if using sorting,
  where `k` is the maximum word length.
  Can be improved to `O(n * k)` with frequency counts.
* **Space:** `O(k)` for storing signatures.

---

## **What I Learned**

* How anagram detection can be standardized using sorted sequences or frequency mappings.
* How a problem that seems to involve pairwise comparisons can be simplified by checking only the most recent retained element.
* Techniques for filtering sequences based on matching structural properties.
