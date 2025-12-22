# Shortest Path — Dijkstra  

This note is written for beginners who feel:

- “I know BFS gives shortest path — until weights appear”
- “Priority queue logic feels magical”
- “I mix up BFS, Dijkstra, and DP”

If this sounds familiar, this note is for you.

---

## 1. What problem does Dijkstra solve?

Dijkstra solves this problem:

> **Find the shortest path in a graph with non-negative edge weights**

Typical questions:
- minimum distance
- minimum time / cost / price
- cheapest route

If edges have **different weights**, BFS is no longer correct.

---

## 2. Why BFS fails with weights (intuition)

BFS assumes:
- every edge costs the same

If edges have weights:
- reaching a node in fewer steps
- does NOT guarantee lower total cost

So “layer by layer” is no longer valid.

---

## 3. The core idea of Dijkstra

Dijkstra’s key idea:

> **Always expand the node with the smallest known distance so far**

Once you pick such a node:
- its shortest distance is finalized
- it will never be improved later

This is the crucial invariant.

---

## 4. The greedy invariant (VERY IMPORTANT)

During Dijkstra:

> **When a node is popped from the priority queue, its distance is final.**

This is true because:
- all weights are non-negative
- any alternative path would be longer

This is why Dijkstra is greedy.

---

## 5. Data structures you need

Dijkstra needs:
- a distance array / map
- a priority queue (min-heap)

Why heap?
- to always get the smallest distance node efficiently

---

## 6. Canonical Dijkstra template (Python)

```python
import heapq

def dijkstra(graph, start):
    dist = {node: float('inf') for node in graph}
    dist[start] = 0

    heap = [(0, start)]  # (distance, node)

    while heap:
        cur_dist, node = heapq.heappop(heap)

        if cur_dist > dist[node]:
            continue  # outdated entry

        for nei, weight in graph[node]:
            new_dist = cur_dist + weight
            if new_dist < dist[nei]:
                dist[nei] = new_dist
                heapq.heappush(heap, (new_dist, nei))

    return dist
````

This is the **standard, safe version**.

---

## 7. Why we need the “outdated entry” check

Priority queue can contain:

* multiple entries for the same node

This check:

```python
if cur_dist > dist[node]:
    continue
```

ensures:

* we only process the best one
* correctness and performance

---

## 8. When Dijkstra does NOT work

Dijkstra does NOT work when:

* there are **negative edge weights**

Why?

* the greedy invariant breaks

In that case, you need:

* Bellman-Ford
* or other algorithms

LeetCode almost always avoids negative weights.

---

## 9. Dijkstra vs BFS vs DP (quick comparison)

| BFS        | Dijkstra                | DP             |
| ---------- | ----------------------- | -------------- |
| Unweighted | Weighted (non-negative) | State-based    |
| Queue      | Priority Queue          | Table          |
| Min steps  | Min cost                | Optimal result |
| Local      | Greedy global           | Exhaustive     |

Choose based on **edge weights and problem structure**.

---

## 10. Dijkstra on grids (very common)

Grid interpretation:

* cell = node
* move = edge
* cost = cell value / movement cost

Use Dijkstra when:

* moving costs differ per cell

Same algorithm, different graph.

---

## 11. Common beginner mistakes

### Mistake 1: Using BFS when weights exist

This gives wrong answers.

### Mistake 2: Forgetting outdated-check

Leads to TLE or wrong logic.

### Mistake 3: Thinking Dijkstra finds all paths

It only finds **shortest distances**.

---

## 12. Beginner checklist

Before using Dijkstra, ask:

* Are edge weights non-negative?
* Do I need minimum cost?
* Can I model this as nodes + weighted edges?

If yes → Dijkstra applies.

---

## 13. Related problems in this repository

Shortest path thinking applies to:

* weighted grid problems
* minimum cost routes
* time / fuel / energy minimization problems

(Any “cheapest / fastest” wording is a hint.)

---

## Final reminder

Dijkstra is not complicated.

It is simply:

> **BFS upgraded to respect cost**

Once you see the priority queue as
“who should go next”,
Dijkstra becomes natural.
