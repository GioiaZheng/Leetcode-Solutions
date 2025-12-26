# **LeetCode 2483 – Minimum Penalty for a Shop**

**Difficulty:** Medium  
**Tags:** String, Greedy, Prefix Sum  
**Link:** [https://leetcode.com/problems/minimum-penalty-for-a-shop/](https://leetcode.com/problems/minimum-penalty-for-a-shop/)

---

## **Problem Summary**

You are given a string `customers` consisting of characters `'Y'` and `'N'`.

* `'Y'` means customers come during that hour.
* `'N'` means no customers come during that hour.

If the shop closes at hour `j` (`0 <= j <= n`):

* For every hour **before `j`** (shop open):

  * `'N'` adds **+1 penalty**
* For every hour **from `j` onward** (shop closed):

  * `'Y'` adds **+1 penalty**

Return the **earliest hour** at which closing the shop results in the **minimum penalty**.

---

## **Key Insight**

* Choosing a closing time splits the timeline into two parts:

  * Open hours → penalize `'N'`
  * Closed hours → penalize `'Y'`
* Instead of recalculating penalties for every possible closing time,
  we can **scan once** and update the penalty incrementally.
* This is a classic **prefix scan + greedy minimum tracking** problem.

---

## **Approach**

1. Assume the shop closes at hour `0`:

   * All `'Y'` characters contribute to the penalty.
2. Scan the string from left to right:

   * If we pass a `'Y'`, staying open avoids a closed-penalty → penalty decreases by `1`
   * If we pass an `'N'`, staying open causes an open-penalty → penalty increases by `1`
3. After processing each hour `i`, treat it as closing at hour `i + 1`.
4. Track the **minimum penalty** and the **earliest hour** that achieves it.

---

## **Example**

### Example 1

```
Input: customers = "YYNY"
Output: 2
```

Explanation (penalty by closing hour):

```
Hour 0 → 3
Hour 1 → 2
Hour 2 → 1   ← minimum (earliest)
Hour 3 → 2
Hour 4 → 1
```

---

### Example 2

```
Input: customers = "NNNNN"
Output: 0
```

Explanation:

```
Best to close immediately since no customers ever come
```

---

### Example 3

```
Input: customers = "YYYY"
Output: 4
```

Explanation:

```
Best to stay open all the time
```

---

## **Why This Works**

* Each step updates the penalty based on **local information only**.
* The scan guarantees all possible closing times are considered.
* Tracking the earliest minimum satisfies the problem requirement.
* No extra arrays or complex data structures are needed.

---

## **Complexity**

| Aspect | Complexity |
| ------ | ---------- |
| Time   | **O(n)**   |
| Space  | **O(1)**   |

Where `n = len(customers)`.

---

## **What I Learned**

* How to model penalties using prefix differences.
* Why a greedy scan can replace repeated full recalculations.
* A clean way to handle “earliest minimum” requirements.
* A reusable pattern for many prefix-based optimization problems.

---

###  Notes

This pattern is closely related to:

* Prefix sum optimizations
* Sweep-line / one-pass greedy algorithms
* Cost minimization over split points
