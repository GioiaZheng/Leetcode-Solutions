# Hash Table Basics  

This note is written for beginners who feel:

- “Everyone keeps using hash tables, but I don’t fully get why”
- “I use dict because solutions do, not because I understand”
- “I don’t know when hashing is the right tool”

If this sounds familiar, this note is for you.

---

## 1. What problem does a hash table solve?

A hash table solves one core problem:

> **How can I quickly remember something I have seen before?**

Instead of scanning an array again and again,  
we store information so we can **look it up instantly**.

---

## 2. The key idea in plain words

A hash table is like a notebook:

- Key → question
- Value → answer

When you need information, you:
- open the notebook
- go directly to the page
- get the answer immediately

This is why hash table lookup is (on average) **O(1)**.

---

## 3. Python perspective: dict is your hash table

In Python:
- `dict` **is** a hash table
- `set` is a special case (only keys, no values)

Examples:

```python
seen = set()
count = {}
````

If you can use `dict` comfortably, you already know hashing.

---

## 4. When should you think of hashing?

You should consider a hash table when:

* You need to know if something exists
* You need to count occurrences
* You need to map one value to another
* You want to avoid nested loops

Typical questions:

* “Have I seen this before?”
* “How many times does this appear?”
* “Which index/value corresponds to this?”

---

## 5. Hashing vs brute force (why it matters)

### Brute force approach:

```python
for i in range(n):
    for j in range(n):
        ...
```

Time complexity: **O(n²)**

---

### Hashing approach:

```python
seen = set()
for x in nums:
    if x in seen:
        ...
    seen.add(x)
```

Time complexity: **O(n)**

Hashing trades **space** for **time**.

---

## 6. The three most common hashing patterns

### Pattern 1 — Existence checking

> “Does this element already exist?”

```python
seen = set()
for x in nums:
    if x in seen:
        return True
    seen.add(x)
```

---

### Pattern 2 — Key → value mapping

> “This thing corresponds to that thing”

```python
index_map = {}
for i, x in enumerate(nums):
    index_map[x] = i
```

---

### Pattern 3 — Counting frequency

> “How many times does this appear?”

```python
count = {}
for x in nums:
    count[x] = count.get(x, 0) + 1
```

This pattern is so common it deserves its own note.

---

## 7. Why hashing feels like “cheating” (but isn’t)

Hashing feels powerful because:

* it removes repeated work
* it turns searching into lookup

But it is not magic.

It works because:

* keys are hashed
* memory is used to store information

Understanding this trade-off is important.

---

## 8. Common beginner mistakes

### Mistake 1: Using hashing when order matters

Hash tables do not preserve order logic.

If order is important, arrays or two pointers may be better.

---

### Mistake 2: Forgetting about memory

Hashing uses extra space.

Sometimes sorting + two pointers is better.

---

### Mistake 3: Overcomplicating keys

Keys should be simple and hashable.

Avoid unnecessary complexity.

---

## 9. Hash table vs sorting (early intuition)

| Hash table       | Sorting        |
| ---------------- | -------------- |
| O(n) average     | O(n log n)     |
| Uses extra space | Often in-place |
| No order         | Order emerges  |

Neither is “better” universally.

Choosing correctly is a skill.

---

## 10. How hashing combines with other techniques

Hash tables often appear together with:

* sliding window (frequency inside window)
* prefix sum (map sum → count)
* greedy (tracking best choices)
* bucket techniques

Learning hashing unlocks many combinations.

---

## 11. Beginner checklist

Before using a hash table, ask:

* Do I need fast lookup?
* Am I checking existence or counting?
* Is order irrelevant?

If yes → hashing is likely correct.

---

## 12. Related problems in this repository

Practice hashing with:

* `0001-two-sum`
* `0049-group-anagrams`
* `0242-valid-anagram`
* `0220-contains-duplicate-iii`
* `2273-find-resultant-array-after-removing-anagrams`

---

## Final reminder

Hash tables are not advanced.

They are simply:

> **memory used intelligently**

Once you are comfortable with hashing,
many problems stop feeling impossible.
