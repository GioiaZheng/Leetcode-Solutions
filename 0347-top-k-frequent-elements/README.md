# **LeetCode 347 – Top K Frequent Elements**

**Difficulty:** Medium  
**Tags:** Array, Hash Table, Heap, Sorting  
**Link:** [https://leetcode.com/problems/top-k-frequent-elements/](https://leetcode.com/problems/top-k-frequent-elements/)

---

## **Problem Summary**

Given an integer array `nums`, return a list containing the `k` most frequent elements.

The order of the returned elements does not matter, but the result must contain exactly the `k` elements that appear most often in the array.

---

## **Key Insight**

The key observation is that this problem is about **frequency ranking**, not sorting by value.

A mapping from elements to their occurrence counts is required.
Once frequencies are known, the task reduces to selecting the `k` highest-frequency keys.

Common approaches include:

* Sorting elements by frequency
* Using a max heap
* Using a bucket structure keyed by frequency

Since the value range is arbitrary, a frequency map is essential.

---

## **Approach**

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

## **Example**

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

## **Why This Works**

The frequency map captures exactly how often each element appears.
Sorting the keys by their associated counts guarantees that the top `k` entries correspond to the required result.

This problem emphasizes the separation between:

* Value ordering (not relevant)
* Frequency ordering (required)

Using a hash map plus sorting provides clarity and efficiency.

---

## **Complexity**

* **Time:** `O(n log n)` due to sorting
  Can be optimized to `O(n)` with bucket sort or `O(n log k)` with a heap.
* **Space:** `O(n)` for the frequency map

---

## **What I Learned**

* How separating value and frequency simplifies ranking problems.
* Why hash maps are essential for counting occurrences efficiently.
* How different data structures (heap, bucket, sort) impact performance trade-offs.
