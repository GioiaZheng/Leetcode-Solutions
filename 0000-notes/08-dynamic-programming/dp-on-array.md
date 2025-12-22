# Dynamic Programming on Arrays  

This note is written for beginners who feel:

- “I understand DP states, but I still don’t know how to start coding”
- “Array DP problems all look different”
- “I don’t know when a simple array problem becomes DP”

If this sounds familiar, this note is for you.

---

## 1. Why array-based DP is the best starting point

Most DP problems:
- start with arrays
- use indices as states
- build answers from left to right

If you are comfortable with array traversal,
array DP is just **one extra layer of memory**.

---

## 2. The core question for array DP

Before writing DP, always ask:

> **“What is the best / number of ways ending at index i?”**

This single question generates many classic DP problems.

---

## 3. The most common array DP state

The safest and most common definition is:

```text
dp[i] = the best result ending at index i
````

Key property:

* the answer **must include** element `i`
* dp[i] depends on earlier dp values

This makes transitions natural.

---

## 4. Canonical 1D array DP template

```python
dp = [0] * n
dp[0] = base_value

for i in range(1, n):
    dp[i] = transition(dp, i)

answer = max(dp)
```

This structure appears again and again.

---

## 5. Example thinking: Maximum Subarray (intuition)

Question:

> “What is the maximum subarray sum?”

Human thinking:

* At position `i`, either:

  * start a new subarray at `i`
  * or extend the best subarray ending at `i-1`

DP definition:

```text
dp[i] = max subarray sum ending at i
```

Transition:

```text
dp[i] = max(nums[i], dp[i-1] + nums[i])
```

This is DP, not magic.

---

## 6. From one-pass to DP: what changes?

| One-pass     | DP                 |
| ------------ | ------------------ |
| Forget past  | Remember best past |
| Local update | State transition   |
| No memory    | Explicit memory    |

DP is just **remembering more**.

---

## 7. Counting-style array DP

Array DP is also used for counting.

Example state:

```text
dp[i] = number of ways to reach index i
```

Typical transition:

```text
dp[i] = dp[i-1] + dp[i-2]
```

(Fibonacci-style problems)

---

## 8. Space optimization (important but later)

Many array DP problems only depend on:

* dp[i-1]
* dp[i-2]

So you can reduce space:

```python
prev2, prev1 = base_cases
for i in range(n):
    curr = transition(prev1, prev2)
    prev2 = prev1
    prev1 = curr
```

Always write full DP first, optimize later.

---

## 9. Common beginner mistakes

### Mistake 1: Wrong dp meaning

If dp[i] sometimes includes i and sometimes doesn’t → wrong.

### Mistake 2: Forgetting to take max over dp

Some answers are `dp[n-1]`, others are `max(dp)`.

### Mistake 3: Overcomplicating transitions

Keep transitions simple and readable.

---

## 10. How array DP connects to previous techniques

Array DP often combines with:

* prefix sum (fast accumulation)
* greedy ideas (local vs global)
* sliding window (limited memory)

DP is not isolated — it builds on basics.

---

## 11. Beginner checklist

Before coding array DP, confirm:

* dp[i] has a clear meaning
* dp[i] depends only on earlier indices
* base cases are correct

If yes → coding is mechanical.

---

## 12. Related problems in this repository

Practice array DP with:

* `3573-best-time-to-buy-and-sell-stock-v`
* classic maximum subarray problems
* counting sequences problems
* stock trading DP variants

---

## Final reminder

Array DP is not a new skill.

It is:

> **array traversal + remembering the right thing**

Once this clicks,
DP becomes systematic instead of scary.
