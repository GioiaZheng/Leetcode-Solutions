# Prefix Sum  

This note is written for beginners who feel:

- “I’ve seen prefix sum formulas, but they feel abstract”
- “I don’t know when prefix sum is useful”
- “I confuse prefix sum with sliding window”

If this sounds familiar, this note is for you.

---

## 1. What problem does prefix sum solve?

Prefix sum solves one core problem:

> **Repeatedly asking about the sum (or count) of a range**

Instead of recalculating the same range again and again,
we **precompute cumulative information once**.

---

## 2. Intuitive idea (no math)

Imagine you have daily expenses:

```text
Day:    1  2  3  4  5
Money:  2  3  1  4  2
````

If someone asks:

* “How much did I spend from day 2 to day 4?”

You could:

* add 3 + 1 + 4 every time ❌

Or:

* keep a running total once ✅

Prefix sum is just **running total stored in an array**.

---

## 3. What exactly is a prefix sum?

Given an array `nums`:

```text
nums:        [a, b, c, d]
prefix_sum:  [a, a+b, a+b+c, a+b+c+d]
```

Each position stores:

> the sum of everything **before and including** it

---

## 4. Why prefix sum is powerful

With prefix sum:

* building it takes O(n)
* querying any range takes O(1)

This turns:

* nested loops ❌
  into:
* simple subtraction ✅

---

## 5. Canonical prefix sum construction (Python)

```python
prefix = [0] * (n + 1)

for i in range(n):
    prefix[i + 1] = prefix[i] + nums[i]
```

Important detail:

* `prefix[0] = 0`
* `prefix[i]` = sum of first `i` elements

This avoids edge cases.

---

## 6. Range sum using prefix sum

To get sum of `nums[l : r]` (inclusive):

```python
sum_lr = prefix[r + 1] - prefix[l]
```

This formula is the **entire point** of prefix sum.

---

## 7. When should you think of prefix sum?

Think of prefix sum when:

* The problem asks about:

  * range sum
  * number of subarrays
  * cumulative counts
* You see nested loops over ranges
* Sliding window feels hard or impossible

Prefix sum handles **static ranges** very well.

---

## 8. Prefix sum vs sliding window

| Prefix Sum        | Sliding Window      |
| ----------------- | ------------------- |
| Precompute once   | Update dynamically  |
| Static ranges     | Dynamic constraints |
| Easy counting     | Harder logic        |
| Needs extra space | O(1) space          |

They solve **different types of problems**.

---

## 9. Prefix sum + hash table (VERY IMPORTANT)

This is a powerful combination.

Idea:

* prefix sum turns range problems into differences
* hash table remembers previous prefix sums

Common pattern:

> “How many times have I seen this prefix sum before?”

This unlocks many Medium problems.

---

## 10. Classic example: subarray sum equals K

Key transformation:

```text
prefix[j] - prefix[i] = K
→ prefix[i] = prefix[j] - K
```

So for each prefix sum:

* check how many times `(current_sum - K)` appeared before

This avoids nested loops.

---

## 11. Common beginner mistakes

### Mistake 1: Off-by-one errors

Prefix arrays are usually length `n + 1`.

### Mistake 2: Forgetting prefix[0] = 0

This breaks subarrays starting at index 0.

### Mistake 3: Mixing indices and values

Prefix sum stores **aggregated values**, not positions.

---

## 12. Variants of prefix sum

Prefix sum can store:

* sum
* count
* parity (odd/even)
* frequency

It’s a general **accumulation technique**.

---

## 13. Beginner checklist

Before using prefix sum, ask:

* Am I repeatedly querying ranges?
* Can I precompute something once?
* Are ranges static?

If yes → prefix sum is a strong candidate.

---

## 14. Related problems in this repository

Practice prefix sum with:

* `1523-count-odd-numbers-in-an-interval-range`
* `3381-maximum-subarray-sum-with-length-divisible-by-k`
* `3432-count-partitions-with-even-sum-difference`
* `3583-count-special-triplets`
* `2435-paths-in-matrix-divisible-by-k`

---

## Final reminder

Prefix sum is not a formula to memorize.

It is a mindset:

> **do the work once, reuse it many times**

Once this clicks,
many counting problems become straightforward.
