# LeetCode 3 – Longest Substring Without Repeating Characters
**Difficulty:** Medium 
**Tags:** Sliding Window, Hash Map, Two Pointers 
**Link:** [https://leetcode.com/problems/longest-substring-without-repeating-characters/](https://leetcode.com/problems/longest-substring-without-repeating-characters/)

---

## Problem Summary
Given a string `s`, the task is to determine the **length** of the longest substring that contains **no repeated characters**.

A substring must consist of **contiguous characters**, unlike a subsequence.

---

## Key Insight
A brute-force solution would check every possible substring, but this leads to `O(n²)` time and is far too slow for inputs as large as `50,000` characters.

The key observation is:

### A valid substring (no duplicates) can be represented by a **sliding window**.

As we move from left to right:

* Add characters to the window until a duplicate appears.
* When a duplicate is encountered, move the **left** pointer just past the previous occurrence.
* Maintain a dictionary mapping each character to its **most recent index**.
* Track the longest window encountered so far.

This ensures each character is processed at most twice (once by `right`, once by `left`), making the solution **O(n)**.

---

## Approach
1. Use a dictionary `last_seen` to record the most recent index of each character.
2. Initialize two pointers:

 * `left` = start of current window
 * `right` = current character being examined
3. For each character `s[right]`:

 * If the character is already in `last_seen` **and** its previous index is inside the window (`>= left`),
 then update:

 ```
 left = last_seen[s[right]] + 1
 ```
 * Update the character’s latest index:

 ```
 last_seen[s[right]] = right
 ```
 * Compute window size:

 ```
 right - left + 1
 ```
 * Update `max_len` accordingly.
4. Return `max_len`.

This maintains a valid window at all times and ensures linear performance.

---

## Example
**Input**

```
s = "pwwkew"
```

**Explanation**

Sliding window evolution:

* `"p"` → length 1
* `"pw"` → length 2
* Duplicate `"w"` encountered → move left past first `"w"`
* Window becomes `"w"`
* Then `"wk"` → `"wke"` → length 3

The longest valid substring is `"wke"` with length **3**.

**Output**

```
3
```

---

## Why This Works
* The sliding window ensures we never reconsider characters outside the active substring.
* The dictionary lets us jump the `left` pointer efficiently to avoid duplicates.
* Each pointer (`left`, `right`) moves only forward, giving a true **O(n)** algorithm.
* The approach carefully distinguishes between duplicates inside and outside the window, ensuring correctness.

---

## Complexity
* **Time:** `O(n)` — Each index visited at most twice
* **Space:** `O(k)` where `k` is the character set size (at most 128 for ASCII)

---

## What I Learned
* How sliding window algorithms convert seemingly quadratic problems into linear ones.
* The importance of tracking the **most recent index** of characters.
* Why moving `left` only forward (never backward) ensures linear time.
* How to maintain window validity with a single data structure (`last_seen`).
* How substring problems differ fundamentally from subsequence problems.

<!--
Sections below are the optional "AI card" extension. The problem
carries `"ai_card_status": "reviewed"` in metadata.json. See
CONTRIBUTING.md section "Optional Problem README Sections (AI Card)".
-->

---

## Brute-force baseline

For every starting index `i`, extend a substring forward while characters stay unique (e.g. with a `set`); record the maximum length.

- **Time:** `O(n^2)` worst case — pathological inputs like `"abcabcabc..."` re-scan most prefixes.
- **Space:** `O(σ)` for the running uniqueness set, where `σ` is the alphabet size.

The sliding-window solution above amortises to `O(n)` total work by never moving `left` backward.

---

## Common mistakes

- Setting `left = last_seen[c] + 1` unconditionally on a duplicate, instead of `left = max(left, last_seen[c] + 1)`. The unguarded form can move `left` **backward** when the previous occurrence is already outside the current window, breaking the "never go back" invariant.
- Updating `last_seen[c] = right` **before** computing the window length. The length must be measured against the current `left`, then the map is updated for the next iteration.
- Off-by-one on the window length: it is `right - left + 1`, not `right - left`.
- Using `set` plus an inner loop that shrinks the window character-by-character until the duplicate is evicted. Functionally correct but `O(n)` per shrink in the worst case (degrades to `O(n^2)` total); the index-map jump-to-past-the-last-seen pattern is `O(n)` amortised.

---

## Failure cases

1. **`s = "abba"`** — at `right = 3` (the second `'a'`), the unguarded update `left = last_seen['a'] + 1 = 1` would move `left` backward past the second `'b'`, producing a window `"bba"` with a duplicate. The `max(left, ...)` guard keeps `left = 2` and the answer stays correct.
2. **`s = "tmmzuxt"`** — at `right = 6` (the second `'t'`), the unguarded update sets `left = 1`, re-admitting an `'m'` that is already past the current `left = 3`. Same `max(...)` guard fixes it; expected answer `5` (`"mzuxt"`).

---

## Interview follow-ups

- *"Longest substring with at most K distinct characters."* → LeetCode 340. Same sliding-window skeleton, but shrink from the left when the **distinct count** exceeds `K` instead of when a single character repeats.
- *"Longest substring with exactly K distinct characters."* → LeetCode 992 / inclusion-exclusion. Compute "at most K" minus "at most K-1".
- *"What if the alphabet is Unicode rather than ASCII?"* — `dict` already handles it; the `[128]` array trick (if you used it) breaks. Space stays `O(σ)`.
- *"Stream input?"* — sliding window is naturally streamable; emit the running `max_len` after each character.

---

## Bilingual summary

**English.** Sliding window with a `char -> last-seen index` map. Right pointer scans forward; on a duplicate, jump `left = max(left, last_seen[c] + 1)` so it never moves backward. Track `right - left + 1` at each step. Each index visited at most twice, giving `O(n)` time; space `O(σ)` for the alphabet size.

**中文。** 滑动窗口 + 哈希表（字符 → 最近出现的索引）。右指针向前推进；遇到重复字符时让 `left = max(left, last_seen[c] + 1)`，保证它永不回退。每步更新 `right - left + 1` 取最大值。每个下标至多被两个指针扫过，时间 `O(n)`；空间 `O(σ)`，σ 为字符集大小。
