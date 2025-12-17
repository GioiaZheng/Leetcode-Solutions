# How to Read LeetCode Problems  

This note is written for **absolute beginners**.

If you often feel:
- “I understand every word, but I don’t know what to do”
- “I stare at the problem for 10 minutes and my brain is blank”
- “I read the solution and think: how did anyone think of that?”

Then this file is for you.

---

## 1. The biggest misunderstanding beginners have

Most beginners think:

> “I can’t solve this problem because I don’t know enough algorithms.”

But in reality, the real problem is usually:

> **You don’t know how to *read* the problem yet.**

Reading a coding problem is a **skill**, not a talent.

---

## 2. What “reading a problem” actually means

Reading a problem is NOT:
- translating English into your language
- understanding the story
- knowing what the output looks like

Reading a problem means answering **three hidden questions**:

1. What is the **input structure**?
2. What kind of **output** is required?
3. What is the **relationship** between input and output?

Until these three are clear, **do not think about algorithms**.

---

## 3. Step 1 — Identify the input type (MOST IMPORTANT)

Always start by asking:

> “What form is the input?”

Common input types:
- Array / List of numbers
- String
- Matrix (2D array)
- Linked List
- Tree / Graph

### Why this matters

Each input type **limits** the possible algorithms.

Example:
- String → sliding window, two pointers, frequency counting
- Sorted array → binary search
- Tree → DFS / BFS / recursion

📌 **Algorithm choice is not magic — it is constrained by input structure.**

---

## 4. Step 2 — Look for keywords that hint at thinking direction

Certain words appear again and again in problems.

### Common keywords and what they suggest

| Keyword | Often suggests |
|------|------|
| contiguous / substring / subarray | sliding window |
| sorted | binary search |
| at most / at least | sliding window, prefix sum |
| maximum / minimum | greedy, DP |
| number of ways | DP, combinatorics |
| exactly k | transform into “at most k” |

⚠️ Keywords do not give answers, but they **narrow the search space**.

---

## 5. Step 3 — Identify what is being optimized or checked

Ask yourself:

> “Is the problem asking me to **find**, **count**, or **verify** something?”

### Three major categories

1. **Find**
   - maximum length
   - minimum cost
   - earliest / latest position

2. **Count**
   - number of ways
   - number of valid subarrays

3. **Verify**
   - is it possible?
   - does there exist?

Different categories often lead to different techniques.

---

## 6. Step 4 — Ignore constraints at first (seriously)

Beginners often panic when they see:

```

1 <= n <= 10^5

```

For now:
- Ignore performance
- Focus on understanding the task

First ask:
> “If n were small, what would I do?”

A slow but correct idea is **always better** than no idea.

Optimization comes later.

---

## 7. Step 5 — Rephrase the problem in your own words

If you cannot rephrase the problem, you **do not understand it yet**.

Example:

Original:
> Return the length of the longest substring without repeating characters.

Rephrased:
> I need the longest continuous part of the string where every character appears only once.

If you can’t do this step, stop and reread.

---

## 8. A beginner-safe reading checklist

Before thinking about algorithms, confirm you can answer:

- [ ] What is the input type?
- [ ] What is the output?
- [ ] Is order important?
- [ ] Is the data contiguous?
- [ ] Am I finding, counting, or checking?
- [ ] Can I describe the problem in one sentence?

If any answer is “I’m not sure” → **do not move on yet**.

---

## 9. Why solutions look “obvious” after you read them

When you read a solution, your brain sees:
- the cleaned-up idea
- the final abstraction
- no confusion

You don’t see:
- the wrong ideas
- the dead ends
- the trial-and-error

So don’t compare your **starting point** to someone else’s **ending point**.

---

## 10. What comes next

After learning how to read problems, the next step is:

> **How to choose the right algorithm once the problem is clear**

That is covered in the next note:

➡️ `how-to-choose-algorithms.md`

---

## Final reminder

Struggling to understand a problem does NOT mean you are bad at programming.

It means:
> You are still learning how to *think* in problem-solving terms.

And that is exactly what this series is for.
