# Bucket Technique  

This note is written for beginners who feel:

- “I’ve seen ‘bucket’ in solutions, but I don’t really get it”
- “Bucket sort sounds complicated and mathematical”
- “Why not just sort everything?”

If this sounds familiar, this note is for you.

---

## 1. What problem does the bucket technique solve?

The bucket technique solves this problem:

> **Too many elements to compare directly**

Instead of comparing everything with everything,
we **split data into groups (buckets)** and work inside each group.

---

## 2. Intuitive idea (no algorithms yet)

Imagine sorting exam scores from 0 to 100.

Instead of sorting all students together, you:
- put scores 0–9 in bucket 0
- put scores 10–19 in bucket 1
- ...
- put scores 90–100 in bucket 9

Now:
- each bucket is small
- order becomes easier to manage

This is the core intuition.

---

## 3. When should you think about buckets?

Think about buckets when:

- The value range is limited or structured
- You care about **relative positions**, not exact order
- The problem asks for:
  - gaps
  - groups
  - top K elements

Buckets are especially useful when:
> **sorting feels too slow or unnecessary**

---

## 4. Bucket vs sorting (big picture)

| Sorting | Bucket |
|------|------|
| Compare elements | Group elements |
| O(n log n) | Often O(n) |
| Simple logic | More design |
| General purpose | Problem-specific |

Buckets trade **generality** for **efficiency**.

---

## 5. The core bucket design questions

Before using buckets, always answer:

1. How many buckets do I need?
2. What does each bucket represent?
3. How do I map an element to a bucket?

If you cannot answer these, stop.

---

## 6. Example: Maximum Gap (intuition only)

Problem:
> Find the maximum difference between adjacent elements in sorted order.

Key insight:
- If numbers are spread out, the maximum gap must be **between buckets**, not inside them.

Bucket idea:
- each bucket stores:
  - minimum value
  - maximum value
- ignore inner order

Then:
- compute gaps between consecutive buckets

This avoids full sorting.

---

## 7. Example: Top K Frequent Elements

Bucket idea:
- frequency range is limited (1 to n)
- create buckets indexed by frequency
- each bucket stores elements with that frequency

Then:
- iterate from highest frequency bucket down

This avoids sorting by frequency.

---

## 8. Common beginner mistakes

### Mistake 1: Using too many buckets
Too many buckets = wasted space.

### Mistake 2: Using buckets without value range
If values are unbounded, bucket logic breaks.

### Mistake 3: Overengineering
If sorting is simple enough, do not force buckets.

---

## 9. Bucket technique vs heap

Both are used for top-K problems.

| Bucket | Heap |
|------|------|
| O(n) | O(n log k) |
| More memory | Less memory |
| Needs range | No range needed |

Choose based on constraints.

---

## 10. How buckets connect to hashing

Buckets often use:
- arrays (index = bucket)
- hash tables (dynamic buckets)

They combine well with frequency counting.

---

## 11. Beginner checklist

Before using buckets, ask:
- Is there a natural grouping?
- Is value range manageable?
- Do I need full sorting?

If yes → bucket technique may help.

---

## 12. Related problems in this repository

Practice bucket technique with:

- `0164-maximum-gap`
- `0347-top-k-frequent-elements`
- `0451-sort-characters-by-frequency`
- `0692-top-k-frequent-words`
- `0220-contains-duplicate-iii`

---

## Final reminder

Buckets are not advanced magic.

They are simply:
> **structure before computation**

Once you see grouping opportunities,
many “hard” problems become manageable.
