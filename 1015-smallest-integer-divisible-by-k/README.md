# **LeetCode 1015 – Smallest Integer Divisible by K**

**Difficulty:** Medium  
**Tags:** Math, Modulo, BFS / Simulation  
**Link:** https://leetcode.com/problems/smallest-integer-divisible-by-k/

---

## **Problem Summary**

You are given a positive integer `k`.

You need to find the **length** of the smallest positive integer `n` such that:

- `n` is **divisible by `k`**
- `n` contains **only the digit `1`**  
  (i.e. `1`, `11`, `111`, `1111`, ...)

If no such number exists, return **`-1`**.

⚠️ Note:  
The number `n` itself may be extremely large, so you **must not construct it directly**.

---

## **Key Insight**

We are looking for a number of the form:

```

1
11
111
1111
...

```

These numbers grow exponentially, so storing them as integers is impossible.

### 👉 Trick: **Only track remainders modulo `k`**

If we know:
```

current_remainder = x % k

```

Then appending a digit `1` gives:
```

new_remainder = (x * 10 + 1) % k

```

So we can simulate the process **without ever building the number**.

---

## **Important Observation (Early Exit)**

If `k` is divisible by **2 or 5**, then:

- Any number made only of `1`s **cannot** be divisible by `k`
- Because such numbers are **never even** and **never end in 0 or 5**

So:
```

if k % 2 == 0 or k % 5 == 0 → return -1

```

---

## **Algorithm**

1. If `k % 2 == 0` or `k % 5 == 0`, return `-1`
2. Initialize:
```

remainder = 0

````
3. For length `i = 1` to `k`:
- Update:
  ```
  remainder = (remainder * 10 + 1) % k
  ```
- If `remainder == 0`, return `i`
4. If no remainder becomes `0` after `k` steps, return `-1`

Why at most `k` steps?
- There are only `k` possible remainders (`0` to `k-1`)
- If we repeat a remainder, we are in a loop and will never reach `0`

---

## **Example Walkthrough**

### Example 1
```
k = 3
```

Simulation:

```
1   % 3 = 1
11  % 3 = 2
111 % 3 = 0  ✅
```

Answer: `3`

---

### Example 2
```

k = 2

````

`k % 2 == 0` → impossible  
Answer: `-1`

---
## **Why This Works**

* We avoid large numbers by using modulo arithmetic
* Each step simulates appending a `1`
* Pigeonhole principle guarantees termination
* Efficient even for `k = 100000`

---

## **Complexity Analysis**

| Aspect | Complexity |
| ------ | ---------- |
| Time   | **O(k)**   |
| Space  | **O(1)**   |

---

## **Common Pitfalls**

* ❌ Trying to build the actual number `n`
* ❌ Forgetting the `k % 2 == 0 or k % 5 == 0` shortcut
* ❌ Infinite loop without limiting steps to `k`
* ❌ Using recursion (unnecessary)

---

## **What I Learned**

* Modulo arithmetic can simulate huge numbers safely
* Repetition + pigeonhole principle guarantees termination
* Sometimes the answer is about **length**, not the number itself
* Early mathematical pruning saves a lot of time

---

## **Related Problems**

* 166. Fraction to Recurring Decimal
* 202. Happy Number
* 974. Subarray Sums Divisible by K

---

## **One-Line Interview Summary**

> “Simulate appending digit `1` using modulo arithmetic; if remainder becomes zero within `k` steps, return the length, otherwise return `-1`.”
