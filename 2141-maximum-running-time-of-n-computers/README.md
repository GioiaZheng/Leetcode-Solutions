# **LeetCode 2141 – Maximum Running Time of N Computers**

**Difficulty:** Hard
**Tags:** Binary Search, Greedy, Math
**Link:** [https://leetcode.com/problems/maximum-running-time-of-n-computers/](https://leetcode.com/problems/maximum-running-time-of-n-computers/)

---

## **Problem Summary**

We are given `n` computers and a list of batteries.
Each battery can power exactly one computer at a time, and batteries can be swapped freely without any cost.

The goal is to determine the maximum number of minutes all `n` computers can run simultaneously.

---

## **Key Insight**

If each computer needs to run for `T` minutes, then the total required energy is:

```
n * T
```

Each battery can contribute at most:

```
min(battery[i], T)
```

Thus, the feasibility of a candidate time `T` depends on:

```
sum(min(battery[i], T)) ≥ n * T
```

This condition is monotonic, meaning if a time `T` is feasible, all smaller values are also feasible. This justifies using binary search.

---

## **Approach**

1. Compute the total battery capacity.
2. The maximum possible running time cannot exceed `total_capacity // n`.
3. Use binary search over `[0, total_capacity // n]`.
4. For each candidate time `T`, compute:

   ```
   total_usable = sum(min(battery[i], T))
   ```
5. If `total_usable ≥ n * T`, then `T` is feasible; otherwise, it is not.
6. Return the maximum feasible value of `T`.

---

## **Example**

**Input**

```
n = 2
batteries = [3, 3, 3]
```

**Explanation**

* Total energy = 9
* Maximum possible equal time = 9 // 2 = 4
* It is possible to combine battery energy to sustain both computers for 4 minutes.

**Output**

```
4
```

---

## **Why This Works**

Because batteries can be swapped arbitrarily, the physical distribution of energy does not matter. What matters is the **total usable energy**, capped at `T` for each battery.

The feasibility condition:

```
sum(min(b[i], T)) ≥ n * T
```

is monotonic with respect to `T`, which allows the solution to perform an efficient binary search.

---

## **Complexity**

* **Time:** `O(m log(total/n))`, where `m` is the number of batteries
* **Space:** `O(1)`

---

## **What I Learned**

* How binary search is applied in “maximize feasible value” problems.
* How monotonic feasibility conditions simplify optimization.
* Why freely swappable batteries reduce the problem to analyzing total usable energy.
我就依序开始重写所有题目。
