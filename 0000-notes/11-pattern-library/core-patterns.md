# Core Algorithm Patterns  

This note is written for learners who feel:

- “I understand the idea, but I blank when coding”
- “Every solution looks different, I don’t see patterns”
- “I want reusable templates, not random tricks”

If this sounds familiar, this note is for you.

---

## 1. Why patterns matter more than solutions

A solution solves **one problem**.

A pattern solves:
> **a whole family of problems**

Strong problem solvers don’t memorize answers.
They recognize patterns.

---

## 2. Pattern 1 — Two Pointers (Linear Scan)

### When to use
- sorted array
- pairs / ranges
- shrinking from both sides

### Core idea
Move pointers based on comparison.

### Template
```python
l, r = 0, n - 1
while l < r:
    if condition:
        l += 1
    else:
        r -= 1
````

---

## 3. Pattern 2 — Sliding Window (Dynamic Range)

### When to use

* contiguous subarray / substring
* condition maintained dynamically
* max / min length

### Core idea

Expand right, shrink left.

### Template

```python
l = 0
for r in range(n):
    add(nums[r])
    while not valid():
        remove(nums[l])
        l += 1
    update_answer()
```

---

## 4. Pattern 3 — Hash Table (Existence / Frequency)

### When to use

* seen before?
* counting
* mapping

### Core idea

Trade space for time.

### Template

```python
seen = set()
for x in data:
    if x in seen:
        ...
    seen.add(x)
```

Frequency:

```python
count[x] = count.get(x, 0) + 1
```

---

## 5. Pattern 4 — Prefix Sum

### When to use

* range queries
* cumulative properties
* subarray counting

### Core idea

Precompute once, reuse.

### Template

```python
prefix = [0] * (n + 1)
for i in range(n):
    prefix[i+1] = prefix[i] + nums[i]
```

---

## 6. Pattern 5 — Binary Search on Array

### When to use

* sorted data
* boundary finding

### Core idea

Shrink interval, keep invariant.

### Template

```python
l, r = 0, n
while l < r:
    mid = (l + r) // 2
    if nums[mid] < target:
        l = mid + 1
    else:
        r = mid
```

---

## 7. Pattern 6 — Binary Search on Answer

### When to use

* maximize / minimize feasible value
* monotonic feasibility

### Core idea

Search values, not indices.

### Template

```python
while l < r:
    mid = (l + r + 1) // 2
    if can(mid):
        l = mid
    else:
        r = mid - 1
```

---

## 8. Pattern 7 — Greedy (Safe Choice)

### When to use

* local choice provably safe
* scheduling / intervals

### Core idea

Pick the least harmful option.

### Template (interval greedy)

```python
intervals.sort(key=lambda x: x[1])
end = -inf
for s, e in intervals:
    if s >= end:
        end = e
```

---

## 9. Pattern 8 — DP on Array

### When to use

* max / min ending at position
* overlapping subproblems

### Core idea

Remember best so far.

### Template

```python
dp[0] = base
for i in range(1, n):
    dp[i] = transition(dp[i-1], ...)
```

---

## 10. Pattern 9 — DP on Strings (2D)

### When to use

* subsequence / edit distance
* compare two strings

### Core idea

Prefix vs prefix.

### Template

```python
dp = [[0]*(m+1) for _ in range(n+1)]
for i in range(1, n+1):
    for j in range(1, m+1):
        dp[i][j] = transition(...)
```

---

## 11. Pattern 10 — BFS (Shortest Path, Unweighted)

### When to use

* minimum steps
* grid / graph

### Core idea

Layer by layer.

### Template

```python
queue = deque([start])
visited = {start}
while queue:
    node = queue.popleft()
    for nei in graph[node]:
        if nei not in visited:
            visited.add(nei)
            queue.append(nei)
```

---

## 12. Pattern 11 — DFS (Full Exploration)

### When to use

* connected components
* regions
* cycles

### Core idea

Go deep, then backtrack.

### Template

```python
def dfs(node):
    for nei in graph[node]:
        if nei not in visited:
            dfs(nei)
```

---

## 13. Pattern 12 — Union-Find

### When to use

* dynamic connectivity
* grouping

### Core idea

Track components, not paths.

### Template

```python
def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]
```

---

## 14. How to actually use this page

When stuck:

1. Identify goal (distance? count? optimize?)
2. Match with a pattern
3. Adapt template to problem details

Never start from a blank file.

---

## Final reminder

Patterns are not shortcuts.

They are:

> **compressed experience**

The more problems you solve,
the faster you’ll recognize which pattern applies.
