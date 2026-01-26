# **LeetCode 1200 – Minimum Absolute Difference**

**Difficulty:** Easy  
**Tags:** Sorting, Greedy  
**Link:** [https://leetcode.com/problems/minimum-absolute-difference/](https://leetcode.com/problems/minimum-absolute-difference/)

---

## **Problem Summary**

You are given an array `arr` of **distinct integers**.

Your task is to find **all pairs of elements** `[a, b]` such that:

* `a` and `b` are elements from `arr`
* `a < b`
* `b - a` is equal to the **minimum absolute difference** among all pairs in `arr`

Return the list of such pairs in **ascending order**.

---

## **Key Insight**

If the array is **sorted**, the minimum absolute difference between any two elements **must occur between adjacent elements**.

Why?

* For any two non-adjacent elements in a sorted array, there exists at least one element in between them.
* That intermediate element creates a **smaller or equal difference** with one of them.
* Therefore, checking non-adjacent pairs is unnecessary.

 **Only adjacent elements after sorting matter.**

---

## **Algorithm**

1. Sort the array `arr`
2. Iterate through adjacent pairs and compute differences
3. Track the minimum difference found
4. Collect all adjacent pairs whose difference equals this minimum
5. Return the list of pairs

---

## **Example**

### Example 1

```
Input: arr = [4,2,1,3]

Sorted: [1,2,3,4]

Differences:
2 - 1 = 1
3 - 2 = 1
4 - 3 = 1

Output:
[[1,2], [2,3], [3,4]]
```

---

### Example 2

```
Input: arr = [1,3,6,10,15]

Sorted: [1,3,6,10,15]

Differences:
3 - 1 = 2   ← minimum
6 - 3 = 3
10 - 6 = 4
15 - 10 = 5

Output:
[[1,3]]
```

---

## **Complexity Analysis**

| Aspect        | Complexity                  |
| ------------- | --------------------------- |
| Sorting       | **O(n log n)**              |
| One pass scan | **O(n)**                    |
| Total Time    | **O(n log n)**              |
| Extra Space   | **O(1)** (excluding output) |

---

## **Why This Works**

* Sorting ensures elements are in order
* Adjacent differences capture the minimum possible gap
* Greedy scanning avoids unnecessary comparisons
* Simple logic with guaranteed correctness

---

## **Common Mistakes**

* ❌ Comparing all possible pairs (O(n²))
* ❌ Forgetting to sort first
* ❌ Returning pairs out of order

---

## **One-Line Interview Summary**

> “After sorting, the minimum absolute difference must occur between adjacent elements, so we scan neighbors and collect all pairs with the smallest gap.”
