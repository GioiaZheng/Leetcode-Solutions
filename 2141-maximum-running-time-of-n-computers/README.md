# 2141. Maximum Running Time of N Computers

**Difficulty:** Hard  
**Topics:** Binary Search, Greedy, Math  
**Link:** https://leetcode.com/problems/maximum-running-time-of-n-computers/

---

##  Problem Description

You have `n` computers and an array `batteries` where each battery has a certain running time (in minutes).  
You want to run **all n computers simultaneously** for the **maximum number of minutes**, under these rules:

- Initially, you may insert **at most one battery per computer**.
- You can **swap batteries at any time**, and swapping takes no time.
- Batteries **cannot be recharged**.
- A battery can be reused on any computer after removal.

Return the **maximum number of minutes** that all `n` computers can run simultaneously.

---

##  Examples

### Example 1
```

Input: n = 2, batteries = [3, 3, 3]
Output: 4

```

Explanation:  
You can swap batteries optimally to run both computers for 4 minutes total.

---

### Example 2
```

Input: n = 2, batteries = [1,1,1,1]
Output: 2

```

---

##  Key Insight

Since batteries can be freely swapped, the order does not matter.

To run **n computers for t minutes**, we need:

```

Total usable power ≥ n * t

```

Each battery contributes at most:

```

min(battery[i], t)

```

Thus total contribution is:

```

sum( min(bi, t) )

```

If:

```

sum(min(bi, t)) ≥ n * t

```

 We **can** run the computers for `t` minutes.  
 Otherwise, we **cannot**.

This gives a clear **feasibility function** → perfect for **binary search**.

---

##  Why Binary Search?

`t` is monotonic:

- If we can run for `t` minutes → we can run for any `t' < t`
- If we cannot run for `t` minutes → we cannot run for any `t' > t`

Therefore:

We binary search `t` between:

```

left = 0
right = sum(batteries) // n

```

---

##  Algorithm

1. Binary search on the answer `t`
2. For each candidate `t`, compute:
```

total = sum(min(bi, t))

```
3. If `total >= n * t`, t is feasible
4. Adjust search boundaries
5. Return the maximum feasible t

---

##  Complexity

```

Time:  O(n log(sum(batteries)/n))
Space: O(1)

````

Efficient for n up to 100,000.

---

##  Summary

* This is a **binary search on time** problem.
* We check feasibility using:

  ```
  sum(min(bi, t)) >= n * t
  ```
* Swapping batteries is allowed, so only total usable minutes matter.
* Final answer is the maximum `t` satisfying the feasibility condition.
