# Dynamic Programming — Summary  

This note is written for learners who feel:

- “I learned DP, but I’m afraid I’ll forget when to use it”
- “Sometimes greedy works, sometimes DP is needed — how do I tell?”
- “I want a checklist, not another long explanation”

If this sounds familiar, this summary is for you.

---

## 1. What DP really is (one sentence)

Dynamic Programming is:

> **Solving a big problem by solving smaller overlapping subproblems once, and remembering the results.**

Everything else is detail.

---

## 2. The three questions that define DP

Every DP problem answers these three questions:

1. **State** — What am I remembering?
2. **Transition** — How do I move from smaller problems to bigger ones?
3. **Base case** — Where does it start?

If any of these is unclear, DP will fail.

---

## 3. The most common DP state patterns

### Pattern A — Position-based

```text
dp[i] = best result using / ending at index i
````

Used for:

* array DP
* stock problems
* maximum subarray

---

### Pattern B — Prefix-based (2D)

```text
dp[i][j] = best result using first i and j elements
```

Used for:

* string DP
* LCS
* edit distance

---

### Pattern C — Range-based

```text
dp[l][r] = result for range [l, r]
```

Used for:

* palindrome problems
* interval DP

---

### Pattern D — Counting-based

```text
dp[i] = number of ways to reach state i
```

Used for:

* counting paths
* partitions
* combinations

---

## 4. DP vs Greedy vs Binary Search (VERY IMPORTANT)

### Use Greedy when:

* a local choice is provably safe
* decisions do not affect future options

### Use Binary Search when:

* the answer space is ordered
* feasibility is monotonic

### Use DP when:

* decisions affect future states
* greedy choices may block optimal solutions
* multiple paths must be considered

If you hesitate between greedy and DP → DP is safer.

---

## 5. A beginner-friendly DP decision flow

When you see a problem, ask in order:

1. Can I solve this with a one-pass greedy choice?
2. Can I binary search on the answer?
3. Do subproblems overlap?

If the answer to (3) is yes → DP.

---

## 6. Typical DP warning signs in problem statements

You should strongly suspect DP if the problem mentions:

* “maximum / minimum”
* “number of ways”
* “longest / shortest”
* “optimal”
* “all possible”

Especially when:

* brute force is exponential
* choices branch

---

## 7. Why DP feels hard (and why that’s normal)

DP feels hard because:

* you must think abstractly
* you must define states before coding
* bugs come from logic, not syntax

This is normal.
DP is a **thinking skill**, not a coding trick.

---

## 8. The correct way to practice DP

Bad practice:

* memorize solutions
* jump straight to code
* copy templates blindly

Good practice:

1. Define the state in words
2. Write transitions in math or plain English
3. Identify base cases
4. Then code

DP is designed, not typed.

---

## 9. Space optimization: when to care

Space optimization:

* is optional
* comes after correctness
* should never hide logic

Always write the clear DP first.
Optimize later.

---

## 10. Common DP failure patterns

* State meaning changes mid-solution
* Too many dimensions “just in case”
* Base cases guessed, not derived
* Transitions don’t match state meaning

If DP breaks, check these first.

---

## 11. How DP connects to everything else

DP is not isolated.

It builds on:

* arrays
* prefix ideas
* greedy reasoning
* binary search (sometimes)

DP is the **structured memory version** of all previous techniques.

---

## 12. Problems in this repository using DP

You have already encountered DP in:

* `3573-best-time-to-buy-and-sell-stock-v`
* `2435-paths-in-matrix-divisible-by-k`
* `3578-count-partitions-with-max-min-difference-at-most-k`
* string and counting problems

Revisit them with this summary in mind.

---

## Final reminder

DP is not something you “remember”.

It is something you **design**.

Once you learn to design DP states calmly,
DP becomes a powerful and reliable tool.
