# **LeetCode 242 – Valid Anagram**

**Difficulty:** Easy  
**Tags:** Hash Table, String, Sorting  
**Link:** https://leetcode.com/problems/valid-anagram/

---

## **Problem Summary**

Given two strings `s` and `t`, determine whether `t` is an **anagram** of `s`.

Two strings are anagrams if they contain exactly the same characters with the same frequencies, but possibly in a different order.

---

## **Key Insight**

Two strings are anagrams if and only if:

1. They have the **same length**, and
2. They have **identical character frequency distributions**.

This can be checked using:

* Sorting both strings and comparing the results, or
* Counting characters using a hash table (more efficient).

---

## **Approach**

1. If the lengths of `s` and `t` differ, they cannot be anagrams.
2. Count the frequency of each character in both strings.
3. Compare the two frequency maps.
4. If all counts match, the strings are anagrams.

Sorting-based comparison is also valid:

* Sort `s`, sort `t`, and compare the sorted strings.

---

## **Example**

**Input**

```
s = "anagram"
t = "nagaram"
```

**Explanation**
Both strings contain the same characters with the same counts.

**Output**

```
true
```

---

## **Why This Works**

An anagram must preserve both:

* Total number of characters, and
* Frequency of each distinct character.

If any character appears a different number of times, or one string has characters the other does not, the strings cannot be anagrams.

This makes frequency comparison both necessary and sufficient.

---

## **Complexity**

Using hash maps:

* **Time:** `O(n)`
* **Space:** `O(1)` if limited to lowercase letters; otherwise `O(k)`

Using sorting:

* **Time:** `O(n log n)`
* **Space:** `O(1)` or `O(n)` depending on sorting implementation

---

## **What I Learned**

* How to characterize anagrams using frequency equality.
* How sorting provides a simple but less efficient alternative.
* How hash maps allow linear-time comparison of character distributions.
