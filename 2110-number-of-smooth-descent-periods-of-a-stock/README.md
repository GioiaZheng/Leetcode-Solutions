# **LeetCode 2110 – Number of Smooth Descent Periods of a Stock**

**Difficulty:** Medium  
**Tags:** Array, Sliding Window, Consecutive Segment Counting  
**Link:** [https://leetcode.com/problems/number-of-smooth-descent-periods-of-a-stock/](https://leetcode.com/problems/number-of-smooth-descent-periods-of-a-stock/)

---

## **Problem Summary**

You are given an integer array `prices`, where `prices[i]` represents the stock price on day `i`.

A **smooth descent period** is defined as a contiguous subarray of one or more days such that:

* For every day except the first,
  the price decreases by **exactly 1** compared to the previous day.
* A single day by itself is always considered a valid smooth descent period.

Your task is to count the total number of smooth descent periods.

---

## **Key Insight**

The key observation is that **smooth descent periods correspond to consecutive segments** where:

```
prices[i - 1] - prices[i] == 1
```

For any such consecutive segment of length `k`:

```
prices[a], prices[a+1], ..., prices[b]
```

there are exactly:

```
1 + 2 + ... + k
```

smooth descent periods ending at each position.

Instead of computing this sum explicitly, we can **count them incrementally while scanning the array once**.

---

## **Approach**

We traverse the array from left to right and maintain:

* `length`: the length of the current smooth descent segment ending at index `i`
* `ans`: the total number of smooth descent periods

### Step-by-step logic:

1. Initialize `length = 1` because a single element always forms a valid period.
2. For each index `i`:

   * If `prices[i-1] - prices[i] == 1`,
     extend the current descent segment:

     ```
     length += 1
     ```
   * Otherwise, reset the segment:

     ```
     length = 1
     ```
3. Add `length` to the answer, since there are exactly `length` smooth descent periods ending at `i`.

---

## **Example Walkthrough**

### **Input**

```
prices = [3, 2, 1, 4]
```

### **Execution**

| Day | Price | Current Segment Length | Added to Answer | Total |
| --: | ----: | ---------------------: | --------------: | ----: |
|   0 |     3 |                      1 |               1 |     1 |
|   1 |     2 |                      2 |               2 |     3 |
|   2 |     1 |                      3 |               3 |     6 |
|   3 |     4 |                      1 |               1 |     7 |

### **Output**

```
7
```

---

## **Why This Works**

For each index `i`, the variable `length` represents the number of valid smooth descent periods **ending at `i`**.

This works because:

* Each new element in a descending-by-1 sequence extends all previous valid periods.
* When the descent breaks, we reset and start counting again.
* Every valid subarray is counted exactly once when it ends.

This avoids nested loops and allows the problem to be solved efficiently.

---

## **Complexity Analysis**

* **Time Complexity:** `O(n)`
  (Single pass through the array)

* **Space Complexity:** `O(1)`
  (Only constant extra space used)

---

## **What I Learned**

* How to count subarrays using **consecutive segment length tracking**
* Why incremental counting is more efficient than summing subarray lengths
* How sliding window–style logic applies even without explicit window pointers
* How to recognize problems where “each element contributes multiple subarrays”
