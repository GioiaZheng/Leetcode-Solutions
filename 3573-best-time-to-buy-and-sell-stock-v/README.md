# **LeetCode 3573 – Best Time to Buy and Sell Stock V**

**Difficulty:** Medium  
**Tags:** Dynamic Programming, Stock Trading, State Machine  
**Link:** [https://leetcode.com/problems/best-time-to-buy-and-sell-stock-v/](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-v/)

---

## **Problem Summary**

You are given an integer array `prices`, where `prices[i]` represents the stock price on day `i`,
and an integer `k` representing the **maximum number of transactions** allowed.

Each transaction can be one of the following:

* **Normal transaction:** buy on day `i`, sell on day `j` (`i < j`)
  Profit: `prices[j] - prices[i]`
* **Short selling transaction:** sell on day `i`, buy back on day `j` (`i < j`)
  Profit: `prices[i] - prices[j]`

Constraints:

* You must **complete one transaction before starting another**
* You cannot buy/sell on the same day as another transaction’s action
* At most `k` completed transactions are allowed

Return the **maximum total profit** achievable.

---

## **Key Insight**

This problem is an extension of the classic *Best Time to Buy and Sell Stock IV*,
with an important twist:

> You are allowed to profit from both **price increases** and **price decreases**.

The key observation:

* A transaction is **complete only after both actions**:

  * buy → sell (normal)
  * sell → buy back (short)
* At any time, the trader can be in **exactly one of three states**:

  1. **Free** (no position)
  2. **Holding a long position**
  3. **Holding a short position**

Thus, the problem naturally maps to a **state-machine dynamic programming** solution.

---

## **DP State Definition**

Let:

```
dp[t][state]
```

be the maximum profit after completing `t` transactions, where:

* `state = 0` → free (no open position)
* `state = 1` → holding a long position (after buy)
* `state = 2` → holding a short position (after sell)

Initial state:

```
dp[0][0] = 0
```

All other states are initialized to negative infinity.

---

## **State Transitions**

For each day with price `p`:

### From FREE

* Buy → hold long
  `dp[t][1] = max(dp[t][1], dp[t][0] - p)`
* Sell → hold short
  `dp[t][2] = max(dp[t][2], dp[t][0] + p)`

### From HOLD LONG

* Sell → complete one transaction
  `dp[t+1][0] = max(dp[t+1][0], dp[t][1] + p)`

### From HOLD SHORT

* Buy back → complete one transaction
  `dp[t+1][0] = max(dp[t+1][0], dp[t][2] - p)`

Only completed transactions increase the transaction count.

---

## **Approach**

1. Use a 2D DP array tracking:

   * number of completed transactions
   * current holding state
2. Iterate through prices day by day
3. Update all valid state transitions
4. Use space optimization by rolling DP arrays
5. The final answer is the maximum profit in the **free state** with at most `k` transactions

---

## **Example**

### Example 1

```
prices = [1,7,9,8,2], k = 2
```

Transactions:

1. Buy at 1 → sell at 9 → profit = 8
2. Sell at 8 → buy back at 2 → profit = 6

**Total profit = 14**

---

### Example 2

```
prices = [12,16,19,19,8,1,19,13,9], k = 3
```

Transactions:

1. Buy at 12 → sell at 19 → profit = 7
2. Sell at 19 → buy back at 8 → profit = 11
3. Buy at 1 → sell at 19 → profit = 18

**Total profit = 36**

---

## **Why This Works**

* The state-machine DP cleanly models all valid actions
* Normal and short transactions are treated symmetrically
* The transaction limit is strictly enforced
* No overlapping or invalid operations are allowed
* Works efficiently within constraints

---

## **Complexity**

| Aspect | Complexity   |
| ------ | ------------ |
| Time   | **O(n · k)** |
| Space  | **O(k)**     |

Where `n` is the number of days.

---

## **What I Learned**

* How to model stock trading problems using **state-machine DP**
* How to extend classic stock DP problems with **short selling**
* Why counting only **completed transactions** is crucial
* How to manage multiple states cleanly without overlap
