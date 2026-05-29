# LeetCode 49 – Group Anagrams
**Difficulty:** Medium 
**Tags:** Array, Hash Table, String 
**Link:** [https://leetcode.com/problems/group-anagrams/](https://leetcode.com/problems/group-anagrams/)

---

## Problem Summary
You are given an array of strings.
Your task is to group the strings into collections where each group consists of strings that are **anagrams** of one another.

Two strings are anagrams if they contain the same characters with identical frequencies, regardless of order.

The output should be a list of groups, where each group contains all strings belonging to the same anagram class.

---

## Key Insight
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

## Approach
1. Create an empty hash map.
2. For each word:

 * Compute its canonical representation.
 (Most commonly, sort the string.)
 * Insert the word into the hash map under its canonical key.
3. After processing all strings, the values of the hash map represent the anagram groups.
4. Return all groups.

This approach ensures that all words sharing the same canonical form end up in the same group.

---

## Example
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

## Why This Works
The set of characters in a string, together with their counts, uniquely identifies an anagram class.
Sorting the characters provides a simple and deterministic canonical form.

Using the canonical representation as a hash key ensures:

* All true anagrams map to the same bucket
* No non-anagrams can appear in the same group

This converts what seems like a pairwise comparison problem into a classification problem based on hashing.

---

## Complexity
Using sorting as the canonical form:

* **Time:** `O(n * k log k)`
 where `n` is the number of strings and `k` is the maximum string length
* **Space:** `O(n * k)` for storing grouped strings

Using character frequency counting instead of sorting improves the canonical computation to `O(k)`.

---

## What I Learned
* How canonical representations simplify grouping tasks.
* Why hashing enables efficient classification of objects by structural similarity.
* How string anagram relationships reduce to frequency analysis or sorting.

<!--
Sections below are the optional "study card" extension. The problem
carries `"study_card_status": "reviewed"` in metadata.json. See
CONTRIBUTING.md section "Optional Problem README Sections (Study Card)".
-->

---

## Brute-force baseline

For each pair `(i, j)` of strings in `strs`, decide whether they are anagrams (e.g. via `sorted(strs[i]) == sorted(strs[j])`); union-find or merge groups based on positive matches.

- **Time:** `O(n^2 \cdot k \log k)` where `n` is the number of strings and `k` is the maximum string length.
- **Space:** `O(n)` for the group structure (excluding the output).

The hash-based grouping above improves to `O(n \cdot k \log k)` (sort-string key) or `O(n \cdot k)` (count-tuple key).

---

## Common mistakes

- Using a sorted **list** as a `dict` key. `sorted(s)` returns a `list`, which is unhashable. Convert via `"".join(sorted(s))` or `tuple(sorted(s))`.
- Encoding count keys without a deterministic ordering. A 26-int tuple is canonical because its position encodes the character. Storing `tuple(counter.items())` without `sorted(...)` first lets dict-iteration order leak in.
- Returning a list of `set`s instead of a list of `list`s. The problem signature expects lists; sets also deduplicate, which would silently drop intentional duplicates like `["", ""]`.
- Mutating the input. Sorting `strs` in place to build keys leaves the caller's array reordered. Compute keys without touching the source list.

---

## Failure cases

1. **`strs = [""]`** — single empty string. Canonical key is `""` (sorted of empty is empty). Output is `[[""]]`. Implementations that skip empty inputs would drop it.
2. **`strs = ["", ""]`** — two empty strings, both keyed by `""`. Expected output is `[["", ""]]`. A set-based deduper would collapse them to `[[""]]`.

---

## Interview follow-ups

- *"What if k is much larger than n?"* — switch from sort-key (`O(k \log k)` per string) to count-tuple key (`O(k)` per string). Total drops from `O(n \cdot k \log k)` to `O(n \cdot k)`.
- *"What if the alphabet is Unicode, not just lowercase?"* — use `tuple(sorted(Counter(s).items()))` as the key; loses the fixed-size 26-element optimisation but stays linear in `k`.
- *"What if memory is constrained?"* — sort `strs` by canonical key, then linearly group adjacent same-key entries. `O(n \cdot k \log k + n \log n)` time, `O(1)` extra space beyond the output.
- *"Streaming input?"* — `defaultdict(list)` works the same; you simply cannot emit any group until the stream closes, since a later string could join an existing group.

---

## Bilingual summary

**English.** Bucket each string by a canonical anagram key — either the sorted character string/tuple or a fixed-length character-count tuple. One pass through `strs` into a `defaultdict(list)`; the dict values are the anagram groups. Sort-key variant `O(n \cdot k \log k)`; count-tuple variant `O(n \cdot k)`. Space `O(n \cdot k)`.

**中文。** 用"规范化字符特征"作 key 对字符串分桶——可以是排序后的字符串/元组，或长度固定的字符频次元组。`defaultdict(list)` 一次扫描即可，字典的 values 就是各 anagram 组。排序 key 版 `O(n \cdot k \log k)`，频次元组版 `O(n \cdot k)`。空间 `O(n \cdot k)`。
