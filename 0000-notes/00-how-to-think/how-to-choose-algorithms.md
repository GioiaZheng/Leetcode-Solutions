# How to Choose the Right Algorithm  

This note is written for beginners who often feel:

- “I understand the problem, but I don’t know which algorithm to use”
- “There are too many techniques — how am I supposed to choose?”
- “Why do solutions always use methods I never think of?”

If this sounds familiar, this note is for you.

---

## 1. The uncomfortable truth (and good news)

Most beginners believe:

> “Good programmers immediately know which algorithm to use.”

This is **false**.

In reality, good programmers:
- narrow down possibilities
- eliminate wrong options
- test simple ideas first

Algorithm selection is not intuition — it is **process of elimination**.

---

## 2. Why beginners feel overwhelmed

Beginners usually face two problems:

1. They know **too many algorithm names**, but
2. They don’t know **when NOT to use them**

So everything feels possible:
- DP? Maybe.
- Greedy? Not sure.
- Binary search? Could be.
- Hash table? Always?

This note will teach you how to **systematically rule things out**.

---

## 3. The first and most important rule

> **Never choose an algorithm before understanding the input structure.**

Input structure already removes many options.

### Examples

- String → graph algorithms are unlikely
- Sorted array → binary search becomes a candidate
- Tree → recursion / DFS / BFS become natural

If you skip this step, algorithm choice becomes guessing.

---

## 4. Think in terms of “problem shapes”, not algorithm names

Instead of asking:
> “Which algorithm should I use?”

Ask:
> “What kind of problem shape is this?”

### Common problem shapes

| Problem shape | Typical meaning |
|--------------|----------------|
| Contiguous segment | sliding window, prefix sum |
| Pair / triple relationships | hashing, sorting |
| Optimal value | DP or greedy |
| Feasibility check | binary search on answer |
| Count number of ways | DP or combinatorics |

Algorithms are just **tools for shapes**.

---

## 5. The elimination method (VERY IMPORTANT)

Instead of finding the correct algorithm, do this:

> **Actively eliminate impossible or unreasonable ones**

### Example: substring problem

If the problem asks about:
> substring / subarray

You can eliminate:
- graph algorithms ❌
- tree DP ❌
- random backtracking ❌

Now only a few options remain:
- sliding window
- prefix sum
- brute force (for small n)

This is how professionals think.

---

## 6. A beginner-friendly decision flow

When you finish reading a problem, go through this order:

### Step 1 — Is the data contiguous?
- Yes → sliding window / prefix sum
- No → sorting / hashing / DP

---

### Step 2 — Is the input sorted or monotonic?
- Yes → binary search becomes possible
- No → binary search is unlikely

---

### Step 3 — Are we optimizing something?
(max / min / longest / shortest)

- Yes → greedy or DP
- No → simulation or counting

---

### Step 4 — Are constraints changing dynamically?
(e.g. “at most k”, “no more than”, “window must stay valid”)

- Yes → sliding window
- No → static methods

---

## 7. When NOT to use Dynamic Programming

Beginners overuse DP.

You should **avoid DP** when:
- the problem is one-pass
- decisions do not affect future states
- greedy works

DP is powerful but **expensive mentally**.

If you can solve it without DP, you probably should.

---

## 8. When NOT to use Greedy

Greedy feels tempting because it is simple.

Greedy often fails when:
- local choices affect future options
- the problem requires global optimality
- the problem asks for “number of ways”

If you cannot explain *why* greedy works, be suspicious.

---

## 9. Why reading solutions helps (if done correctly)

Reading solutions is useful only if you ask:

- Why this algorithm fits the problem shape?
- What alternatives were possible but rejected?
- What property makes this solution valid?

Do NOT just memorize code.

---

## 10. A safe beginner mindset

When choosing algorithms, aim for:

> “I can justify why this approach makes sense.”

Not:
> “I hope this is the right one.”

Confidence comes from **reasoning**, not speed.

---

## 11. Practice: what should you think first?

When you see a new problem, ask yourself:

1. What is the input type?
2. Is order important?
3. Is it contiguous?
4. Am I finding, counting, or checking?
5. What can I immediately eliminate?

If you can answer these, you are already thinking correctly.

---

## 12. What comes next

Now that you know:
- how to read problems
- how to choose algorithms

The next step is learning your **first core technique**:

➡️ **Arrays & basic traversal**

This is covered in:

➡️ `01-array/array-basics.md`

---

## Final note

Choosing the right algorithm is not about being fast.

It is about being **methodical**.

And that is a skill you are actively building.
