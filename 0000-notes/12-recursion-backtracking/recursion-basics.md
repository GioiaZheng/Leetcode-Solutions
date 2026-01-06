# Recursion Basics  

This note is written for learners who feel:

- “I know recursion exists, but I don’t really understand it”
- “I can’t picture what happens when a function calls itself”
- “Backtracking problems scare me”

If this sounds familiar, start here.

---

## 1. What recursion really is (no code)

Recursion means:

> **Solving a problem by asking a smaller version of the same problem.**

That’s it.

Not loops.
Not magic.
Not stack tricks.

Just:
- same problem
- smaller input

---

## 2. The single most important rule

Every recursive solution MUST answer two questions:

1. **When do we stop?** → base case  
2. **How do we reduce the problem?** → recursive case

If either is missing:
- infinite recursion
- stack overflow
- wrong answer

---

## 3. Think in terms of “responsibility”

When writing a recursive function, never think about the whole problem.

Instead ask:

> **“What is THIS function call responsible for?”**

Example:
- `dfs(node)` is responsible for handling the subtree rooted at `node`
- `backtrack(path)` is responsible for exploring all solutions starting with `path`

Each call has a **limited, local responsibility**.

---

## 4. A mental model that actually works

Imagine recursion as:

> **delegation**

You don’t solve everything yourself.
You trust future calls to do their job.

This mindset is crucial.

---

## 5. The three components of recursion (ALWAYS present)

Every recursive solution has:

1. **Base case**
   - smallest input
   - stops recursion

2. **Recursive call**
   - calls itself on a smaller input

3. **Progress**
   - input size strictly decreases

If you can’t point to all three, your recursion is broken.

---

## 6. Simple example: sum of an array

Goal:
> Sum all elements in an array

Recursive idea:
- sum of array = first element + sum of the rest

```python
def array_sum(nums, i):
    if i == len(nums):
        return 0
    return nums[i] + array_sum(nums, i + 1)
````

Here:

* base case: `i == len(nums)`
* recursive case: `array_sum(nums, i + 1)`
* progress: `i` increases

---

## 7. What the call stack really means (important)

Each recursive call:

* pauses the current function
* waits for the result of the next call

Think of it as:

> **“I’ll finish my work after you finish yours.”**

No need to simulate the entire stack.
Just trust the return value.

---

## 8. Common beginner mistake #1 — Trying to track everything

Beginners often try to:

* simulate the entire recursion tree
* track all variable changes manually

This is unnecessary and confusing.

Correct approach:

> Focus only on ONE call’s responsibility.

---

## 9. Recursion vs iteration

| Recursion         | Iteration            |
| ----------------- | -------------------- |
| Delegation        | Manual control       |
| Natural for trees | Natural for arrays   |
| Uses call stack   | Uses explicit loop   |
| Clear logic       | Often more efficient |

Recursion is a **thinking tool**, not a performance trick.

---

## 10. When recursion is a good idea

Use recursion when:

* the problem is naturally hierarchical
* the input structure is recursive (tree, graph)
* the solution explores possibilities

Avoid recursion when:

* depth can be extremely large
* a simple loop is clearer

---

## 11. Common beginner mistake #2 — Missing base case

Symptoms:

* infinite recursion
* runtime error
* stack overflow

Rule:

> Always write the base case FIRST.

---

## 12. Common beginner mistake #3 — No progress

If the recursive call does not reduce the problem,
recursion will never end.

Always ask:

> “Is the next call closer to the base case?”

---

## 13. How recursion connects to backtracking

Backtracking is just:

> **recursion + choices**

You will:

* make a choice
* recurse
* undo the choice

But recursion itself is the foundation.

---

## 14. Beginner checklist (use this every time)

Before writing recursion, ask:

* What is the base case?
* What smaller problem am I calling?
* What is this function responsible for?

If you can answer these, recursion will work.

---

## Final reminder

Recursion is not about code.

It is about:

> **trusting smaller versions of the same problem**

Once you adopt this mindset,
backtracking and DFS become much easier.
