# Difference Array  

This note is written for beginners who feel:

- “I understand prefix sum, but difference array feels mysterious”
- “Why do people update only two positions?”
- “Range updates always confuse me”

If this sounds familiar, this note is for you.

---

## 1. What problem does the difference array solve?

Difference array solves this core problem:

> **Many range updates, but few final queries**

Instead of updating every element in a range again and again,
we record **where changes start and where they end**.

---

## 2. Intuitive idea (no math)

Imagine this task:

> “Add +10 to days 2 through 5”

Brute force:
- update day 2, 3, 4, 5 ❌

Difference idea:
- mark “+10 starts at day 2”
- mark “+10 ends after day 5”

Everything in between is affected automatically.

---

## 3. Difference array explained in one sentence

Given an array `nums`,  
the difference array `diff` stores:

> **how much the value changes at each position**

---

## 4. How difference array is defined

Given:
```text
nums: [a, b, c, d]
````

Difference array:

```text
diff[0] = a
diff[1] = b - a
diff[2] = c - b
diff[3] = d - c
```

Reconstruction:

```text
nums[i] = diff[0] + diff[1] + ... + diff[i]
```

👉 This is just a prefix sum!

---

## 5. Why difference array helps with range updates

Suppose we want to:

> add `x` to all elements in range `[l, r]`

Instead of updating all elements:

* do `diff[l] += x`
* do `diff[r + 1] -= x` (if exists)

That’s it.

Later, prefix sum reconstructs the final array.

---

## 6. Canonical Python template

### Step 1: Initialize diff array

```python
diff = [0] * (n + 1)
```

---

### Step 2: Apply range updates

```python
diff[l] += x
diff[r + 1] -= x
```

---

### Step 3: Recover final array

```python
nums = [0] * n
running = 0

for i in range(n):
    running += diff[i]
    nums[i] = running
```

This pattern appears again and again.

---

## 7. When should you think of difference array?

Think of difference array when:

* The problem has **many range updates**
* Final values are needed after all updates
* Direct updates would be too slow

If updates ≫ queries, difference array is perfect.

---

## 8. Difference array vs prefix sum

| Prefix Sum    | Difference Array |
| ------------- | ---------------- |
| Fast queries  | Fast updates     |
| Slow updates  | O(1) updates     |
| Query-focused | Update-focused   |

They are two sides of the same idea.

---

## 9. Common beginner mistakes

### Mistake 1: Forgetting r + 1 boundary

Always check array bounds.

### Mistake 2: Updating original array instead of diff

All updates go to `diff`, not `nums`.

### Mistake 3: Forgetting reconstruction

`diff` is not the final answer.

---

## 10. Real problem intuition

Difference array is useful when:

* updates overlap
* effects accumulate
* order of updates doesn’t matter

It turns chaos into structure.

---

## 11. Beginner checklist

Before using difference array, ask:

* Are there many range updates?
* Can I delay computing final values?
* Do updates overlap heavily?

If yes → difference array is a strong candidate.

---

## 12. Related problems in this repository

Practice difference array ideas with:

* range update style problems
* interval marking problems
* cumulative effect simulations

(Some problems combine difference array + prefix sum.)

---

## Final reminder

Difference array is not hard.

It is just:

> **prefix sum used in reverse**

Once you see this,
range update problems stop being scary.
