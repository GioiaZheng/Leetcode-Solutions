# **LeetCode 121 – Best Time to Buy and Sell Stock**

**Difficulty:** Easy  
**Tags:** Array, Greedy  
**Link:** [https://leetcode.com/problems/best-time-to-buy-and-sell-stock/](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/)

---

## **Problem Summary**

You are given an array `prices`, where `prices[i]` is the stock price on day `i`.

You want to maximize your profit by:

* Choosing **one day to buy** a stock
* Choosing a **later day to sell** the stock

If no profitable transaction is possible, return `0`.

---

## **Key Insight**

* The profit depends on:

  * the **lowest price so far** (best buying point)
  * the **current price** (possible selling point)
* We only need to scan the array **once**.
* At each day, we decide:

  * Is this a better day to buy?
  * Or is this a better day to sell?

This leads to a greedy, one-pass solution.

---

## **Approach**

1. Initialize:

   * `min_price` to infinity
   * `max_profit` to `0`
2. Iterate through each price:

   * Update `min_price` if the current price is lower
   * Otherwise, calculate the profit if selling today
   * Update `max_profit` if the profit is higher
3. Return `max_profit`

---

## **Example**

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

## **Why This Works**

* Buying must always happen **before** selling.
* Tracking the minimum price ensures a valid buying day.
* Every price is considered once as a potential selling point.
* Greedy choice at each step guarantees the global maximum profit.

---

## **Complexity**

| Aspect | Complexity |
| ------ | ---------- |
| Time   | **O(n)**   |
| Space  | **O(1)**   |

---

## **What I Learned**

* How to transform a brute-force `O(n²)` problem into `O(n)`.
* Why tracking historical minimums enables greedy solutions.
* A fundamental stock-trading pattern used in many variations.
* One of the simplest yet most important interview problems.

---

###  Notes

This problem is the foundation for more advanced stock problems:

* Best Time to Buy and Sell Stock II
* Stock with Cooldown
* Stock with Transaction Fee

Mastering this solution makes all of them easier.
