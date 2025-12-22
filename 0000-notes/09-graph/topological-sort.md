# Topological Sort  

This note is written for beginners who feel:

- “I know topological sort is about prerequisites, but I don’t really get it”
- “Why does this problem suddenly become a graph problem?”
- “In-degree, queue, ordering… I get lost”

If this sounds familiar, this note is for you.

---

## 1. What problem does topological sort solve?

Topological sort solves problems where:

> **Some tasks must be done before others.**

Typical questions:
- Can I finish all tasks?
- In what order should I do them?
- Is there a valid ordering?

If the problem mentions:
- prerequisites
- dependencies
- before / after

→ suspect topological sort.

---

## 2. The key requirement (VERY IMPORTANT)

Topological sort only works on:

> **Directed Acyclic Graphs (DAG)**

Meaning:
- directed edges (A → B means A before B)
- no cycles

If there is a cycle:
- no valid ordering exists

---

## 3. Intuitive idea (no code)

Imagine courses at university:

- Course A must be taken before B
- Course B before C

You cannot take C first.

Topological sort finds:
> one valid order that respects all such rules

---

## 4. How to model the problem as a graph

Always do this first:

- **Node** → a task / course / job
- **Edge** A → B → A must come before B

Once you do this, the problem becomes concrete.

---

## 5. Two classic ways to do topological sort

There are **two standard approaches**:

1. **Kahn’s Algorithm (BFS-based)**
2. **DFS-based ordering**

For beginners, **Kahn’s Algorithm is clearer**.

---

## 6. Core idea of Kahn’s Algorithm

Key concept: **in-degree**

- in-degree = number of incoming edges
- meaning: how many prerequisites remain

Algorithm intuition:
1. Tasks with in-degree 0 can be done immediately
2. Remove them and update others
3. Repeat

---

## 7. Step-by-step Kahn’s Algorithm

### Step 1 — Build graph and in-degree

```python
graph = defaultdict(list)
indegree = [0] * n

for a, b in prerequisites:
    graph[a].append(b)
    indegree[b] += 1
````

---

### Step 2 — Initialize queue

```python
queue = deque()
for i in range(n):
    if indegree[i] == 0:
        queue.append(i)
```

These are tasks with no remaining prerequisites.

---

### Step 3 — Process queue

```python
order = []

while queue:
    node = queue.popleft()
    order.append(node)
    for nei in graph[node]:
        indegree[nei] -= 1
        if indegree[nei] == 0:
            queue.append(nei)
```

---

## 8. How to detect cycles

After the algorithm:

* if `len(order) == number of nodes`
  → valid topological order exists
* else
  → there is a cycle

This answers:

> “Can I finish all tasks?”

---

## 9. Why this works (intuition)

* Tasks with in-degree 0 are safe to do
* Removing them never breaks dependencies
* Repeating this mimics “finishing tasks”

This is a **greedy + BFS** process.

---

## 10. DFS-based topological sort (conceptual)

Another approach:

* use DFS
* push node to stack **after** exploring children

This works, but:

* harder to reason about
* cycle detection is trickier

For learning, BFS-based is recommended first.

---

## 11. Common beginner mistakes

### Mistake 1: Forgetting direction

Edges must point from prerequisite → dependent.

### Mistake 2: Not handling cycles

Always check final count.

### Mistake 3: Thinking there is only one order

There can be **many valid topological orders**.

---

## 12. When should you think of topological sort?

Use topological sort when:

* order matters
* dependencies exist
* graph is directed
* cycles invalidate solutions

This pattern appears very often.

---

## 13. Beginner checklist

Before using topological sort, ask:

* Are there dependencies?
* Can I model them as directed edges?
* Does a cycle mean “impossible”?

If yes → topological sort applies.

---

## 14. Related problems in this repository

Topological thinking applies to:

* course scheduling
* dependency resolution
* build systems
* ordering with constraints

---

## Final reminder

Topological sort is not about sorting.

It is about:

> **respecting dependencies**

Once you learn to see “before / after” as edges,
these problems become systematic.
