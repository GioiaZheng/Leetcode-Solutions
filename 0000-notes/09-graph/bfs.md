# Breadth-First Search (BFS)  

This note is written for beginners who feel:

- “I know BFS uses a queue, but I don’t really get why”
- “When should I use BFS instead of DFS?”
- “Why BFS gives shortest path without weights?”

If this sounds familiar, this note is for you.

---

## 1. What problem does BFS solve?

BFS is used when you want to:

> **Explore a graph layer by layer**

Typical questions BFS answers:
- What is the minimum number of steps?
- What nodes are closest to the start?
- Can I reach the target in the fewest moves?

If the problem says **“minimum steps / moves / distance”**  
and edges are unweighted → BFS is your first choice.

---

## 2. Intuitive idea (no code)

Imagine ripples in water:

- You drop a stone (start node)
- Waves spread evenly in all directions
- Everything at distance 1 is reached before distance 2

BFS explores the graph **exactly like these ripples**.

---

## 3. Why BFS needs a queue (VERY IMPORTANT)

BFS relies on one rule:

> **Nodes discovered earlier must be processed earlier**

This is exactly what a **queue (FIFO)** does.

- push newly discovered nodes to the back
- process nodes from the front

Stack would break this order — queue preserves layers.

---

## 4. The BFS invariant

During BFS:

> **When a node is first visited, the shortest path to it is already known.**

This is why:
- BFS works for shortest path
- DFS does not guarantee shortest path

This invariant holds only when:
- all edges have equal weight

---

## 5. Canonical BFS template (Python)

```python
from collections import deque

queue = deque([start])
visited = set([start])

while queue:
    node = queue.popleft()
    for nei in graph[node]:
        if nei not in visited:
            visited.add(nei)
            queue.append(nei)
````

This is the **core BFS structure**.

---

## 6. Tracking distance / steps

Often you want distance.

Two common methods:

### Method 1 — Distance map

```python
dist = {start: 0}
```

When visiting neighbor:

```python
dist[nei] = dist[node] + 1
```

---

### Method 2 — Layer-by-layer BFS

```python
steps = 0
while queue:
    for _ in range(len(queue)):
        node = queue.popleft()
        ...
    steps += 1
```

Both are valid. Use what feels clearer.

---

## 7. When should you NOT use BFS?

Do NOT use BFS when:

* edges have different weights → use Dijkstra
* you need to explore all possibilities deeply → DFS
* recursion depth matters → DFS

BFS is about **distance**, not exhaustive search.

---

## 8. BFS vs DFS (practical comparison)

| BFS                        | DFS               |
| -------------------------- | ----------------- |
| Queue                      | Stack / recursion |
| Layer by layer             | Go deep           |
| Shortest path (unweighted) | Explore all       |
| More memory                | Less memory       |

Choose based on problem goal.

---

## 9. Common beginner mistakes

### Mistake 1: Marking visited too late

Always mark visited **when enqueuing**, not dequeuing.

### Mistake 2: Forgetting visited set

This causes infinite loops.

### Mistake 3: Using list instead of deque

`pop(0)` is O(n); deque is O(1).

---

## 10. BFS on grids (very common)

Grids are implicit graphs.

* each cell = node
* neighbors = up / down / left / right

Template idea:

```python
for dx, dy in directions:
    nx, ny = x + dx, y + dy
```

This is BFS in disguise.

---

## 11. Beginner checklist

Before using BFS, ask:

* Is the graph unweighted?
* Do I need minimum steps?
* Can I model this as nodes + edges?

If yes → BFS is likely correct.

---

## 12. Related problems in this repository

BFS thinking applies to:

* shortest path in unweighted graphs
* grid traversal problems
* level-order exploration problems
* reachability with minimum steps

(DFS will contrast with this next.)

---

## Final reminder

BFS is not about queues.

It is about:

> **respecting distance order**

Once you see BFS as “distance first”,
you’ll recognize it immediately in problems.
