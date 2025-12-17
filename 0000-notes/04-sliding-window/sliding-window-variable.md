# Sliding Window — Variable Size  

This note is written for beginners who feel:

- “Fixed window is fine, but variable window confuses me”
- “I don’t know when to use `while` instead of `if`”
- “I get lost when the window needs to shrink”

If this sounds familiar, this note is for you.

---

## 1. What is a variable-size sliding window?

A variable-size sliding window is still:
> a **contiguous subarray / substring**

But unlike fixed window:
- the window **does not have a fixed length**
- the window **must satisfy a condition**

The window **expands and shrinks dynamically**.

---

## 2. The key difference from fixed window

### Fixed window
- size is known
- no need to shrink
- simple for-loop

### Variable window
- size is unknown
- condition may break
- must shrink until valid

This is why `while` appears.

---

## 3. When should you think of variable sliding window?

You should consider variable window when:

- The problem involves **subarrays / substrings**
- There is a constraint like:
  - at most K
  - no more than
  - fewer than
  - without repeating
- You are asked for:
  - longest
  - shortest
  - number of valid windows

If the constraint depends on window content → variable window.

---

## 4. The core invariant (MOST IMPORTANT)

> **After adjustment, the window must always be valid.**

This is the rule everything follows.

Process:
1. Expand the window (move right)
2. If invalid → shrink from left
3. Shrink until valid again
4. Only then update the answer

If you violate this invariant, bugs appear.

---

## 5. Human thinking before code

Imagine reading the array from left to right.

- “Let me include this new element”
- “Oops, now the window is invalid”
- “I must remove elements from the left”
- “Okay, it’s valid again”

This is exactly what the code does.

---

## 6. Canonical Python template

```python
left = 0
window = {}
ans = 0

for right in range(n):
    # include new element
    add(nums[right], window)

    # shrink until window is valid
    while not is_valid(window):
        remove(nums[left], window)
        left += 1

    # update answer when window is valid
    ans = max(ans, right - left + 1)
````

Key points:

* `right` always moves forward
* `left` only moves forward
* total time complexity: **O(n)**

---

## 7. Why `while`, not `if`?

This is a very common beginner mistake.

### Wrong:

```python
if not valid:
    left += 1
```

### Correct:

```python
while not valid:
    left += 1
```

Why?

Because:

* removing one element may **not be enough**
* the window may still be invalid
* you must shrink until the invariant is restored

---

## 8. Three common problem types

### Type 1 — Longest valid window

Example:

* Longest substring without repeating characters

Update answer **after shrinking**.

---

### Type 2 — Shortest valid window

Example:

* Minimum window substring

Update answer **before shrinking further**.

---

### Type 3 — Count valid windows

Key trick:

> If a window is valid,
> **all subwindows inside it are also valid**

This often leads to:

```python
ans += right - left + 1
```

---

## 9. “At most K” vs “Exactly K”

Very important transformation:

> **Exactly K = At most K − At most (K − 1)**

Why this works:

* sliding window handles “at most” naturally
* “exactly” is hard directly

This trick appears often in Medium problems.

---

## 10. Common beginner mistakes

### Mistake 1: Updating answer too early

Only update when window is valid.

### Mistake 2: Shrinking too late

Always fix validity immediately.

### Mistake 3: Forgetting window state cleanup

E.g. not removing keys when count becomes zero.

---

## 11. Debugging checklist

If your variable window solution is wrong, check:

* Does `left` ever move backward? (It should not)
* Do you always restore validity?
* Are you updating the answer at the right moment?
* Is your `is_valid` condition correct?

---

## 12. Related problems in this repository

Practice variable sliding window with:

* `0003-longest-substring-without-repeating-characters`
* `2147-number-of-ways-to-divide-a-long-corridor`
* `0220-contains-duplicate-iii`
* `3578-count-partitions-with-max-min-difference-at-most-k`

---

## Final reminder

Variable sliding window is not hard.

It is just:

> **expand → break → shrink → restore**

Once this loop is clear, many Medium problems become manageable.
