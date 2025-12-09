# **LeetCode 220 – Contains Duplicate III**

**Difficulty:** Hard  
**Tags:** Sliding Window, Bucket Sort, Hash Map  
**Link:** [https://leetcode.com/problems/contains-duplicate-iii/](https://leetcode.com/problems/contains-duplicate-iii/)

---

## **Problem Summary**

You are given an integer array `nums`, and two integers `indexDiff` and `valueDiff`.

The task is to determine whether there exist two distinct indices `(i, j)` such that:

1. `i != j`
2. `|i – j| <= indexDiff`
3. `|nums[i] – nums[j]| <= valueDiff`

Return `true` if such a pair exists, and `false` otherwise.

The constraints allow up to `10^5` elements, which means any brute-force or nested-loop approach will be too slow.

---

## **Key Insight**

This problem imposes **two simultaneous constraints**:

### 1. Index constraint

```
|i - j| <= indexDiff
```

This means only a sliding window of size `indexDiff` matters.

### 2. Value constraint

```
|nums[i] - nums[j]| <= valueDiff
```

To search efficiently within the sliding window, we need a data structure that can quickly answer:

> “Is there a number within `[nums[i] - valueDiff, nums[i] + valueDiff]`?”

A direct search is too slow.
The key insight is to use **Bucketization**, leveraging the fact that:

### If two numbers fall into the same bucket of width `(valueDiff + 1)`,

then they automatically satisfy `|a - b| <= valueDiff`.

Thus, each number is mapped to a bucket based on its value.
We only need to check:

* its own bucket
* the previous bucket
* the next bucket

Since only these three buckets may contain values within the allowed range.

All other buckets are too far away to be valid.

Additionally, we enforce the **index constraint** by sliding the window and removing elements that fall out of range.

---

## **Approach**

1. If `valueDiff < 0`, return `false` directly (no pair can satisfy).
2. Define bucket size:

   ```
   bucketSize = valueDiff + 1
   ```
3. Define a hash map `bucket` mapping bucket IDs to the values inside them.
4. For each index `i` and value `x = nums[i]`:

   * Compute bucket ID:

     ```
     bucketId = x // bucketSize
     ```
   * Check:

     * If bucketId exists → valid pair
     * If bucketId − 1 exists and difference ≤ valueDiff → valid
     * If bucketId + 1 exists and difference ≤ valueDiff → valid
   * Insert the value into its bucket.
5. Maintain sliding-window size:

   * If window exceeds `indexDiff`, remove the element `nums[i - indexDiff]` from its bucket.
6. If no valid pair is found, return `false`.

This achieves near-constant-time bucket insertion and lookup, giving a performant solution for large arrays.

---

## **Example**

**Input**

```
nums = [1, 2, 3, 1]
indexDiff = 3
valueDiff = 0
```

**Explanation**

* Window size allows comparing all numbers.
* We find `nums[0] = 1` and `nums[3] = 1`.
* They fall into the same bucket (size = 1), so difference is ≤ 0.

**Output**

```
true
```

---

## **Why This Works**

The bucket method is built on the observation that:

### • If two values differ by at most `valueDiff`,

they must fall into the same or adjacent bucket of width `valueDiff + 1`.

This reduces value checking to **O(1)** bucket lookups.

The sliding window ensures index constraint is respected by removing outdated elements.

Thus:

* We avoid comparing all pairs.
* We avoid maintaining a sorted structure.
* The algorithm remains efficient even for 100,000 elements.

This is a classic application of bucketization combined with window maintenance.

---

## **Complexity**

| Operation | Complexity                                             |
| --------- | ------------------------------------------------------ |
| Time      | `O(n)` average, `O(n log n)` worst-case due to hashing |
| Space     | `O(indexDiff)` buckets stored in memory                |

---

## **What I Learned**

* How value constraints can be transformed into bucket ranges.
* Why bucket size `(valueDiff + 1)` ensures correctness.
* How to combine sliding-window logic with bucketization to satisfy both index and value constraints.
* How bucket-based techniques can replace balanced BSTs and reduce constant factors.
* Why this problem is categorized as hard: two orthogonal constraints require two complementary techniques.
