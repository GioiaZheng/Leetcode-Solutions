# Two Pointers Basics

This note is written for beginners who think:

- â€œI know how to use a loop, why do I need two pointers?â€
- â€œTwo pointers feels like a trick, not a real methodâ€
- â€œI always get confused about left and right movementâ€

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

### Type 1 â€” Opposite direction pointers

One pointer starts at the left, one at the right.

```text
L â†’ â†’ â†’ â† â† â† R
````

Common use cases:

* sorted arrays
* pair sum problems
* reversing arrays
* palindrome checking

---

### Type 2 â€” Same direction pointers

Both pointers move from left to right, but at different speeds or roles.

```text
slow â†’ â†’ â†’
fast â†’ â†’ â†’ â†’ â†’
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

This is often **O(nÂ²)**.

Two pointers often allow:

* one pass
* each pointer moves at most n times

Total time: **O(n)**

This is not magic â€” it works because pointers never move backward unnecessarily.

---

## 5. Opposite direction pointers: how to think

When using left/right pointers, always ask:

> â€œWhich side should move, and why?â€

Movement is based on **what information you gain** by moving a pointer.

Example logic:

* If current sum is too large â†’ move right pointer
* If current sum is too small â†’ move left pointer

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

### Mistake 3: Using two pointers when order doesnâ€™t matter

If order doesnâ€™t matter, hashing or sorting may be simpler.

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

---

## Interview quick reference

### Pattern description
Use two indices to avoid checking every pair or every rewritten position. The pointers usually either move toward each other (`left`, `right`) or move together with different roles (`slow`, `fast`).

### When to use it
- Sorted array pair/triplet problems.
- Palindrome or container-style left/right comparisons.
- In-place filtering, compaction, or duplicate removal.
- Problems where each element should be visited at most a constant number of times.

### Template code

```python
# Opposite directions on sorted input
left, right = 0, len(nums) - 1
while left < right:
    total = nums[left] + nums[right]
    if total == target:
        return [left, right]
    if total < target:
        left += 1
    else:
        right -= 1

# Same direction / write pointer
write = 0
for read, value in enumerate(nums):
    if keep(value):
        nums[write] = value
        write += 1
return write
```

### Common pitfalls
- Moving both pointers without a proof.
- Forgetting to skip duplicates in `3sum`-style problems.
- Using two pointers before sorting when the movement logic requires sorted order.
- Losing the meaning of `slow` / `write` in in-place problems.

### Linked solved problems
- [`0015-3sum`](../../problems/0015-3sum/)
- [`0011-container-with-most-water`](../../problems/0011-container-with-most-water/)
- [`0026-remove-duplicates-from-sorted-array`](../../problems/0026-remove-duplicates-from-sorted-array/)
- [`1877-minimize-maximum-pair-sum-in-array`](../../problems/1877-minimize-maximum-pair-sum-in-array/)
