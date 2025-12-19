# Interval Greedy  

This note is written for beginners who feel:

- “Interval problems all look different”
- “Sometimes sort by start, sometimes by end — I’m confused”
- “I don’t know why greedy works here”

If this sounds familiar, this note is for you.

---

## 1. What are interval problems?

Interval problems involve **ranges**:

```text
[start, end]
````

They usually describe:

* time periods
* segments
* ranges of validity

Typical questions:

* How many intervals can I select?
* How many intervals overlap?
* How many intervals do I need to remove?

---

## 2. The most important observation

For interval problems, **the order of decisions matters**.

If you choose a bad interval early,
you may block many good intervals later.

So the key question is:

> **Which interval is the “least harmful” to pick first?**

---

## 3. The greedy answer (core insight)

In most interval problems, the safest choice is:

> **Pick the interval that ends the earliest.**

Why?

* It finishes quickly
* It leaves the most room for future intervals
* It blocks the fewest options

This is a classic **greedy-safe choice**.

---

## 4. The canonical interval greedy pattern

### Step 1 — Sort intervals by end time

```python
intervals.sort(key=lambda x: x[1])
```

---

### Step 2 — Iterate and select greedily

```python
count = 0
current_end = -infinity

for start, end in intervals:
    if start >= current_end:
        count += 1
        current_end = end
```

This simple structure appears everywhere.

---

## 5. Why sorting by start time is often wrong

Sorting by start time answers:

> “Who begins earliest?”

But that does **not** guarantee minimal blocking.

Example intuition:

* An interval that starts early but ends late
* Blocks many short intervals after it

Ending time matters more than starting time.

---

## 6. Common types of interval greedy problems

### Type 1 — Maximum number of non-overlapping intervals

→ Sort by end time, pick greedily

---

### Type 2 — Minimum number of intervals to remove

→ Total intervals − maximum non-overlapping set

---

### Type 3 — Minimum number of resources

(meeting rooms, platforms)
→ Often greedy + heap

---

## 7. Why interval greedy is provably correct

Informal proof idea (exchange argument):

* Suppose an optimal solution picks interval A first
* Greedy picks interval B, which ends earlier than A
* Replace A with B
* You never reduce the number of remaining choices

So greedy does not hurt optimality.

---

## 8. Common beginner mistakes

### Mistake 1: Using `>` instead of `>=`

Be careful with boundary definitions.

### Mistake 2: Forgetting to sort

Greedy without order is guessing.

### Mistake 3: Mixing problem goals

Make sure you know whether you’re counting kept or removed intervals.

---

## 9. Variants that look different but are the same

Many problems hide interval greedy behind stories:

* meetings
* tasks
* segments
* collisions
* scheduling

Ignore the story — focus on `[start, end]`.

---

## 10. How interval greedy combines with other tools

Interval greedy often combines with:

* sorting
* heap (for overlapping counts)
* binary search (advanced scheduling)

But the **core decision** stays the same.

---

## 11. Beginner checklist

Before using interval greedy, ask:

* Can I model this as intervals?
* Does choosing earlier-ending intervals help?
* Can I justify that choice?

If yes → interval greedy applies.

---

## 12. Related problems in this repository

Practice interval greedy with:

* `2147-number-of-ways-to-divide-a-long-corridor`
* `2211-count-collisions-on-a-road`
* meeting / scheduling style problems
* overlap counting problems

---

## Final reminder

Interval greedy works because:

> **time is a limited resource**

The earlier you finish,
the more future you keep available.
