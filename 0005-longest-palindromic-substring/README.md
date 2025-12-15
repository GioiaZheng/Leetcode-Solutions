# **LeetCode 5 – Longest Palindromic Substring**

**Difficulty:** Medium  
**Tags:** String, Two Pointers, Expand Around Center  
**Link:** [https://leetcode.com/problems/longest-palindromic-substring/](https://leetcode.com/problems/longest-palindromic-substring/)

---

## **Problem Summary**

You are given a string `s` consisting of digits and English letters.

A **palindromic substring** is a contiguous substring that reads the same forward and backward.

Your task is to return the **longest palindromic substring** in `s`.

If multiple answers exist, returning any one of them is acceptable.

---

## **Key Insight**

A palindrome is symmetric around its **center**.

There are only two possible types of palindrome centers:

1. **Odd-length palindromes**

   * Centered at a single character
   * Example: `"aba"`

2. **Even-length palindromes**

   * Centered between two characters
   * Example: `"bb"`

Instead of checking all substrings, we can **expand outward from each possible center** and keep track of the longest palindrome found.

This reduces the problem to:

> For each index `i`, expand around
>
> * `(i, i)` → odd-length palindromes
> * `(i, i+1)` → even-length palindromes

---

## **Approach**

We iterate through the string and treat each position as a potential center.

### Steps:

1. For each index `i`, expand around:

   * `(i, i)` to handle odd-length palindromes
   * `(i, i + 1)` to handle even-length palindromes
2. For each expansion, compute the maximum palindrome length.
3. Keep track of the longest palindrome using two pointers `start` and `end`.
4. Return the substring defined by `[start, end]`.

---

## **Example Walkthrough**

### **Input**

```
s = "babad"
```

### **Key expansions**

* Center at `'b'` → `"bab"`
* Center at `'a'` → `"aba"`

Both have length `3`, so either result is valid.

### **Output**

```
"bab"
```

---

### **Input**

```
s = "cbbd"
```

### **Key expansion**

* Center between `'b'` and `'b'` → `"bb"`

### **Output**

```
"bb"
```

---

## **Why This Works**

For any palindrome substring, there exists a center from which the palindrome can be fully expanded.

By checking **both odd and even centers**, we ensure that:

* No valid palindrome is missed
* Each expansion is performed efficiently
* Each palindrome is checked in linear time relative to its length

Although we expand from each index, the total time remains acceptable due to the constraint `n ≤ 1000`.

---

## **Complexity Analysis**

* **Time Complexity:** `O(n²)`

  * Each character can expand outward at most `n` times
* **Space Complexity:** `O(1)`

  * Only constant extra space is used

---

## **What I Learned**

* Why palindromes must be checked using center expansion
* The importance of handling both odd and even-length cases
* How to update substring boundaries without slicing repeatedly
* How two-pointer techniques apply naturally to string symmetry problems
