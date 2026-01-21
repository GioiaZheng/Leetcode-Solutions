# **LeetCode 3315 – Construct the Minimum Bitwise Array II**

**Difficulty:** Medium  
**Tags:** Bit Manipulation, Greedy  
**Link:** https://leetcode.com/problems/construct-the-minimum-bitwise-array-ii/

---

## **Problem Summary**

You are given an array `nums` consisting of **prime integers**.

Your task is to construct an array `ans` of the same length such that for every index `i`:

```

ans[i] OR (ans[i] + 1) == nums[i]

```

Additional requirements:

- Each `ans[i]` must be the **minimum possible value** satisfying the condition.
- If no such value exists, set `ans[i] = -1`.

Each position can be solved **independently**.

---

## **Key Observations**

### 1️⃣ Even numbers have no solution

The expression:
```

x OR (x + 1)

```
is **always odd**.

Therefore:
- If `nums[i]` is even → impossible
- Since `nums[i]` is prime, the only even case is `nums[i] = 2`

So:
```

nums[i] == 2 → ans[i] = -1

```

---

### 2️⃣ Binary behavior of `x OR (x + 1)`

When adding `1` to a number `x`:
- All **trailing `1`s** become `0`
- The first `0` bit to the left becomes `1`

As a result:
```

x OR (x + 1)

```
produces a number whose lower bits form a block of consecutive `1`s.

---

## **Core Insight**

To make:
```

x OR (x + 1) == n

```
and minimize `x`, we need to **reverse this bit effect**.

### Key rule:

> For an **odd** number `n`, find the **lowest `0` bit** in its binary representation  
> (counting from the right, 0-indexed, call it `pos`).

Then the minimum valid value is:
```

x = n - 2^(pos - 1)

```

This removes just enough bits to make `x` minimal, while ensuring:
```

x OR (x + 1) = n

```

---

## **Why This Works**

- The lowest `0` bit in `n` determines where the carry from `x + 1` must occur
- Clearing `2^(pos - 1)` ensures:
  - Lower bits turn into `1`s after OR
  - Higher bits remain unchanged
- Any smaller `x` would fail to reconstruct `n`

This greedy choice is **both correct and optimal**.

---

## **Examples**

### Example 1
```

nums = [2, 3, 5, 7]

```

| n | Binary | Lowest 0 bit | ans | Check |
|---|--------|--------------|-----|------|
| 2 | 10 | — | -1 | ❌ |
| 3 | 11 | pos=2 | 1 | 1 OR 2 = 3 |
| 5 | 101 | pos=1 | 4 | 4 OR 5 = 5 |
| 7 | 111 | pos=3 | 3 | 3 OR 4 = 7 |

Output:
```

[-1, 1, 4, 3]

```

---

### Example 2
```

nums = [11, 13, 31]

```

| n | Binary | Lowest 0 bit | ans |
|---|--------|--------------|-----|
| 11 | 1011 | pos=2 | 9 |
| 13 | 1101 | pos=1 | 12 |
| 31 | 11111 | pos=5 | 15 |

Output:
```

[9, 12, 15]

```

---

## **Algorithm**

For each number `n` in `nums`:

1. If `n` is even:
```

ans = -1

````
2. Otherwise:
- Find the lowest position `pos` where bit is `0`
- Compute:
  ```
  ans = n - (1 << (pos - 1))
  ```

---

## **Complexity Analysis**

Let `B = bit-length of nums[i]` (≤ 30 since `nums[i] ≤ 10^9`).

| Aspect | Complexity                  |
| ------ | --------------------------- |
| Time   | **O(n · B)**                |
| Space  | **O(1)** (excluding output) |

---

## **Common Pitfalls**

* ❌ Clearing all trailing `1`s (may produce `0`, invalid)
* ❌ Using `n & (n - 1)` blindly (not minimal for all cases)
* ❌ Forgetting that minimization matters
* ❌ Treating even numbers as solvable

---

## **What I Learned**

* Bitwise OR with consecutive numbers has strict structural rules
* The *lowest zero bit* is often more important than the lowest one bit
* Greedy bit manipulation can give exact minimal solutions
* Understanding carry propagation is crucial in bit problems

---

## **Related Problems**

* 3314. Construct the Minimum Bitwise Array I
* 231. Power of Two
* 268. Missing Number

---

## **One-Line Interview Summary**

> “For odd `n`, find the lowest zero bit and subtract `2^(pos−1)` to obtain the minimum `x` such that `x | (x+1) = n`; even `n` has no solution.”
