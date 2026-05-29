# LeetCode 121 – Best Time to Buy and Sell Stock
**Difficulty:** Easy 
**Tags:** Array, Greedy 
**Link:** [https://leetcode.com/problems/best-time-to-buy-and-sell-stock/](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/)

---

## Problem Summary
You are given an array `prices`, where `prices[i]` is the stock price on day `i`.

You want to maximize your profit by:

* Choosing **one day to buy** a stock
* Choosing a **later day to sell** the stock

If no profitable transaction is possible, return `0`.

---

## Key Insight
* The profit depends on:

 * the **lowest price so far** (best buying point)
 * the **current price** (possible selling point)
* We only need to scan the array **once**.
* At each day, we decide:

 * Is this a better day to buy?
 * Or is this a better day to sell?

This leads to a greedy, one-pass solution.

---

## Approach
1. Initialize:

 * `min_price` to infinity
 * `max_profit` to `0`
2. Iterate through each price:

 * Update `min_price` if the current price is lower
 * Otherwise, calculate the profit if selling today
 * Update `max_profit` if the profit is higher
3. Return `max_profit`

---

## Example
### Example 1

```
Input: prices = [7,1,5,3,6,4]
Output: 5
```

Explanation:

```
Buy at 1 → Sell at 6 → Profit = 5
```

---

### Example 2

```
Input: prices = [7,6,4,3,1]
Output: 0
```

Explanation:

```
Prices keep decreasing → no profitable transaction
```

---

## Why This Works
* Buying must always happen **before** selling.
* Tracking the minimum price ensures a valid buying day.
* Every price is considered once as a potential selling point.
* Greedy choice at each step guarantees the global maximum profit.

---

## Complexity
| Aspect | Complexity |
| ------ | ---------- |
| Time | **O(n)** |
| Space | **O(1)** |

---

## What I Learned
* How to transform a brute-force `O(n²)` problem into `O(n)`.
* Why tracking historical minimums enables greedy solutions.
* A fundamental stock-trading pattern used in many variations.
* One of the simplest yet most important interview problems.

---

### Notes

This problem is the foundation for more advanced stock problems:

* Best Time to Buy and Sell Stock II
* Stock with Cooldown
* Stock with Transaction Fee

Mastering this solution makes all of them easier.

<!--
Sections below are the optional "study card" extension. The problem
carries `"study_card_status": "reviewed"` in metadata.json. See
CONTRIBUTING.md section "Optional Problem README Sections (Study Card)".
-->

---

## Brute-force baseline

Two nested loops: for each candidate buy-day `i`, try every later sell-day `j > i` and keep the maximum of `prices[j] - prices[i]`.

- **Time:** `O(n^2)` — `n(n-1)/2` pair checks in the worst case.
- **Space:** `O(1)`.

The one-pass `O(n)` solution above keeps the running minimum and computes profit against it without revisiting earlier days.

---

## Common mistakes

- Returning `max(prices) - min(prices)` without enforcing buy-before-sell. Fails on `[6, 1, 2]`: global max is 6, global min is 1, but 6 came first. The correct answer is `1` (buy at 1, sell at 2).
- Updating `min_price` **before** computing today's profit. With `[2, 1]`, updating min first sets `min_price = 1` then computes profit `1 - 1 = 0`. The canonical sequence is: compute profit using yesterday's `min_price`, **then** update `min_price`.
- Mixing in the LeetCode 122 (multi-transaction) logic — summing every positive consecutive diff. That solves a different problem; for I, only one buy-sell pair counts.
- Initialising `min_price = 0`. Any positive price keeps `min_price` at 0 forever and `max_profit` ends up equal to `max(prices)`, which is wrong.

---

## Failure cases

1. **`prices = [7, 6, 4, 3, 1]`** (strictly decreasing) — a buggy "max minus min" approach returns `7 - 1 = 6`. Correct answer is `0` because no profitable buy-then-sell is possible.
2. **`prices = [2, 4, 1]`** — easy to mis-handle if you reset `max_profit` whenever `min_price` updates. The 2 → 4 profit of 2 must be retained even after seeing the later 1, because the sell happened before the new minimum.

---

## Interview follow-ups

- *"What if you can make as many transactions as you like?"* — LeetCode 122. Sum every positive consecutive diff in one pass; `O(n)`.
- *"What if at most k transactions are allowed?"* — LeetCode 188. Two-state DP `dp[t][i]` over transactions and days; `O(nk)`.
- *"What if there is a transaction fee?"* — LeetCode 714. Two-state DP tracking `hold` and `cash`; subtract the fee at each sell.
- *"What if there is a 1-day cooldown after selling?"* — LeetCode 309. Three-state DP (`hold`, `sold`, `rest`); transition `sold -> rest -> hold`.
- *"Generalise to maximum subarray sum."* — the one-pass solution is Kadane's algorithm applied to the consecutive-diff array `prices[i+1] - prices[i]`; same `O(n)` / `O(1)`.

---

## Bilingual summary

**English.** Single-pass scan tracking the minimum price seen so far. At each day, first compute the candidate profit against the running minimum, then update the minimum. The ordering of the two updates enforces "buy must precede sell." `O(n)` time, `O(1)` space.

**中文。** 单次遍历，维护"到目前为止见过的最低价"。每一天先用当前价减去这个最低价算候选利润，再更新最低价。两步的顺序保证了"买必先于卖"。时间 `O(n)`，空间 `O(1)`。
