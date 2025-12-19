# Binary Search on Array  

This note is written for beginners who feel:

- “I know binary search is O(log n), but I don’t really get why it works”
- “I always mess up left / right boundaries”
- “There are too many templates and I don’t know which one to use”

If this sounds familiar, this note is for you.

---

## 1. What problem does binary search solve?

Binary search solves one specific type of problem:

> **Find a target in a sorted or monotonic structure**

Key requirement:
- the search space must be **ordered**
- or have a **monotonic property**

If this is not true, binary search does not apply.

---

## 2. The real idea behind binary search (important)

Binary search is NOT about “splitting in half”.

It is about this invariant:

> **The answer is always inside the current search interval.**

Each step:
- checks the middle
- removes the half that cannot contain the answer

The interval keeps shrinking, but **never loses the answer**.

---

## 3. When should you think of binary search?

Think of binary search when:

- The array is sorted
- The problem says:
  - first / last occurrence
  - minimum / maximum valid index
  - lower bound / upper bound
- The answer moves monotonically

If you can say:
> “If this index works, all indices on one side also work”

Binary search is a candidate.

---

## 4. Understanding boundaries before code

Most bugs come from boundaries, not logic.

Two common interval styles:

### Style 1 — Left-closed, right-closed `[l, r]`

- both ends included
- loop condition: `l <= r`

### Style 2 — Left-closed, right-open `[l, r)`

- left included, right excluded
- loop condition: `l < r`

Both work — **but never mix them**.

---

## 5. Recommended beginner style: `[l, r)`

This style avoids many off-by-one errors.

Initialization:
```python
l = 0
r = n
````

Invariant:

> answer ∈ [l, r)

Loop:

```python
while l < r:
    mid = (l + r) // 2
    ...
```

---

## 6. Canonical Python template (search exact value)

```python
l = 0
r = n

while l < r:
    mid = (l + r) // 2
    if nums[mid] < target:
        l = mid + 1
    else:
        r = mid

# l is the smallest index where nums[l] >= target
```

After the loop:

* `l` is the **lower bound**
* always check if it equals the target

---

## 7. Why this template works

Each iteration:

* reduces the interval size
* keeps the invariant true

No element is skipped.
No infinite loop.

This is why consistency matters more than memorizing code.

---

## 8. First occurrence vs last occurrence

Binary search is often used to find:

* first index ≥ target
* last index ≤ target

These are boundary problems, not equality problems.

The trick:

* modify the comparison
* not the loop structure

---

## 9. Common beginner mistakes

### Mistake 1: Using `(l + r) / 2`

Use integer division.

### Mistake 2: Updating both sides incorrectly

Only one boundary moves per iteration.

### Mistake 3: Forgetting post-check

Binary search narrows the range, but you still need to verify.

---

## 10. Binary search vs linear scan

| Linear scan    | Binary search         |
| -------------- | --------------------- |
| O(n)           | O(log n)              |
| Simple         | Needs order           |
| No constraints | Requires monotonicity |

Binary search is powerful **because order gives information**.

---

## 11. Beginner checklist

Before using binary search, ask:

* Is the data sorted or monotonic?
* Can I define a valid search interval?
* Does the answer move in one direction?

If yes → binary search is appropriate.

---

## 12. Related problems in this repository

Practice binary search on array with:

* `0004-median-of-two-sorted-arrays`
* `0028-find-the-index-of-the-first-occurrence-in-a-string`
* `0912-sort-an-array`
* `2141-maximum-running-time-of-n-computers`

---

## Final reminder

Binary search is not about speed.

It is about **logical elimination**.

Once you trust the invariant,
binary search stops being scary.
