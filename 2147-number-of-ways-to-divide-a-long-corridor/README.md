# **LeetCode 2147 – Number of Ways to Divide a Long Corridor**

**Difficulty:** Hard  
**Tags:** Greedy, Combinatorics, Counting  
**Link:** [https://leetcode.com/problems/number-of-ways-to-divide-a-long-corridor/](https://leetcode.com/problems/number-of-ways-to-divide-a-long-corridor/)

---

## **Problem Summary**

You are given a string `corridor` representing a long corridor, where:

* `'S'` represents a **seat**
* `'P'` represents a **plant**

There is already a room divider installed:

* to the **left of index 0**
* to the **right of index n − 1**

You may install additional dividers between any two adjacent positions.

The goal is to divide the corridor into **non-overlapping sections** such that:

* **Each section contains exactly two seats**
* Each section may contain **any number of plants**
* Two divisions are considered different if at least one divider position differs

Return the **number of valid ways** to divide the corridor, modulo
`10^9 + 7`.
If it is impossible, return `0`.

---

## **Key Insight**

The problem looks complex, but it simplifies once we observe that:

1. **Seats determine validity**

   * Each section must contain exactly **two seats**
   * The total number of seats must be **even**
2. **Plants only create flexibility**

   * Plants do not affect whether a section is valid
   * They only affect **how many choices** we have for placing dividers
3. The corridor can be seen as a sequence of **seat pairs**

   * The number of ways depends on how many plants lie **between consecutive seat pairs**

This turns the problem into a **combinatorics counting problem**, not a partitioning or DP problem.

---

## **Approach**

### 1. Count Total Seats

Let `totalSeats` be the number of `'S'` characters in the corridor.

* If `totalSeats == 0` → return `0`
* If `totalSeats` is **odd** → return `0`

Otherwise, the corridor must be divided into:

```
totalSeats / 2
```

valid sections.

---

### 2. Traverse and Group Seats

Traverse the corridor from left to right while counting seats:

* Every **two seats** complete one section
* When a new section starts, the previous section has ended
* Any plants between these two sections determine where a divider can be placed

---

### 3. Count Divider Choices

For each gap between two consecutive seat-pairs:

* Let `k` be the number of plants between them
* There are:

```
k + 1
```

possible positions to place a divider

The final answer is the **product of all such choices**, modulo `10^9 + 7`.

---

## **Example**

### Example 1

**Input**

```
corridor = "SSPPSPS"
```

**Explanation**

Seat grouping:

```
[S S] P P [S P S]
```

Between the two seat-pairs, there are `2` plants.

Number of ways:

```
2 + 1 = 3
```

**Output**

```
3
```

---

### Example 2

**Input**

```
corridor = "PPSPSP"
```

There are exactly two seats, so the entire corridor forms one valid section.
No additional dividers can be placed.

**Output**

```
1
```

---

### Example 3

**Input**

```
corridor = "S"
```

Only one seat exists, so it is impossible to form a valid section.

**Output**

```
0
```

---

## **Why This Works**

The solution works because:

* Seats fully define the **structure** of the corridor
* Plants only contribute **independent choices**
* Each divider decision is independent of the others
* The total number of ways follows directly from the **rule of product**

By separating **structural constraints** (seats) from **combinatorial freedom** (plants), the problem becomes both simpler and efficient.

---

## **Complexity**

* **Time Complexity:** `O(n)`

  * Single pass through the corridor
* **Space Complexity:** `O(1)`

  * Only constant extra variables are used

This easily satisfies the constraint `n ≤ 10^5`.

---

## **What I Learned**

* How to reduce a seemingly complex partitioning problem to a counting problem
* Why identifying **invariant elements** (seats) is crucial in greedy solutions
* That many Hard problems hide simple math behind long descriptions
* How combinatorics can replace dynamic programming when decisions are independent
