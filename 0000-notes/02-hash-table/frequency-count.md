# Frequency Counting  

This note is written for beginners who feel:

- “I know how to use dict, but I don’t know when frequency matters”
- “I see counting everywhere, but I don’t recognize it”
- “I often miss problems that require frequency logic”

If this sounds familiar, this note is for you.

---

## 1. What is frequency counting?

Frequency counting means:

> **tracking how many times something appears**

Instead of storing each element separately,  
we store **its count**.

This simple idea appears in many problems.

---

## 2. When should you think about frequency?

Think about frequency when a problem mentions:

- how many times
- duplicates
- anagrams
- most / least frequent
- same elements with different order

If the exact order does not matter, frequency often does.

---

## 3. The core frequency question

Every frequency problem can be reduced to:

> “What does each unique element contribute?”

Once you answer this, the problem structure becomes clearer.

---

## 4. Canonical frequency counting template (dict)

```python
count = {}

for x in data:
    count[x] = count.get(x, 0) + 1
````

This is one of the most important templates in Python.

---

## 5. Using Counter (and when not to)

Python provides:

```python
from collections import Counter
freq = Counter(data)
```

### When Counter is good:

* simple counting
* clean code
* quick prototyping

### When Counter is NOT ideal:

* performance-critical loops
* frequent updates inside sliding window
* needing custom logic

Understanding both matters.

---

## 6. Frequency + one pass pattern

Many problems follow this structure:

1. Scan data once
2. Update frequency
3. Check or update answer

Example:

```python
for x in nums:
    freq[x] += 1
    if freq[x] > threshold:
        ...
```

This avoids nested loops.

---

## 7. Frequency inside sliding window

Very common combination.

Example logic:

* expand window → increment frequency
* shrink window → decrement frequency
* maintain validity based on frequency

If you understand this, many substring problems become easy.

---

## 8. Common beginner mistakes

### Mistake 1: Forgetting to remove zero-count keys

This can break validity checks.

### Mistake 2: Confusing frequency with index

Frequency counts appearances, not positions.

### Mistake 3: Using list instead of dict

Unless value range is small, dict is safer.

---

## 9. Frequency vs sorting

Two common approaches:

### Frequency-based

* O(n)
* extra space
* direct logic

### Sorting-based

* O(n log n)
* simpler comparisons
* order-based logic

Choose based on problem constraints.

---

## 10. Why frequency simplifies thinking

Frequency turns:

* complex structures
* repeated comparisons

into:

* simple numbers
* direct checks

This reduces cognitive load.

---

## 11. Beginner checklist

Before solving a problem, ask:

* Do I care about order?
* Do I care about duplicates?
* Do I need counts, not positions?

If yes → frequency counting is likely involved.

---

## 12. Related problems in this repository

Practice frequency counting with:

* `0001-two-sum`
* `0049-group-anagrams`
* `0242-valid-anagram`
* `0347-top-k-frequent-elements`
* `0451-sort-characters-by-frequency`
* `0692-top-k-frequent-words`
* `2273-find-resultant-array-after-removing-anagrams`

---

## Final reminder

Frequency counting is not advanced.

It is just:

> **turning repetition into numbers**

Once you see problems this way,
many patterns become obvious.
