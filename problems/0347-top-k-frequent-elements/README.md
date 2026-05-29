# LeetCode 347 – Top K Frequent Elements
**Difficulty:** Medium 
**Tags:** Array, Hash Table, Heap, Sorting 
**Link:** [https://leetcode.com/problems/top-k-frequent-elements/](https://leetcode.com/problems/top-k-frequent-elements/)

---

## Problem Summary
Given an integer array `nums`, return a list containing the `k` most frequent elements.

The order of the returned elements does not matter, but the result must contain exactly the `k` elements that appear most often in the array.

---

## Key Insight
The key observation is that this problem is about **frequency ranking**, not sorting by value.

A mapping from elements to their occurrence counts is required.
Once frequencies are known, the task reduces to selecting the `k` highest-frequency keys.

Common approaches include:

* Sorting elements by frequency
* Using a max heap
* Using a bucket structure keyed by frequency

Since the value range is arbitrary, a frequency map is essential.

---

## Approach
1. Iterate through the array and build a frequency map:

 ```
 element → count
 ```
2. Extract all unique elements.
3. Sort them based on frequency in descending order.
4. Take the first `k` items from the sorted list.
5. Return these as the result.

This method ensures correctness and is simple to implement.

---

## Example
**Input**

```
nums = [1, 1, 1, 2, 2, 3]
k = 2
```

**Explanation**
The elements `1` (frequency 3) and `2` (frequency 2) are the top two most frequent elements.

**Output**

```
[1, 2]
```

---

## Why This Works
The frequency map captures exactly how often each element appears.
Sorting the keys by their associated counts guarantees that the top `k` entries correspond to the required result.

This problem emphasizes the separation between:

* Value ordering (not relevant)
* Frequency ordering (required)

Using a hash map plus sorting provides clarity and efficiency.

---

## Complexity
* **Time:** `O(n log n)` due to sorting
 Can be optimized to `O(n)` with bucket sort or `O(n log k)` with a heap.
* **Space:** `O(n)` for the frequency map

---

## What I Learned
* How separating value and frequency simplifies ranking problems.
* Why hash maps are essential for counting occurrences efficiently.
* How different data structures (heap, bucket, sort) impact performance trade-offs.

---

## Solution Files
- `solution.py` is the recommended `Counter.most_common` implementation because it is concise and idiomatic for Python.
- `approaches/solution_sorting.py` and `approaches/solution_bucket_sort.py` preserve sorting and bucket-sort alternatives for comparison.

<!--
Sections below are the optional "study card" extension. The problem
carries `"study_card_status": "reviewed"` in metadata.json. See
CONTRIBUTING.md section "Optional Problem README Sections (Study Card)".
-->

---

## Brute-force baseline

Build the frequency map; sort all `(element, count)` pairs by count descending; take the first `k`.

- **Time:** `O(n + u \log u)` where `u` is the number of distinct elements. Worst case `u = n`, giving `O(n \log n)`.
- **Space:** `O(u)` for the frequency map.

The bucket-sort variant drops time to `O(n)`; the size-`k` min-heap variant gives `O(n \log k)`, which is faster than the full sort whenever `k \ll n`.

---

## Common mistakes

- Sorting by **value** instead of **frequency**. The problem ranks by occurrence count, not by integer magnitude.
- Using a max-heap and popping `k` times. That is `O(u + k \log u)`, no better than the full sort. The fast pattern is a **min-heap of size `k`**: push every `(count, element)` then evict the smallest when size exceeds `k`. Total `O(u \log k)`.
- Bucket sort indexed by frequency, then scanning **low to high**. Frequencies range `[1, n]`, so buckets must be scanned from index `n` down to `0` to surface the most frequent first.
- Returning `Counter.most_common(k)` directly without stripping the counts. The output type is `list[int]`, not `list[tuple[int, int]]` — extract with `[elem for elem, _ in counter.most_common(k)]`.
- Forgetting that ties are arbitrary. Some implementations sort by `(count, value)` deterministically; LeetCode accepts any of the equally-frequent elements at the boundary.

---

## Failure cases

1. **`nums = [1], k = 1`** — single-element trivial case; expected `[1]`. Implementations that `pop` from an empty data structure or assume `len(nums) > k` crash here.
2. **`nums = [1, 2, 3, 4], k = 2`** — all elements have frequency `1`. Any 2 of the 4 are a valid answer; the bug to catch is sorting by *value* (returns `[1, 2]` always, which is correct by coincidence here but would fail on `[4, 3, 2, 1], k = 2` expecting `[4, 3]` or any 2).
3. **`nums = [4, 1, -1, 2, -1, 2, 3], k = 2`** — expected `[-1, 2]` (both have count `2`); tests that negative numbers do not break the frequency map and that the heap / bucket variants pick the right two.

---

## Interview follow-ups

- *"What if `k` changes per query but `nums` does not?"* — precompute the sorted-by-frequency list once, then each query is an `O(k)` slice.
- *"Streaming input."* — Misra-Gries summary or Count-Min Sketch for approximate top-k under bounded memory; exact top-k requires `O(u)` storage.
- *"Why is bucket sort `O(n)` here?"* — frequencies are bounded by `n`, so there are at most `n + 1` distinct buckets; iterating buckets is `O(n)`, and the total elements across buckets is `u <= n`.
- *"Top-k by some other ordering — e.g. absolute value, or `(frequency, -value)`?"* — heap stays valid as long as the comparison key is a total order; wrap as `(key_fn(elem), elem)` tuples.

---

## Bilingual summary

**English.** One pass through `nums` builds a `Counter`. Then choose by `n / k` ratio: (a) sort all `(elem, count)` pairs for `O(u \log u)` — simplest; (b) a size-`k` min-heap evicts the smallest as new elements arrive, `O(u \log k)`; (c) bucket sort indexed by frequency `1..n`, scanned high-to-low, `O(n)`. Space `O(u)`.

**中文。** 一次遍历 `nums` 构建 `Counter`，然后按 `n / k` 比值选实现：(a) 把所有 `(elem, count)` 排序取前 k，`O(u \log u)`；(b) 容量 `k` 的小顶堆，新元素来时驱逐最小，`O(u \log k)`；(c) 频次作为索引的桶排序（桶大小 `1..n`，从高往低扫），`O(n)`。空间 `O(u)`。
