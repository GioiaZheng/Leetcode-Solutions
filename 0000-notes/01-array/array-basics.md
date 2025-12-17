# Array Basics  

This note is written for beginners who think:

- “Arrays are easy, why do we need a note for this?”
- “I know how to loop through an array, but problems still feel hard”
- “I always mess up indices and boundaries”

If that sounds familiar, this note is for you.

---

## 1. What problems do arrays usually represent?

An array usually represents:

- a sequence
- a timeline
- an ordered list of values
- a step-by-step process

Examples:
- daily stock prices
- characters in a string
- scores over time
- events in order

📌 **Arrays are about order.**  
If order matters, arrays are usually involved.

---

## 2. The most important question when seeing an array

Before doing anything, ask:

> “Do I need to use the order, or can I ignore it?”

### If order matters:
- one-pass traversal
- sliding window
- prefix sum
- two pointers

### If order does NOT matter:
- sorting
- hashing
- counting frequency

Many wrong solutions come from answering this question incorrectly.

---

## 3. The core array mindset

When working with arrays, always think in terms of:

> **“What information do I know up to index i?”**

This question leads to:
- prefix sums
- running minimum / maximum
- dynamic programming
- greedy decisions

Array problems are often about **accumulating information** as you move forward.

---

## 4. One-pass traversal: the most powerful idea

The simplest and most powerful array pattern is:

> **Scan from left to right once**

Why this matters:
- O(n) time
- minimal complexity
- easier to reason about

### Basic template

```python
for i in range(n):
    # process nums[i]
````

Many beginners underestimate how much can be done in one pass.

---

## 5. What can be maintained during one pass?

While scanning the array, you can maintain:

* running sum
* current minimum / maximum
* count of elements
* frequency map
* best answer so far

### Example: running maximum

```python
current_max = float('-inf')

for x in nums:
    current_max = max(current_max, x)
```

This idea appears everywhere.

---

## 6. Index-based thinking (critical for beginners)

Array indices are **not just positions**.

They represent:

* time steps
* boundaries
* state transitions

Common index-related mistakes:

* off-by-one errors
* accessing out of bounds
* mixing indices and values

### Golden rule

> Always know whether a variable represents an **index** or a **value**.

If you confuse them, bugs follow.

---

## 7. Adjacent elements matter more than you think

Many array problems depend on relationships between neighbors:

* increasing / decreasing sequences
* differences between consecutive elements
* breaks in continuity

Example:

```python
nums[i] - nums[i - 1]
```

If a problem mentions:

* consecutive
* adjacent
* next to each other

Then neighbor relationships are key.

---

## 8. When arrays turn into something else

Sometimes array problems evolve into:

* sliding window → dynamic range
* prefix sum → fast range queries
* DP → storing past decisions

But they **always start** as array traversal.

If you are lost, go back to:

> “What happens if I just scan the array once?”

---

## 9. Common beginner mistakes with arrays

### Mistake 1: Overcomplicating traversal

Using nested loops when one loop is enough.

### Mistake 2: Ignoring edge cases

* empty array
* array of length 1

### Mistake 3: Updating answer at the wrong time

* too early
* too late

Always ask:

> “When is the answer valid?”

---

## 10. How arrays connect to other techniques

Arrays are the foundation for:

* Two pointers → two indices on the same array
* Sliding window → moving subarray
* Prefix sum → accumulated array
* Binary search → searching over indices
* DP → state indexed by position

If you master array thinking, everything else becomes easier.

---

## 11. Beginner practice mindset

When you see an array problem:

1. Ask if order matters
2. Try one-pass traversal first
3. Decide what information to maintain
4. Only then consider more advanced techniques

Most medium problems start with these steps.

---

## 12. Related problems in this repository

You can practice array basics with:

* `0001-two-sum`
* `0026-remove-duplicates-from-sorted-array`
* `0027-remove-element`
* `2110-number-of-smooth-descent-periods-of-a-stock`
* `1523-count-odd-numbers-in-an-interval-range`

---

## Final reminder

Arrays are not “easy problems”.

They are **fundamental problems**.

Strong fundamentals make advanced algorithms feel natural.
