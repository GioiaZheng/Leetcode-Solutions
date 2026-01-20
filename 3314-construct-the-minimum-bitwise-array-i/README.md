# **LeetCode 3314 – Construct the Minimum Bitwise Array I**

**Difficulty:** Easy  
**Tags:** Bit Manipulation, Greedy  
**Link:** https://leetcode.com/problems/construct-the-minimum-bitwise-array-i/

---

## **Problem Summary**

You are given an array `nums` of **prime integers**.

You need to construct an array `ans` such that for every index `i`:

```

ans[i] OR (ans[i] + 1) == nums[i]

```

Among all valid choices, `ans[i]` must be the **minimum possible value**.

If it is **impossible** to find such a value, set:
```

ans[i] = -1

```

Each index is handled **independently**.

---

## **Key Observations**

### 1️⃣ Even numbers are impossible

The expression:
```

x OR (x + 1)

```
is **always odd**.

Therefore:
- If `nums[i]` is even → **no solution**
- Since `nums[i]` is prime, this only happens when `nums[i] == 2`

---

### 2️⃣ Binary behavior of `x OR (x + 1)`

Adding `1` to a number:
- Flips all **trailing `1`s** to `0`
- Turns the first `0` (from right) into `1`

As a result:
```

x OR (x + 1)

```
produces a number where:
- All bits **to the right of the lowest zero bit in `x` become `1`**

This means the result has the form:
```

xxxxx0111...111

```

---

## **Core Insight**

To make:
```

x OR (x + 1) == n

```
and **minimize `x`**, we must reverse the process:

> **Find the lowest `0` bit in `n` and subtract `2^(pos - 1)`**

where:
- `pos` = index (0-based, from right) of the **lowest zero bit** in `n`

This gives the **smallest possible `x`** that reconstructs `n` via OR.

---

## **Algorithm**

For each number `n` in `nums`:

1. If `n` is even:
```

ans = -1

````
2. Otherwise:
- Find the **lowest bit position `pos`** where `n` has a `0`
- Compute:
  ```
  ans = n - (1 << (pos - 1))
  ```

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

````

---

## **Why This Works**

* `x OR (x + 1)` always produces a number with trailing `1`s
* Matching `n` means controlling **where that trailing block starts**
* The **lowest zero bit** of `n` determines this boundary
* Subtracting `2^(pos - 1)` minimizes `x` while keeping correctness

---

## **Complexity Analysis**

Let `B` be the bit-length of numbers (`≤ 10` since `nums[i] ≤ 1000`).

| Aspect | Complexity                 |
| ------ | -------------------------- |
| Time   | **O(n · B)**               |
| Space  | **O(1)** (output excluded) |

---

## **Common Pitfalls**

* ❌ Clearing all trailing `1`s (may produce `0`, invalid)
* ❌ Using `n & (n - 1)` blindly (not minimal for all cases)
* ❌ Treating all odd numbers the same
* ❌ Forgetting that **minimization** is required

---

## **What I Learned**

* Bitwise operations follow strict, exploitable patterns
* Understanding binary carry behavior is crucial
* “Minimum valid value” often means **remove just enough bits**
* Edge cases (like `111...111`) matter a lot in bit problems

---

## **One-Line Interview Summary**

> “For odd `n`, find the lowest zero bit and subtract `2^(pos−1)` to get the minimum `x` such that `x | (x+1) = n`; even `n` has no solution.”
