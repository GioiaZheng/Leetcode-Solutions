# How to Choose the Right Algorithm  

This note is written for learners who feel:

- “I know many algorithms, but I don’t know which one to use”
- “I often start with brute force and get stuck”
- “I want a decision process, not guesses”

If this sounds familiar, this note is for you.

---

## 1. The biggest mistake beginners make

Beginners usually ask:

> “Which algorithm should I use?”

This is the wrong first question.

The right first question is:

> **“What is this problem REALLY asking?”**

Algorithm choice comes **after** understanding the goal.

---

## 2. Always start with the problem goal

Every problem asks one of these:

- Reachability → can I get there?
- Distance → how far / how many steps?
- Optimal value → max / min
- Counting → how many ways?
- Validation → is this possible?

Identify the goal first.  
This already eliminates many algorithms.

---

## 3. The high-level decision flow (IMPORTANT)

Use this order when reading a problem:

1. Is this about **relationships / movement / reachability**?
   → Graph

2. Is this about **ranges / windows / contiguous segments**?
   → Sliding Window / Prefix Sum

3. Is this about **existence / frequency / mapping**?
   → Hash Table

4. Is this about **maximum / minimum with choices affecting future**?
   → DP

5. Is this about **minimum / maximum feasible value**?
   → Binary Search on Answer

6. Is a **local choice provably safe**?
   → Greedy

This flow saves enormous time.

---

## 4. BFS vs DFS vs Union-Find (graph family)

### Use BFS when:
- minimum steps
- shortest path (unweighted)

### Use DFS when:
- explore everything
- count components
- detect cycles

### Use Union-Find when:
- only care about connectivity
- edges are added dynamically

If you choose the wrong one, performance or correctness breaks.

---

## 5. DP vs Greedy (the classic confusion)

Ask this key question:

> **“Can a local decision ever hurt a future decision?”**

- If **no** → Greedy
- If **yes / maybe** → DP

If you’re unsure, DP is safer.

---

## 6. Binary Search: array vs answer

### Binary search on array:
- array is sorted
- find index / boundary

### Binary search on answer:
- answer space is numeric
- feasibility is monotonic

If you’re searching for a **value**, not a position → answer BS.

---

## 7. Sliding Window vs Prefix Sum

### Sliding Window:
- dynamic window
- condition maintained while moving
- usually O(n)

### Prefix Sum:
- static ranges
- many queries
- precompute once

If the window size changes dynamically → sliding window.

---

## 8. Counting problems: DP or math?

If counting:
- with constraints / choices → DP
- simple formula / parity → math

Don’t over-DP simple math problems.

---

## 9. Red flags that hint specific algorithms

- “minimum steps” → BFS
- “dependencies / prerequisites” → Topological Sort
- “connected components” → DFS / Union-Find
- “maximum subarray / subsequence” → DP
- “top K” → Heap / Bucket
- “range updates” → Difference Array

Train yourself to notice these phrases.

---

## 10. A safe default strategy (very practical)

If stuck:

1. Write brute force idea
2. Identify repeated work
3. Ask: can I remember something?
   - yes → DP / Hash
4. Ask: is order monotonic?
   - yes → Binary Search

This prevents panic.

---

## 11. Common beginner failure patterns

- Jumping to code immediately
- Forcing DP everywhere
- Ignoring problem constraints
- Using BFS where weights exist
- Overcomplicating state

Slow down. Think first.

---

## 12. How this connects to this repository

This repo is structured exactly around this guide:

- Array / Two Pointers
- Sliding Window
- Hash Table
- Prefix Sum
- Binary Search
- Greedy
- DP
- Graph

You are building **a mental map**, not memorizing tricks.

---

## Final reminder

Strong problem solvers do not know “more algorithms”.

They:
> **choose the right one faster**

This guide is about building that instinct.
