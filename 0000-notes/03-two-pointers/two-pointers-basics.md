# Two Pointers Basics  

This note is written for beginners who think:

- “I know how to use a loop, why do I need two pointers?”
- “Two pointers feels like a trick, not a real method”
- “I always get confused about left and right movement”

If this sounds familiar, this note is for you.

---

## 1. What is the core idea of two pointers?

The idea is simple:

> Instead of looking at the array from one position,  
> **look at it from two positions at the same time.**

These two positions (pointers) give you **more information** with the same time complexity.

---

## 2. When should you think about two pointers?

You should consider two pointers when:

- The input is an array or string
- Order matters
- You are comparing elements or ranges
- You want to avoid nested loops

Typical goals:
- shrink or expand a range
- compare two elements
- maintain a condition

---

## 3. Two main types of two pointers

### Type 1 — Opposite direction pointers

One pointer starts at the left, one at the right.

```text
L → → → ← ← ← R
````

Common use cases:

* sorted arrays
* pair sum problems
* reversing arrays
* palindrome checking

---

### Type 2 — Same direction pointers

Both pointers move from left to right, but at different speeds or roles.

```text
slow → → →  
fast → → → → →
```

Common use cases:

* removing duplicates
* partitioning arrays
* fast/slow pointer patterns

---

## 4. Why two pointers reduce time complexity

Many beginners start with:

```python
for i in range(n):
    for j in range(n):
        ...
```

This is often **O(n²)**.

Two pointers often allow:

* one pass
* each pointer moves at most n times

Total time: **O(n)**

This is not magic — it works because pointers never move backward unnecessarily.

---

## 5. Opposite direction pointers: how to think

When using left/right pointers, always ask:

> “Which side should move, and why?”

Movement is based on **what information you gain** by moving a pointer.

Example logic:

* If current sum is too large → move right pointer
* If current sum is too small → move left pointer

Movement must be **justified**, not guessed.

---

## 6. Same direction pointers: the slow-fast mindset

In same-direction pointers, roles matter more than position.

Typical roles:

* `fast`: explores new elements
* `slow`: maintains the valid structure

Example:

* `fast` scans
* `slow` marks where to write or keep elements

This is the core idea behind:

* removing duplicates
* filtering elements in-place

---

## 7. Canonical templates (Python)

### Opposite direction template

```python
left = 0
right = n - 1

while left < right:
    if condition_met(nums[left], nums[right]):
        # do something
        left += 1
        right -= 1
    elif need_move_left:
        left += 1
    else:
        right -= 1
```

---

### Same direction template

```python
slow = 0

for fast in range(n):
    if is_valid(nums[fast]):
        nums[slow] = nums[fast]
        slow += 1
```

Key idea:

* `fast` always moves
* `slow` moves only when condition is satisfied

---

## 8. Common beginner mistakes

### Mistake 1: Moving both pointers blindly

Always explain **why** a pointer moves.

### Mistake 2: Losing track of pointer roles

If you forget what `slow` represents, logic breaks.

### Mistake 3: Using two pointers when order doesn’t matter

If order doesn’t matter, hashing or sorting may be simpler.

---

## 9. How two pointers relate to sliding window

Sliding window is a **special case** of two pointers.

Difference:

* two pointers: general movement
* sliding window: window must stay valid

If you understand two pointers, sliding window becomes easier.

---

## 10. Beginner practice checklist

Before coding, ask:

* What does each pointer represent?
* Under what condition does each pointer move?
* Is each pointer moving forward only?

If you can answer these, your solution is likely correct.

---

## 11. Related problems in this repository

Practice two pointers with:

* `0026-remove-duplicates-from-sorted-array`
* `0027-remove-element`
* `0005-longest-palindromic-substring`
* `0028-find-the-index-of-the-first-occurrence-in-a-string`

---

## Final reminder

Two pointers are not about being clever.

They are about **seeing two sides of the same data at once**.

Once this clicks, many problems suddenly feel easier.
