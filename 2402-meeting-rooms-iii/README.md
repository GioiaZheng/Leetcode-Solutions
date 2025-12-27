# **LeetCode 2402 – Meeting Rooms III**

**Difficulty:** Hard  
**Tags:** Heap (Priority Queue), Simulation, Sorting  
**Link:** [https://leetcode.com/problems/meeting-rooms-iii/](https://leetcode.com/problems/meeting-rooms-iii/)

---

## **Problem Summary**

You are given:

* An integer `n`, representing `n` meeting rooms labeled from `0` to `n - 1`
* An array `meetings`, where:

  ```
  meetings[i] = [start, end]
  ```

  indicates a meeting scheduled in the half-closed interval `[start, end)`

Rules for assigning meetings:

1. Meetings are processed in order of **original start time**.
2. If there are free rooms, assign the meeting to the **unused room with the smallest index**.
3. If no rooms are available:

   * Delay the meeting until a room becomes free
   * Keep the **original duration** of the meeting
   * Meetings with earlier original start times have priority
4. Return the room that held the **most meetings**.

   * If there is a tie, return the room with the **smallest index**.

---

## **Key Insight**

* This is a **simulation problem** with strict ordering rules.
* We need to efficiently:

  * Find the smallest available room
  * Find the room that finishes earliest
* A **two-heap approach** allows us to model this process precisely.

---

## **Approach**

1. Sort all meetings by `start` time.
2. Maintain two min-heaps:

   * `available`: free rooms ordered by room index
   * `busy`: occupied rooms ordered by `(end_time, room_index)`
3. For each meeting:

   * Free all rooms whose meetings have ended by the current `start`
   * If a room is available:

     * Assign the meeting immediately
   * Otherwise:

     * Take the room that finishes earliest
     * Delay the meeting to start at that time
4. Count how many meetings each room hosts.
5. Return the room with the maximum count (smallest index on ties).

---

## **Example**

### Example 1

```
Input:
n = 2
meetings = [[0,10],[1,5],[2,7],[3,4]]

Output: 0
```

Explanation:

```
Room 0: 2 meetings
Room 1: 2 meetings
→ return room 0 (smaller index)
```

---

### Example 2

```
Input:
n = 3
meetings = [[1,20],[2,10],[3,5],[4,9],[6,8]]

Output: 1
```

Explanation:

```
Room 1 and Room 2 both host 2 meetings
→ return room 1
```

---

## **Why This Works**

* Sorting guarantees meetings are processed in the correct order.
* The `available` heap enforces the smallest-index rule.
* The `busy` heap ensures the earliest-finishing room is reused first.
* Delayed meetings preserve their original duration.
* The simulation exactly follows the problem constraints.

---

## **Complexity**

| Aspect | Complexity     |
| ------ | -------------- |
| Time   | **O(m log n)** |
| Space  | **O(n)**       |

Where:

* `m = len(meetings)`
* `n = number of rooms`

---

## **What I Learned**

* How to simulate scheduling systems with priority constraints.
* Why multiple heaps are useful for real-time resource allocation.
* How to correctly model delayed tasks while preserving order.
* A classic hard problem combining heaps and simulation.
