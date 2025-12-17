# Sliding Window — Fixed Size  

This note is written for beginners who feel:

- “I hear ‘sliding window’ everywhere, but it feels confusing”
- “I don’t know when sliding window is necessary”
- “I mix up fixed window and variable window all the time”

This note focuses on the **simplest form**: fixed-size sliding window.

---

## 1. What is a sliding window (intuitively)?

A sliding window is:
> a **contiguous subarray** that moves across the array.

Imagine a window of fixed length `k` moving from left to right.

```text
[ x x x ] _ _ _
_ [ x x x ] _ _
_ _ [ x x x ] _
````

The window content changes, but its **size stays the same**.

---

## 2. When should you think of a fixed-size window?

Think of a fixed-size window when:

* The problem asks about **subarrays or substrings**
* The size of the subarray is **given and fixed**
* You are evaluating each window independently

Typical examples:

* maximum sum of length k
* average of length k
* checking every substring of length k

---

## 3. Why sliding window is better than brute force

Brute force approach:

* For each window, recompute everything
* Time complexity: O(n * k)

Sliding window approach:

* Reuse information from the previous window
* Add one element, remove one element
* Time complexity: O(n)

The idea is **avoid repeated work**.

---

## 4. The core idea in one sentence

> When the window moves,
> **only two elements change**:
> one leaves, one enters.

This is the heart of sliding window.

---

## 5. Step-by-step thinking process

Suppose we want the sum of each window of size `k`.

1. Compute the sum of the first window
2. Move the window one step to the right
3. Subtract the leftmost element
4. Add the new rightmost element

Repeat until the end.

---

## 6. Canonical Python template

```python
window_sum = sum(nums[:k])
best = window_sum

for i in range(k, len(nums)):
    window_sum += nums[i]        # add new element
    window_sum -= nums[i - k]    # remove old element
    best = max(best, window_sum)
```

Key points:

* `i` is the right end of the window
* `i - k` is the element leaving the window

---

## 7. Common beginner mistakes

### Mistake 1: Recomputing the window each time

This defeats the purpose of sliding window.

### Mistake 2: Off-by-one errors

Confusing indices `i`, `i - k`, and window boundaries.

### Mistake 3: Forgetting to initialize the first window

Always handle the first window explicitly.

---

## 8. Fixed window vs variable window

| Fixed window    | Variable window            |
| --------------- | -------------------------- |
| Size is known   | Size changes               |
| Simple logic    | More complex logic         |
| No `while` loop | Requires `while` to shrink |
| Easier to debug | Easier to break            |

Always learn fixed window first.

---

## 9. How fixed window connects to prefix sum

Prefix sum can also compute window sums:

* Precompute prefix array
* Query each range in O(1)

Sliding window:

* O(1) space
* One pass

Both are valid — sliding window is more memory efficient.

---

## 10. Beginner practice checklist

Before coding, confirm:

* Window size is fixed
* Data is contiguous
* Only window content matters

If all three are true, sliding window is likely correct.

---

## 11. Related problems in this repository

Practice fixed-size sliding window with:

* `2110-number-of-smooth-descent-periods-of-a-stock`
* `3381-maximum-subarray-sum-with-length-divisible-by-k`
* (many array average / sum problems)

---

## Final reminder

Sliding window is not a trick.

It is just:

> **remembering what changes when the window moves**.

Once this feels natural, variable window becomes much easier.
