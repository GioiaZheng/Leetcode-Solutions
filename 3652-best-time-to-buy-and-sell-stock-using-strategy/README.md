# **LeetCode 3652 – Best Time to Buy and Sell Stock using Strategy**

**Difficulty:** Medium  
**Tags:** Prefix Sum, Sliding Window, Greedy  
**Link:** [https://leetcode.com/problems/best-time-to-buy-and-sell-stock-using-strategy/](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-using-strategy/)

---

## **Problem Summary**

You are given two integer arrays of equal length:

* `prices[i]`: the stock price on day `i`
* `strategy[i]`: the trading action on day `i`

  * `-1` → buy one unit
  * `0` → hold
  * `1` → sell one unit

The **profit** is defined as:

```text
profit = sum(strategy[i] * prices[i]) over all days
```

You are also given an **even integer** `k`.

You may perform **at most one modification** to the strategy:

* Select **exactly `k` consecutive days**
* Set:

  * first `k / 2` elements → `0` (hold)
  * last `k / 2` elements → `1` (sell)

Return the **maximum possible profit** after at most one modification.

> There are no constraints on budget or stock ownership.

---

## **Key Insight**

* The original profit can be computed directly as a dot product.
* A modification only affects a **contiguous subarray of length `k`**.
* For a chosen window:

  * We **remove** the contribution of the original strategy
  * We **add** the contribution of the modified strategy
* Therefore, for each window we can compute a **profit delta**.

The goal is to find the window that gives the **maximum positive delta**.

---

## **Approach**

1. Compute the **base profit** using the original strategy.
2. Precompute prefix sums for:

   * `prices`
   * `strategy[i] * prices[i]`
3. Use a **sliding window** of length `k`:

   * For each window `[l, r]`:

     * Subtract original profit in that window
     * Add modified profit:

       * First `k/2` days → `0`
       * Last `k/2` days → sum of prices
4. Track the maximum total profit:

   * Either keep the original strategy
   * Or apply the best modification

---

## **Example**

### Example 1

```
prices   = [4, 2, 8]
strategy = [-1, 0, 1]
k = 2
```

Original profit:

```
(-1 × 4) + (0 × 2) + (1 × 8) = 4
```

Modify days `[0, 1]`:

```
strategy → [0, 1, 1]
profit   → 0 + 2 + 8 = 10
```

**Maximum profit = 10**

---

### Example 2

```
prices   = [5, 4, 3]
strategy = [1, 1, 0]
k = 2
```

Original profit:

```
5 + 4 + 0 = 9
```

All modifications reduce profit.

**Maximum profit = 9**

---

## **Why This Works**

* Only the modified window affects profit changes.
* Prefix sums allow each window to be evaluated in **O(1)** time.
* Sliding window ensures the entire solution runs in linear time.
* No simulation of stock ownership is needed due to problem constraints.

---

## **Complexity**

| Aspect | Complexity             |
| ------ | ---------------------- |
| Time   | **O(n)**               |
| Space  | **O(n)** (prefix sums) |

---

## **What I Learned**

* How to transform a strategy modification problem into a **delta optimization** problem.
* How prefix sums simplify range profit calculations.
* Why sliding window is ideal for fixed-length subarray optimization.
* How problem constraints can eliminate the need for state tracking.
