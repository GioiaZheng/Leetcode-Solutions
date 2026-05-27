# LeetCode 242 – Valid Anagram
**Difficulty:** Easy 
**Tags:** Hash Table, String, Sorting 
**Link:** https://leetcode.com/problems/valid-anagram/

---

## Problem Summary
Given two strings `s` and `t`, determine whether `t` is an **anagram** of `s`.

Two strings are anagrams if they contain exactly the same characters with the same frequencies, but possibly in a different order.

---

## Key Insight
Two strings are anagrams if and only if:

1. They have the **same length**, and
2. They have **identical character frequency distributions**.

This can be checked using:

* Sorting both strings and comparing the results, or
* Counting characters using a hash table (more efficient).

---

## Approach
1. If the lengths of `s` and `t` differ, they cannot be anagrams.
2. Count the frequency of each character in both strings.
3. Compare the two frequency maps.
4. If all counts match, the strings are anagrams.

Sorting-based comparison is also valid:

* Sort `s`, sort `t`, and compare the sorted strings.

---

## Example
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

## Why This Works
An anagram must preserve both:

* Total number of characters, and
* Frequency of each distinct character.

If any character appears a different number of times, or one string has characters the other does not, the strings cannot be anagrams.

This makes frequency comparison both necessary and sufficient.

---

## Complexity
Using hash maps:

* **Time:** `O(n)`
* **Space:** `O(1)` if limited to lowercase letters; otherwise `O(k)`

Using sorting:

* **Time:** `O(n log n)`
* **Space:** `O(1)` or `O(n)` depending on sorting implementation

---

## What I Learned
* How to characterize anagrams using frequency equality.
* How sorting provides a simple but less efficient alternative.
* How hash maps allow linear-time comparison of character distributions.

---

## Solution Files
- `solution.py` is the recommended `Counter` implementation because it compares character frequencies directly in linear time.
- `approaches/solution_sort.py` preserves the sorting-based approach as a simpler but less efficient alternative.

<!--
Sections below are the optional "AI card" extension. The problem
carries `"ai_card_status": "reviewed"` in metadata.json. See
CONTRIBUTING.md section "Optional Problem README Sections (AI Card)".
-->

---

## Brute-force baseline

For each character in `s`, search-and-remove its first occurrence in `t`. After scanning the whole `s`, `t` must be empty for a valid anagram.

- **Time:** `O(n^2)` — each removal is an `O(n)` slice or `index()` call.
- **Space:** `O(n)` for the mutable copy of `t`.

The canonical solutions above improve to `O(n log n)` via sorting or `O(n)` via a frequency map.

---

## Common mistakes

- Skipping the length pre-check. Two strings of different lengths are never anagrams; comparing them with `Counter` works but wastes a full pass when a single `len(s) != len(t)` would reject.
- Using a `set` instead of a frequency counter. `set("aab") == set("abb")` is `True` but the strings are not anagrams. Sets discard multiplicity.
- Hard-coding a 26-element array when the problem's follow-up asks about Unicode inputs. Switch to `collections.Counter` (or a `dict`) for non-ASCII.
- Using `sorted(s) == sorted(t)` and calling it `O(n)`. It is correct but `O(n log n)`; faster `O(n)` approaches exist.

---

## Failure cases

1. **`s = "aab", t = "abb"`** — a set-based check returns `True` (both sets equal `{"a", "b"}`) but counts differ. The frequency map correctly returns `False`.
2. **`s = "ac", t = "bb"`** — same length, totally different characters. A buggy "check first char then early-return" would pass on length; only full frequency comparison rejects.

---

## Interview follow-ups

- *"What if the inputs contain Unicode characters?"* — `collections.Counter` handles Unicode out of the box; the fixed `[26]`-element array trick breaks. Memory becomes `O(σ)` where `σ` is the input's distinct-character count.
- *"Generalise to grouping a list of strings into anagram classes."* → LeetCode 49 (Group Anagrams).
- *"Find all anagrams of `p` as substrings of `s`."* → LeetCode 438 (Find All Anagrams in a String); sliding window over a fixed-size frequency map.
- *"What if `t` arrives as a stream?"* — Pre-count `s`; for each incoming char in `t` decrement and reject on negative; track a running "remaining" count.

---

## Bilingual summary

**English.** Length pre-check, then build a frequency map of `s` and decrement it while scanning `t`; reject on any negative count, accept if all counts land at zero. Sorting is the simpler `O(n log n)` alternative. `O(n)` time, `O(σ)` space where `σ` is the alphabet size.

**中文。** 先比长度，再用频次表统计 `s` 的字符；扫描 `t` 时逐个递减，遇到负值即判定不是 anagram，全部归零则相等。排序版本更简洁但慢一档（`O(n log n)`）。时间 `O(n)`，空间 `O(σ)`，σ 为字母表大小。
