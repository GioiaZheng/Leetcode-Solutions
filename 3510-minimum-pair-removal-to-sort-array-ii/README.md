# **LeetCode 3510 – Minimum Pair Removal to Sort Array II**

**Difficulty:** Hard
**Tags:** Greedy, Heap, Linked List, Simulation
**Link:** [https://leetcode.com/problems/minimum-pair-removal-to-sort-array-ii/](https://leetcode.com/problems/minimum-pair-removal-to-sort-array-ii/)

---

## **Problem Summary**

You are given an integer array `nums`.

You can repeatedly perform the following operation:

1. Select the **adjacent pair with the minimum sum**

   * If multiple pairs have the same minimum sum, choose the **leftmost** one.
2. Replace the pair with their sum.

Your task is to return the **minimum number of operations** required to make the array **non-decreasing**.

An array is non-decreasing if:

```
nums[i] <= nums[i+1] for all valid i
```

---

## **Key Insight (Why This Is Hard)**

This problem is **not** about sorting, and it is **not** about counting inversions.

The difficulty comes from **two strict constraints happening at the same time**:

1. **The merge order is forced**

   * At every step, you *must* merge the globally smallest adjacent pair.
   * You are not allowed to choose where to fix the order.

2. **The structure of the array keeps changing**

   * After each merge:

     * Indices shift
     * Adjacencies change
     * Previously computed information becomes invalid

Because of this:

  *  ❌ You **cannot** greedily fix local inversions
  *  ❌ You **cannot** maintain inversion count (`violations`) as an answer
  *  ❌ You **cannot** stop early based on heuristics

You must **faithfully simulate the process**.

---

## **Correct Strategy Overview**

To solve this problem correctly, we must:

1. **Always merge the current smallest adjacent pair**
2. **Efficiently update the array structure**
3. **Stop immediately once the array becomes non-decreasing**

This leads to a **lazy simulation approach** using:

* **Min-Heap** → to find the smallest adjacent pair
* **Doubly Linked List (via arrays)** → to maintain adjacency after merges
* **Local inversion tracking (`bad`)** → to know when the array becomes valid

---

## **Data Structures Used**

### 1️⃣ Doubly Linked List (via arrays)

Instead of actually deleting elements:

* `prev[i]` → index of previous alive element
* `nxt[i]` → index of next alive element
* `removed[i]` → whether index `i` has been merged away

This allows **O(1)** structural updates per merge.

---

### 2️⃣ Min-Heap for Adjacent Pairs

Each heap entry is:

```
(sum_of_pair, left_index)
```

However, because the array changes over time:

> **Heap entries can become stale**

So every popped pair must be validated before use.

---

### 3️⃣ Inversion Counter (`bad`)

We maintain:

```
bad = number of i such that nums[i] > nums[next(i)]
```

Important rule:

> `bad` is **only** used as a *loop condition*,
> **never** as a direct answer indicator.

---

## **Algorithm Steps**

### Step 1: Initialization

* Build linked list structure
* Count initial inversions (`bad`)
* If already non-decreasing → return `0`
* Push all adjacent pairs into the heap

---

### Step 2: Forced Merge Loop

While `bad > 0`:

1. Pop from heap until a **valid adjacent pair** is found:

   * Both indices are alive
   * They are still adjacent
   * Their current sum matches the heap value

2. Before merging:

   * Remove inversion contributions involving the pair

3. Merge the pair:

   * Replace left value with sum
   * Remove right index from linked list

4. After merging:

   * Add new inversion contributions
   * Push new adjacent pairs into heap

5. Increment operation count

---

### Step 3: Termination

* As soon as `bad == 0`, stop
* Return number of operations performed

---

## **Why This Works**

* The heap guarantees **correct merge order**
* Lazy validation prevents using outdated pairs
* The linked list guarantees **correct adjacency**
* `bad` precisely tracks when the array becomes non-decreasing
* No guessing, no shortcuts, no over-merging

This exactly matches the problem’s rules.

---

## **Complexity Analysis**

Let `n = len(nums)`.

| Aspect                  | Complexity     |
| ----------------------- | -------------- |
| Heap operations         | **O(n log n)** |
| Each index removed once | **O(n)**       |
| Total time              | **O(n log n)** |
| Extra space             | **O(n)**       |

---

## **Common Pitfalls (What Fails)**

❌ Maintaining inversion count as the answer
❌ Trying to merge only where local inversions exist
❌ Ignoring stale heap entries
❌ Using monotonic stacks or prefix tricks
❌ Stopping early based on partial ordering

All of these will fail on edge cases.

---

## **One-Line Interview Summary**

> “This problem requires a full greedy simulation using a lazy min-heap and a linked list, because the merge order is forced and array structure changes dynamically.”
