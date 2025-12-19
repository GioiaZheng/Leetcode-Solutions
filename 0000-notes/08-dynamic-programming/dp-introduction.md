# Dynamic Programming — Introduction  

This note is written for beginners who feel:

- “DP looks scary and abstract”
- “I never know when a problem needs DP”
- “States, transitions, tables… everything feels overwhelming”

If this sounds familiar, this note is for you.

---

## 1. What problem does DP solve?

Dynamic Programming solves problems where:

> **The same subproblems appear again and again.**

Instead of solving them repeatedly,
we solve each subproblem **once** and remember the result.

---

## 2. The simplest DP idea (no tables yet)

Imagine this question:

> “What is the best result up to position i?”

If:
- the answer at position `i`
- depends on answers at earlier positions

Then DP is a natural fit.

DP is about **building answers step by step**.

---

## 3. DP vs Greedy (very important difference)

| Greedy | DP |
|------|----|
| One safe choice | Many possible choices |
| No regret | Choices affect future |
| Simple logic | Structured reasoning |
| Fast | Slower but reliable |

Rule of thumb:
> If a local choice might hurt future options → DP.

---

## 4. When should you think of DP?

Think of DP when:

- The problem asks for:
  - maximum / minimum
  - number of ways
- Decisions affect future decisions
- Brute force recursion has overlapping subproblems

Classic hints:
- “longest”
- “optimal”
- “count all possible”
- “can be achieved in how many ways”

---

## 5. The core DP question

Every DP problem starts with one question:

> **What does `dp[i]` represent?**

If you cannot answer this clearly,
you are not ready to write DP yet.

---

## 6. A beginner-friendly DP definition

A DP state should:

- have a clear meaning
- represent a subproblem
- be easy to transition from

Example:
```text
dp[i] = best result using the first i elements
````

This single sentence defines your entire DP.

---

## 7. Transitions: how states connect

Once `dp[i]` is defined, ask:

> “How do I get `dp[i]` from earlier states?”

This is called the **transition**.

Example:

```text
dp[i] = max(dp[i-1], dp[i-2] + value[i])
```

Transitions encode your choices.

---

## 8. Base cases (often forgotten)

DP must start somewhere.

Always define:

* smallest input
* simplest case

Example:

```text
dp[0] = 0
dp[1] = value[1]
```

Without base cases, DP collapses.

---

## 9. DP is just optimized recursion

Think of DP as:

* recursion → overlapping subproblems ❌
* DP → remember results ✅

Two styles:

* Top-down (recursion + memo)
* Bottom-up (table filling)

Both are valid.

---

## 10. Common beginner mistakes

### Mistake 1: Jumping to code too early

Define state and transition first.

### Mistake 2: Overcomplicating state

If your state has too many dimensions, rethink.

### Mistake 3: Forgetting what dp means

If you lose track of the state meaning, bugs appear.

---

## 11. How DP connects to previous topics

DP builds on:

* arrays (dp table)
* prefix ideas (accumulation)
* greedy thinking (choices)

DP is not isolated — it is a **structured extension**.

---

## 12. Beginner checklist

Before coding DP, ask:

* What is my state?
* What choices exist?
* What is the transition?
* What are the base cases?

If you can answer all four, DP is doable.

---

## 13. Related problems in this repository

DP appears in many forms here:

* `3573-best-time-to-buy-and-sell-stock-v`
* `2435-paths-in-matrix-divisible-by-k`
* `3578-count-partitions-with-max-min-difference-at-most-k`
* stock trading problems
* counting paths / partitions

---

## Final reminder

DP is not about memorizing formulas.

It is about:

> **breaking a big problem into smaller, reusable answers**

Once that mindset clicks,
DP becomes systematic — not scary.
