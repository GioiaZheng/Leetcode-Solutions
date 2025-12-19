# Binary Search on Answer  

This note is written for beginners who feel:

- “The array is not sorted, so why can we use binary search?”
- “What does ‘binary search on answer’ even mean?”
- “These problems feel like magic solutions”

If this sounds familiar, this note is for you.

---

## 1. What problem does binary search on answer solve?

Binary search on answer solves problems like:

> **“Find the maximum / minimum value that is still possible.”**

Key difference:
- You are **not searching for an element**
- You are searching for a **value that satisfies a condition**

The array itself does not need to be sorted.

---

## 2. The key requirement (MOST IMPORTANT)

Binary search on answer requires **monotonicity**.

That means:
- If a value `x` is possible,
- then all values **on one side** of `x` are also possible.

This creates a **yes → yes → yes → no → no** pattern  
(or the reverse).

Without this property, binary search does not apply.

---

## 3. Intuitive example (no code)

Imagine this question:

> “How many hours can all computers run simultaneously?”

If:
- running for 3 hours is possible
- running for 2 hours is also possible
- but running for 10 hours is impossible

Then:
- possible hours form a continuous range

That’s exactly what binary search needs.

---

## 4. The core idea in one sentence

> **Binary search on answer = binary search on feasibility**

You are repeatedly asking:
> “Is this value feasible?”

And narrowing the range based on yes/no.

---

## 5. General problem structure

Most binary-search-on-answer problems follow this pattern:

1. Define the **answer range**
2. Define a **feasibility check**
3. Binary search on that range
4. Return the best feasible value

If you cannot clearly define step 2, stop.

---

## 6. Step 1 — Define the answer range

The answer range is usually:
- minimum possible value
- maximum possible value

Example:
- time → `[0, max_time]`
- capacity → `[max_item, sum_items]`

The range does not need to be tight, just correct.

---

## 7. Step 2 — Feasibility check (the hardest part)

A feasibility function answers:

> “Given value `x`, can we do it?”

Important rules:
- must be deterministic
- must be monotonic
- usually runs in O(n)

Example structure:

```python
def can(x):
    # simulate / greedy check
    return True or False
````

This function is the **heart of the solution**.

---

## 8. Step 3 — Binary search template (Python)

```python
l = low
r = high

while l < r:
    mid = (l + r + 1) // 2
    if can(mid):
        l = mid      # mid is feasible
    else:
        r = mid - 1  # mid is not feasible

return l
```

Key detail:

* use `(l + r + 1) // 2` to avoid infinite loops
* `l` always points to a feasible value

---

## 9. Why this works

Each iteration:

* tests feasibility
* discards half of the impossible range
* keeps all possible answers

This is exactly the same logic as classic binary search,
just applied to **values instead of indices**.

---

## 10. Common beginner mistakes

### Mistake 1: No monotonicity

If feasibility is not monotonic, binary search is invalid.

### Mistake 2: Feasibility too slow

If `can(x)` is O(n²), total complexity explodes.

### Mistake 3: Confusing simulation with optimization

The feasibility check should only answer yes/no,
not compute the final answer.

---

## 11. Classic problem types using this technique

Binary search on answer appears in:

* maximum / minimum capacity
* minimum time
* splitting arrays
* scheduling problems
* resource allocation

Once you see these themes, the pattern becomes obvious.

---

## 12. How this connects to greedy thinking

Most feasibility checks are **greedy**:

* allocate resources
* simulate consumption
* stop early if impossible

Binary search + greedy is a very powerful combo.

---

## 13. Beginner checklist

Before using binary search on answer, ask:

* Can I define a numeric answer range?
* Can I check feasibility for a given value?
* Is feasibility monotonic?

If yes → binary search on answer applies.

---

## 14. Related problems in this repository

Practice binary search on answer with:

* `2141-maximum-running-time-of-n-computers`
* `3577-count-the-number-of-computer-unlocking-permutations`
* `3573-best-time-to-buy-and-sell-stock-v` (conceptual)
* capacity / time allocation problems

---

## Final reminder

Binary search on answer is not a trick.

It is just:

> **asking the right yes/no question repeatedly**

Once you master this,
many “hard-looking” problems become systematic.
