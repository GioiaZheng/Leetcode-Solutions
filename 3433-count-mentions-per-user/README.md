# **LeetCode 3433 – Count Mentions Per User**

**Difficulty:** Medium  
**Tags:** Simulation, Hashing, Timeline Processing  
**Link:** [https://leetcode.com/problems/count-mentions-per-user/](https://leetcode.com/problems/count-mentions-per-user/)

---

## **Problem Summary**

You are given:

* An integer `numberOfUsers` representing the total number of users.
* A list of `events`, where each event is either:

  * A **MESSAGE** event mentioning users, or
  * An **OFFLINE** event indicating that a user goes offline for 60 time units.

Each message can mention:

* Specific users (`id<number>`)
* **ALL** users (including offline ones)
* **HERE** users (only users who are online at that time)

Your task is to compute how many times **each user is mentioned** across all MESSAGE events.

Important constraints:

* All users start online.
* Offline and online status changes **must be processed before any message at the same timestamp**.
* Mentions may repeat and **each mention counts**.

---

## **Key Insight**

This problem is essentially a **timeline simulation** problem.

The core difficulties are:

1. **Correctly handling user online/offline intervals**
2. **Processing multiple events at the same timestamp in the correct order**
3. **Distinguishing between different mention rules (ALL / HERE / idX)**

A direct simulation works efficiently because:

* The number of users and events is small (≤ 100)
* We can explicitly track user states over time

---

## **Approach**

### 1. Event Ordering

Events must be processed in this strict order:

1. Increasing timestamp
2. At the same timestamp:

   * **OFFLINE events first**
   * **MESSAGE events after**

This ensures that status changes are applied **before** mentions at the same time.

---

### 2. User State Tracking

Maintain:

* `online[i]`: whether user `i` is currently online
* `back_online_time[i]`: when user `i` automatically becomes online again
* `mentions[i]`: total mention count for user `i`

Before processing any event at time `t`, users whose

```
back_online_time <= t
```

must be brought back online.

---

### 3. Message Handling Rules

* **ALL** → mention all users (online or offline)
* **HERE** → mention only users who are currently online
* **idX** → mention user X, even if offline
* Repeated mentions in the same message all count

---

## **Example**

**Input**

```
numberOfUsers = 3
events = [
  ["OFFLINE","10","0"],
  ["MESSAGE","12","HERE"]
]
```

**Explanation**

* User 0 goes offline at time 10
* At time 12, only users 1 and 2 are online
* HERE mentions users 1 and 2

**Output**

```
[0,1,1]
```

---

## **Why This Works**

The solution works because:

* Timeline simulation guarantees correct ordering of state changes
* Explicit online tracking avoids ambiguity in HERE mentions
* Processing status recovery with `<= current_time` ensures no user remains incorrectly offline
* The small constraints allow safe and readable brute-force simulation

This approach mirrors real-world event systems where **state transitions precede actions**.

---

## **Complexity**

* **Time:** `O(numberOfUsers × events)`
* **Space:** `O(numberOfUsers)`

Both are well within the problem constraints.

---

## **What I Learned**

* How subtle ordering rules at the same timestamp can break an otherwise correct solution
* Why event simulation problems require careful handling of **state duration**, not just equality checks
* How to structure timeline-based problems to avoid hidden corner cases
* The importance of separating **state updates** from **event actions**
