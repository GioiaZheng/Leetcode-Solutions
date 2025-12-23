# **LeetCode 2054 – Two Best Non-Overlapping Events**

**Difficulty:** Medium  
**Tags:** Array, Sorting, Binary Search, Greedy  
**Link:** [https://leetcode.com/problems/two-best-non-overlapping-events/](https://leetcode.com/problems/two-best-non-overlapping-events/)

---

## **Problem Summary**

You are given a list of events, where:

```
events[i] = [startTime, endTime, value]
```

* Each event starts at `startTime` and ends at `endTime` (inclusive).
* If you attend an event, you gain `value`.

You may attend **at most two non-overlapping events**.

Two events **overlap** if:

```
event2.startTime <= event1.endTime
```

So if an event ends at time `t`, the next event must start at **`t + 1` or later**.

Return the **maximum total value** you can obtain.

---

## **Key Insight**

* You can choose **at most two** events.
* For each event, the best choice is:

  * take it alone
  * or combine it with the **best possible non-overlapping event after it**
* This can be solved efficiently by:

  * sorting events by start time
  * using binary search to find the next valid event
  * using a suffix maximum array to get the best future value

---

## **Approach**

1. Sort all events by `startTime`.
2. Build a `starts` array containing all start times.
3. Build a `suffix_max` array:

   * `suffix_max[i]` = maximum event value among events `i ... n-1`
4. For each event `i`:

   * Consider taking only this event.
   * Use binary search to find the first event with:

     ```
     startTime >= endTime + 1
     ```
   * Combine current value with the best future value.
5. Return the maximum result found.

---

## **Example**

### Example 1

```
Input: events = [[1,3,2],[4,5,2],[2,4,3]]
Output: 4
```

Explanation:

```
Choose events [1,3,2] and [4,5,2] → total = 4
```

---

### Example 2

```
Input: events = [[1,3,2],[4,5,2],[1,5,5]]
Output: 5
```

Explanation:

```
Best choice is taking the single event with value 5
```

---

### Example 3

```
Input: events = [[1,5,3],[1,5,1],[6,6,5]]
Output: 8
```

Explanation:

```
Choose events [1,5,3] and [6,6,5] → total = 8
```

---

## **Why This Works**

* Sorting ensures events are processed in time order.
* Binary search efficiently finds the next non-overlapping event.
* The suffix maximum array guarantees the best possible second choice.
* All valid combinations of at most two events are considered.

---

## **Complexity**

| Aspect | Complexity     |
| ------ | -------------- |
| Time   | **O(n log n)** |
| Space  | **O(n)**       |

Where `n = len(events)`.

---

## **What I Learned**

* How to optimize interval scheduling with a fixed number of selections.
* How binary search and suffix optimization work together.
* Why inclusive time boundaries matter in scheduling problems.
* A reusable pattern for many “choose k non-overlapping intervals” problems.

---

### Notes

This problem is closely related to:

- 1235. Maximum Profit in Job Scheduling
- 1751. Maximum Number of Events That Can Be Attended II
- 2008. Maximum Earnings From Taxi

They all share the same **time-based optimization pattern**.
