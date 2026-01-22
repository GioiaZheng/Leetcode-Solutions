# **LeetCode 3507 – Minimum Pair Removal to Sort Array I**

**Difficulty:** Easy  
**Tags:** Simulation, Greedy, Array  
**Link:** https://leetcode.com/problems/minimum-pair-removal-to-sort-array-i/

---

## **Problem Summary**

You are given an integer array `nums`.

You can perform the following operation any number of times:

1. Select the **adjacent pair with the minimum sum**
2. If multiple such pairs exist, choose the **leftmost one**
3. Replace the pair with their **sum**

Your goal is to return the **minimum number of operations** needed to make the array **non-decreasing**.

An array is **non-decreasing** if:
```

nums[i] >= nums[i - 1]  for all valid i

```

---

## **Key Insight**

This is a **pure simulation + greedy** problem.

Important constraints:
- `nums.length ≤ 50` → brute-force simulation is feasible
- The operation is **fully deterministic**:
  - You must always choose the adjacent pair with the **minimum sum**
  - Ties are broken by choosing the **leftmost pair**

So there is **no decision branching** — just simulate exactly what the problem describes.

---

## **Approach**

### Step 1: Check if the array is already sorted
If `nums` is already non-decreasing, return `0`.

---

### Step 2: Repeat the operation until sorted
While the array is **not non-decreasing**:

1. Scan all adjacent pairs
2. Find the pair with the **minimum sum**
   - If multiple, pick the **leftmost**
3. Replace the pair with their sum
4. Increment operation count

---

### Step 3: Return the operation count
Since each operation reduces the array length by 1, the loop is guaranteed to terminate.

---

## **Why This Works**

- The operation rule is **strictly defined**, so no alternative strategies exist
- Each operation reduces array size → finite process
- Small constraints make repeated scanning acceptable
- Greedy choice is enforced by the problem statement

---

## **Example Walkthrough**

### Example 1
```

nums = [5, 2, 3, 1]

```

**Step 1**
Adjacent sums:
- (5,2) → 7
- (2,3) → 5
- (3,1) → 4  ← minimum

Replace `(3,1)`:
```

[5, 2, 4]

```

**Step 2**
Adjacent sums:
- (5,2) → 7
- (2,4) → 6  ← minimum

Replace `(2,4)`:
```

[5, 6]

```

Array is now non-decreasing → stop

✅ Output = `2`

---

### Example 2
```

nums = [1, 2, 2]

````

Already non-decreasing → `0`

---

## **Complexity Analysis**

Let `n = len(nums)`.

* Each operation scans `O(n)` pairs
* At most `n - 1` operations

| Aspect | Complexity |
| ------ | ---------- |
| Time   | **O(n²)**  |
| Space  | **O(n)**   |

With `n ≤ 50`, this is easily fast enough.

---

## **Common Pitfalls**

* ❌ Trying to “optimize” the choice (you are not allowed to)
* ❌ Forgetting tie-breaking must choose the **leftmost**
* ❌ Assuming the result is unique without simulation
* ❌ Overthinking — this is not DP or heap-based

---

## **What I Learned**

* Some greedy problems give **no freedom of choice**
* When constraints are small, direct simulation is best
* Always re-check sortedness after each operation
* Deterministic rules → deterministic simulation

---

## **Related Problems**

* 948. Bag of Tokens
* 1475. Final Prices With a Special Discount
* 228. Summary Ranges

---

## **One-Line Interview Summary**

> “Repeatedly simulate the given operation: always merge the leftmost adjacent pair with minimum sum until the array becomes non-decreasing.”
