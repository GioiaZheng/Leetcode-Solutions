# **LeetCode 2092 – Find All People With Secret**

**Difficulty:** Hard  
**Tags:** Graph, BFS, Sorting  
**Link:** [https://leetcode.com/problems/find-all-people-with-secret/](https://leetcode.com/problems/find-all-people-with-secret/)

---

## **Problem Summary**

There are `n` people labeled from `0` to `n - 1`.

You are given a list of meetings, where:

```
meetings[i] = [x, y, time]
```

means person `x` and person `y` meet at `time`.

Rules:

* Person `0` knows a secret initially.
* At time `0`, person `0` shares the secret with `firstPerson`.
* If a person knows the secret at time `t`, they will share it with anyone they meet at time `t`.
* Secret sharing is **instantaneous** within the same time frame.
* Meetings at different times are independent.

Return **all people who know the secret after all meetings**, in any order.

---

## **Key Insight**

* Meetings must be processed **in chronological order**.
* Secret sharing can **chain within the same time**.
* Secret sharing **cannot cross time boundaries** unless carried by a person who already knows it.

Therefore:

> For each unique time, we must process meetings **independently**
> using only the people involved at that time.

---

## **Approach**

1. Sort all meetings by `time`.
2. Initialize a set `know` with `{0, firstPerson}`.
3. Process meetings **grouped by the same time**:

   * Build a temporary graph for meetings at this time.
   * Start BFS from people who already know the secret.
   * Spread the secret within this time block only.
4. After finishing this time block:

   * Add all newly informed people to `know`.
   * Discard the temporary graph.
5. Continue until all meetings are processed.

---

## **Example**

### Example 1

```
Input:
n = 6
meetings = [[1,2,5],[2,3,8],[1,5,10]]
firstPerson = 1

Output: [0,1,2,3,5]
```

---

### Example 2

```
Input:
n = 4
meetings = [[3,1,3],[1,2,2],[0,3,3]]
firstPerson = 3

Output: [0,1,3]
```

---

### Example 3

```
Input:
n = 5
meetings = [[3,4,2],[1,2,1],[2,3,1]]
firstPerson = 1

Output: [0,1,2,3,4]
```

---

## **Why This Works**

* Sorting ensures meetings are processed in correct time order.
* Temporary graphs prevent secrets from leaking across different times.
* BFS guarantees full propagation **within the same time block**.
* The solution matches the “instantaneous sharing” rule exactly.

---

## **Complexity**

| Aspect | Complexity                                 |
| ------ | ------------------------------------------ |
| Time   | **O(m log m)** (sorting meetings)          |
| Space  | **O(m)** (temporary graphs per time block) |

Where `m = len(meetings)`.

---

## **What I Learned**

* How to handle **time-based constraints** in graph problems.
* Why grouping events by time is essential for correctness.
* How BFS can simulate instantaneous propagation.
* A common interview pattern: **temporal graph processing**.

---

###  Notes

This is a classic example of **time-aware graph traversal**.

Understanding this problem helps with:

* Temporal Union Find problems
* Network propagation models
* Event-based graph simulations
