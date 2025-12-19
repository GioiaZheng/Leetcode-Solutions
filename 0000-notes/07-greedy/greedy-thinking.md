# Greedy Thinking  

This note is written for beginners who feel:

- “Greedy sounds too simple to be reliable”
- “I don’t know when greedy is correct”
- “I often guess greedy and get WA”

If this sounds familiar, this note is for you.

---

## 1. What problem does greedy solve?

Greedy solves problems where:

> **A locally optimal choice leads to a globally optimal result.**

That sentence sounds abstract, so let’s translate it:

- You make a decision step by step
- Once you make a decision, you never need to change it
- That decision will not hurt the final answer

If these are true, greedy may work.

---

## 2. The biggest misunderstanding about greedy

Beginners think greedy means:

> “Pick the best-looking option right now.”

This is **wrong**.

Greedy actually means:

> “Pick an option that can be proven to be safe.”

Greedy is about **proof**, not intuition.

---

## 3. When should you even consider greedy?

Think about greedy when:

- The problem asks for:
  - maximum / minimum
  - earliest / latest
  - longest / shortest
- Decisions are made in sequence
- You do not need to revisit past decisions

Typical examples:
- interval scheduling
- resource allocation
- choosing items under constraints

---

## 4. The key greedy question (VERY IMPORTANT)

Before using greedy, ask:

> **“If I make this choice now, could it ever block a better solution later?”**

If the answer is “no”, greedy is promising.

If the answer is “maybe”, greedy is dangerous.

---

## 5. Intuitive example: interval scheduling

Problem:
> Select the maximum number of non-overlapping intervals.

Greedy choice:
- always pick the interval that ends earliest

Why this works:
- ending earlier leaves more room for future intervals
- no future choice is harmed

This is a **provably safe choice**.

---

## 6. What greedy problems usually have in common

Greedy problems often have:

- a clear ordering (sort by something)
- a one-pass decision process
- a “best-so-far” variable

If sorting is the first step, greedy is often involved.

---

## 7. Greedy vs Dynamic Programming

| Greedy | DP |
|------|----|
| Simple | Complex |
| Fast | Slower |
| Hard to prove | Always correct |
| One path | Many states |

Rule of thumb:
> If greedy works, use it.  
> If not, DP is the fallback.

---

## 8. Common beginner mistakes

### Mistake 1: Using greedy without proof
If you cannot explain *why* it works, don’t trust it.

### Mistake 2: Confusing greedy with heuristics
Greedy is exact, not approximate.

### Mistake 3: Forcing greedy when DP is needed
Some problems need future knowledge.

---

## 9. How greedy connects to other techniques

Greedy often combines with:
- sorting
- priority queues
- binary search (feasibility)
- prefix sums

It rarely appears alone.

---

## 10. How to “prove” greedy (beginner-friendly)

You don’t need formal math.

Just answer:
- If two solutions differ at this step,
- does my greedy choice always leave at least as good a future?

This is often called an **exchange argument**.

---

## 11. Beginner checklist

Before using greedy, ask:
- Is there a clear decision at each step?
- Can I sort or order choices?
- Can I justify why my choice is safe?

If yes → greedy may apply.

---

## 12. Related problems in this repository

Practice greedy thinking with:

- `2147-number-of-ways-to-divide-a-long-corridor`
- `2211-count-collisions-on-a-road`
- `2141-maximum-running-time-of-n-computers`
- interval and scheduling-style problems

---

## Final reminder

Greedy is not about luck.

It is about **making choices you never regret**.

Once you learn to recognize those moments,
greedy becomes one of the most elegant tools you have.
