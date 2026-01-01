# **LeetCode 2343 – Query Kth Smallest Trimmed Number**

**Difficulty:** Medium  
**Tags:** Array, String, Sorting, Caching  
**Link:** [https://leetcode.com/problems/query-kth-smallest-trimmed-number/](https://leetcode.com/problems/query-kth-smallest-trimmed-number/)

---

## **Problem Summary**

You are given:

* An array `nums` of numeric strings, all of the same length
* A list of queries `queries`, where each query is `[k, trim]`

For each query:

1. **Trim** every number in `nums` to its **rightmost `trim` digits**
2. Sort the trimmed numbers:

   * By numeric value (as strings)
   * If equal, by **original index**
3. Return the **index** of the `k`-th smallest trimmed number
4. Reset `nums` to their original form before the next query

Return an array of answers, one per query.

---

## **Key Insight**

* The constraints are small:

  * `nums.length ≤ 100`
  * `queries.length ≤ 100`
* This allows us to:

  * Directly sort trimmed values
  * Cache results for repeated `trim` values
* String comparison works correctly because:

  * All trimmed strings have the same length
  * Leading zeros are allowed and handled naturally

---

## **Approach**

1. Let `L` be the length of each number string.
2. For each unique `trim` value:

   * Create a list of `(trimmed_string, original_index)`
   * Sort the list (lexicographically, then by index)
   * Cache the sorted result
3. For each query `[k, trim]`:

   * Look up the cached sorted list
   * Take the element at position `k - 1`
   * Return its original index

This avoids recomputing the same trims multiple times.

---

## **Example**

### Example 1

```
nums = ["102","473","251","814"]
queries = [[1,1],[2,3],[4,2],[1,2]]

Output: [2,2,1,0]
```

Explanation (first query):

```
Trim to last 1 digit → ["2","3","1","4"]
Sorted → ["1","2","3","4"]
1st smallest = "1" at index 2
```

---

### Example 2

```
nums = ["24","37","96","04"]
queries = [[2,1],[2,2]]

Output: [3,0]
```

---

## **Why This Works**

* Sorting strings of equal length preserves numeric order.
* Stable tie-breaking is achieved by sorting with indices.
* Caching avoids repeated sorting for the same trim length.
* The approach is simple, reliable, and efficient under constraints.

---

## **Complexity**

Let:

* `n = len(nums)`
* `L = length of each number`

| Aspect | Complexity         |
| ------ | ------------------ |
| Time   | **O(L × n log n)** |
| Space  | **O(L × n)**       |

This is well within the problem limits.

---

## **What I Learned**

* How to handle query problems with preprocessing.
* Why caching is useful even for small constraints.
* That numeric comparison can often be replaced by string comparison safely.
* A clean pattern for handling repeated queries efficiently.

---

###  Notes

Alternative approaches exist (e.g. radix-style comparison),
but for these constraints, **sorting + caching** is the clearest and most robust solution.

---

## **One-Line Interview Summary**

> “Preprocess each trim length by sorting trimmed strings with indices, cache the results, and answer each query in O(1).”
