# LeetCode 5 – Longest Palindromic Substring
**Difficulty:** Medium 
**Tags:** String, Two Pointers, Expand Around Center 
**Link:** [https://leetcode.com/problems/longest-palindromic-substring/](https://leetcode.com/problems/longest-palindromic-substring/)

---

## Problem Summary
You are given a string `s` consisting of digits and English letters.

A **palindromic substring** is a contiguous substring that reads the same forward and backward.

Your task is to return the **longest palindromic substring** in `s`.

If multiple answers exist, returning any one of them is acceptable.

---

## Key Insight
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

## Approach
We iterate through the string and treat each position as a potential center.

### Steps:

1. For each index `i`, expand around:

 * `(i, i)` to handle odd-length palindromes
 * `(i, i + 1)` to handle even-length palindromes
2. For each expansion, compute the maximum palindrome length.
3. Keep track of the longest palindrome using two pointers `start` and `end`.
4. Return the substring defined by `[start, end]`.

---

## Example Walkthrough
### Input
```
s = "babad"
```

### Key expansions
* Center at `'b'` → `"bab"`
* Center at `'a'` → `"aba"`

Both have length `3`, so either result is valid.

### Output
```
"bab"
```

---

### Input
```
s = "cbbd"
```

### Key expansion
* Center between `'b'` and `'b'` → `"bb"`

### Output
```
"bb"
```

---

## Why This Works
For any palindrome substring, there exists a center from which the palindrome can be fully expanded.

By checking **both odd and even centers**, we ensure that:

* No valid palindrome is missed
* Each expansion is performed efficiently
* Each palindrome is checked in linear time relative to its length

Although we expand from each index, the total time remains acceptable due to the constraint `n ≤ 1000`.

---

## Complexity Analysis
* **Time Complexity:** `O(n²)`

 * Each character can expand outward at most `n` times
* **Space Complexity:** `O(1)`

 * Only constant extra space is used

---

## What I Learned
* Why palindromes must be checked using center expansion
* The importance of handling both odd and even-length cases
* How to update substring boundaries without slicing repeatedly
* How two-pointer techniques apply naturally to string symmetry problems

<!--
Sections below are the optional "AI card" extension. The problem
carries `"ai_card_status": "reviewed"` in metadata.json. See
CONTRIBUTING.md section "Optional Problem README Sections (AI Card)".
-->

---

## Brute-force baseline

For every pair `(i, j)` of indices, check whether `s[i..j]` reads the same forward and backward; record the longest palindromic span.

- **Time:** `O(n^3)` — `O(n^2)` pairs, each palindrome check is `O(n)`.
- **Space:** `O(1)`.

The expand-around-center solution above amortises the palindrome check across the expansion, giving `O(n^2)` total work.

---

## Common mistakes

- Handling only odd-length centers `(i, i)` and missing even-length cases like `"bb"`. Must expand from both `(i, i)` AND `(i, i + 1)`.
- Tracking only the maximum length without remembering the start position. Then you cannot slice the answer back out.
- Calling `s[i:j]` inside the inner expansion loop. Each slice is `O(n)`, blowing the runtime from `O(n^2)` to `O(n^3)` and hiding the regression behind apparently-simple code.
- Returning the length instead of the substring (or vice versa). LeetCode 5 asks for the substring; LeetCode 647 (count of palindromic substrings) asks for the count. Different problem signatures.

---

## Failure cases

1. **`s = "ac"`** — every character is a length-1 palindrome; no length-2 palindrome exists. An expansion that forgets to also check the even-center case `(0, 1)` still passes here, but the same bug silently fails on `"aa"` (where `(0, 1)` is the answer).
2. **`s = "babad"`** — both `"bab"` and `"aba"` are valid length-3 answers. An expansion that only checks odd centers returns `"bab"`; one that only checks even centers misses both and returns a length-1 result.
3. **`s = "aacabdkacaa"`** — non-symmetric input where the longest palindrome `"aca"` sits in the middle. Naive substring-slicing inside the expansion turns the call quadratic and times out on long strings.

---

## Interview follow-ups

- *"What if `n` is up to 100,000?"* — Manacher's algorithm: `O(n)` time and space. Transforms the string with separators so odd and even cases unify under a single expansion loop.
- *"Count all palindromic substrings, not just the longest."* → LeetCode 647. Same expand-around-center skeleton, but accumulate the count of valid expansions instead of tracking the longest.
- *"Longest palindromic *subsequence* (non-contiguous)."* → LeetCode 516. Different problem entirely: `O(n^2)` DP on `dp[i][j]` = LPS in `s[i..j]`.
- *"Worst-case input?"* — repeated characters like `"aaaa...a"` make every expansion run the full length, hitting the `O(n^2)` bound. Manacher recovers `O(n)` here.

---

## Bilingual summary

**English.** For each index `i` in `s`, expand outward from two candidate centers — `(i, i)` for odd-length palindromes and `(i, i + 1)` for even-length — tracking the longest palindrome encountered. The expansion is bounded by the palindrome's own length, giving `O(n^2)` total work and `O(1)` extra space.

**中文。** 对每个下标 `i`，分别以 `(i, i)`（奇数长）和 `(i, i + 1)`（偶数长）为中心向外扩展，记录目前最长的回文。每次扩展受回文自身长度约束，总时间 `O(n^2)`，额外空间 `O(1)`。
