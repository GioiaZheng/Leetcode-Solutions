# **LeetCode 3512 – Minimum Operations to Make Array Sum Divisible by K**

**Difficulty:** Easy  
**Tags:** Math, Greedy, Modular Arithmetic  
**Link:** https://leetcode.com/problems/minimum-operations-to-make-array-sum-divisible-by-k/

---

## **Problem Summary**

You are given:
- An integer array `nums`
- An integer `k`

You can perform the following operation any number of times:

> Select an index `i` and replace `nums[i]` with `nums[i] - 1`.

Your goal is to find the **minimum number of operations** needed to make the **sum of the array divisible by `k`**.

---

## **Key Insight**

Each operation:
- Decreases the **total sum by exactly 1**

So the problem reduces to:

> **How many times do we need to subtract 1 from the total sum so that it becomes divisible by `k`?**

---

## **Mathematical Reformulation**

Let:
```

S = sum(nums)

```

If:
```

S % k == 0

```
👉 Already divisible → **answer = 0**

Otherwise:
```

S % k = r

```

To make `S` divisible by `k`, we must subtract exactly `r` from the sum.

Since each operation subtracts `1`:
```

minimum operations = r

```

---

## **Why This Always Works**

- You are allowed to apply operations to **any element**
- You can distribute decrements across elements arbitrarily
- In the worst case, you can reduce all numbers to zero
- There is **no restriction** preventing these operations

So the minimum number of operations is purely determined by **modulo arithmetic**, not by array structure.

---

## **Approach**

### Step 1: Compute Total Sum
```

S = sum(nums)

```

---

### Step 2: Compute Remainder
```

r = S % k

```

---

### Step 3: Return Result
- If `r == 0` → return `0`
- Else → return `r`

---

## **Example Walkthrough**

### Example 1
```

nums = [3,9,7], k = 5
sum = 19
19 % 5 = 4

```

Subtract 4 → new sum = 15 → divisible  
 Answer = `4`

---

### Example 2
```

nums = [4,1,3], k = 4
sum = 8
8 % 4 = 0

```

Already divisible  
 Answer = `0`

---

### Example 3
```

nums = [3,2], k = 6
sum = 5
5 % 6 = 5

````

Subtract 5 → new sum = 0 → divisible  
 Answer = `5`

---

## **Complexity Analysis**

Let `n = len(nums)`.

| Aspect | Complexity |
| ------ | ---------- |
| Time   | **O(n)**   |
| Space  | **O(1)**   |

---

## **What I Learned**

* Sometimes array problems reduce to **pure math**
* Understanding what each operation does globally is key
* Modular arithmetic can greatly simplify “minimum operations” problems
* Always check whether element-level choices actually matter

---

## **Related Problems**

* 1590. Make Sum Divisible by P
* 523. Continuous Subarray Sum
* 974. Subarray Sums Divisible by K

---

## **One-Line Interview Summary**

> “Each operation reduces the total sum by one, so the minimum operations needed is simply `sum(nums) % k`.”
