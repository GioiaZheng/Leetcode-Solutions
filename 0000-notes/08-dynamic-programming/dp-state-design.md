# Dynamic Programming — State Design  

This note is written for beginners who feel:

- “I understand DP in theory, but I can’t design states”
- “My dp has too many dimensions”
- “I don’t know what dp[i] should mean”

If this sounds familiar, this note is for you.

---

## 1. Why state design is the hardest part

In DP:
- code is mechanical
- transitions are logical
- **state design is conceptual**

If the state is wrong:
- transitions become messy
- bugs multiply
- solution collapses

So we must design the state **before writing code**.

---

## 2. The golden rule of DP state design

> **One DP state = one clear subproblem**

If you cannot describe `dp[state]` in one clean sentence,
the state is not ready.

---

## 3. The first question to ask

Always start with:

> “What information must I remember to make future decisions?”

Not:
- “What dimensions should dp have?”
- “What have others done?”

Only remember **what is necessary**.

---

## 4. The most common DP state patterns

### Pattern 1 — Position-based DP

```text
dp[i] = best result considering the first i elements
````

This is the **most beginner-friendly** pattern.

Used when:

* data is sequential
* order matters

---

### Pattern 2 — Choice-based DP

```text
dp[i] = best result ending exactly at position i
```

Used when:

* the answer must include position i
* local decisions matter

---

### Pattern 3 — Count-based DP

```text
dp[i] = number of ways to reach state i
```

Used when:

* counting paths
* counting partitions
* counting combinations

---

## 5. One-dimensional DP (start here)

If your state depends only on:

* previous one or two positions

Then **1D DP is enough**.

Example:

```text
dp[i] depends on dp[i-1], dp[i-2]
```

Never jump to 2D DP unless forced.

---

## 6. When do you need multi-dimensional DP?

You need more dimensions when:

* more than one independent variable affects decisions

Example:

```text
dp[i][j] = best result using first i items with capacity j
```

Each dimension must represent **independent information**.

---

## 7. Avoiding state explosion (very important)

Beginner mistake:

> “Let me add one more dimension to be safe.”

This is dangerous.

Before adding a dimension, ask:

* Can this be derived from existing state?
* Can this be handled in transition instead?

If yes → do NOT add a dimension.

---

## 8. State meaning must be consistent

Once you define:

```text
dp[i] = best result using first i elements
```

You must:

* always interpret dp[i] the same way
* never change its meaning mid-solution

Inconsistent meaning = bugs.

---

## 9. Base cases follow from state meaning

Base cases are not guessed.

They are implied.

Example:

```text
dp[0] = best result using zero elements
```

This is usually:

* 0 (for max / min)
* 1 (for counting ways)

Let the definition guide you.

---

## 10. A step-by-step state design process

For any DP problem:

1. Describe the full problem in one sentence
2. Describe a smaller version of the problem
3. Define dp[state] as that smaller problem
4. Check if dp[state] can build the full answer

If step 3 is unclear, stop.

---

## 11. Common beginner mistakes

### Mistake 1: State describes too much

Simplify.

### Mistake 2: State describes too little

Add only what is necessary.

### Mistake 3: Mixing state and transition

State = “what I know”
Transition = “what I do”

---

## 12. How DP state design connects to everything else

DP states often mirror:

* array prefixes
* window endpoints
* greedy choices (but with memory)

DP is structured thinking, not brute force.

---

## 13. Beginner checklist

Before coding DP, confirm:

* Can I explain dp[state] in one sentence?
* Does each dimension represent necessary info?
* Do base cases follow naturally?

If yes → you are ready to code.

---

## Final reminder

Good DP solutions feel simple **after** state design.

If DP feels messy,
the state is almost always the problem.
