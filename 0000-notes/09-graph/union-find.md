# Union-Find (Disjoint Set Union)  

This note is written for beginners who feel:

- “I don’t understand why Union-Find exists”
- “DFS/BFS can find components, so why do we need this?”
- “Parent arrays and path compression confuse me”

If this sounds familiar, this note is for you.

---

## 1. What problem does Union-Find solve?

Union-Find solves problems where you need to:

> **Dynamically track whether two elements are connected**

Key word: **dynamically**

That means:
- connections are added over time
- you need to answer many connectivity queries

---

## 2. When DFS / BFS is NOT ideal

DFS / BFS works well when:
- the graph is fixed
- you traverse once

But they are inefficient when:
- edges are added one by one
- you repeatedly ask “are A and B connected?”

Union-Find is designed exactly for this case.

---

## 3. Core idea (no code yet)

Union-Find maintains:
- several disjoint groups (sets)
- each element belongs to exactly one group

Two basic operations:
1. **Find** → which group am I in?
2. **Union** → merge two groups

That’s it.

---

## 4. Real-world intuition

Think of friend groups:

- initially, everyone is alone
- when two people become friends → groups merge
- later, you ask: “are these two in the same group?”

You don’t care *how* they are connected,
only *whether* they are connected.

---

## 5. Data structure intuition

Each group is represented as a **tree**:

- each node points to a parent
- the root represents the group

If two nodes have the same root → same group.

---

## 6. Canonical Union-Find structure (Python)

```python
class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        px = self.find(x)
        py = self.find(y)
        if px != py:
            self.parent[px] = py
````

This is the **minimum usable version**.

---

## 7. Path compression (VERY IMPORTANT)

This line is the magic:

```python
self.parent[x] = self.find(self.parent[x])
```

What it does:

* flattens the tree
* makes future finds faster

Result:

> **Almost O(1) time per operation**

This is why Union-Find is so powerful.

---

## 8. Union by rank / size (optional but useful)

Optimization idea:

* always attach smaller tree to bigger tree

Why:

* keeps trees shallow
* improves performance

This is an optimization, not a requirement for correctness.

---

## 9. When should you think of Union-Find?

Think of Union-Find when the problem asks:

* are these two connected?
* how many connected components?
* connections are added gradually
* no need to enumerate paths

If the problem is about **connectivity**, not **paths** → Union-Find.

---

## 10. Union-Find vs DFS / BFS

| Union-Find        | DFS / BFS               |
| ----------------- | ----------------------- |
| Dynamic           | Static                  |
| Connectivity only | Full traversal          |
| Very fast queries | Slower repeated queries |
| No path info      | Path info available     |

They solve **different needs**.

---

## 11. Common beginner mistakes

### Mistake 1: Forgetting to call find in union

Always union roots, not raw nodes.

### Mistake 2: Thinking Union-Find gives paths

It does NOT store path information.

### Mistake 3: Overusing Union-Find

If you need shortest path → use BFS/Dijkstra instead.

---

## 12. Typical Union-Find problem patterns

Union-Find is often used in:

* number of connected components
* dynamic graph connectivity
* cycle detection (undirected graph)
* Kruskal’s algorithm (MST)

---

## 13. Beginner checklist

Before using Union-Find, ask:

* Do I only care about connectivity?
* Are edges added dynamically?
* Do I need fast repeated queries?

If yes → Union-Find is ideal.

---

## 14. Related problems in this repository

Union-Find thinking applies to:

* connectivity problems
* grouping problems
* component counting
* merging sets dynamically

(You’ll recognize these patterns more and more.)

---

## Final reminder

Union-Find is not complicated.

It is simply:

> **remembering who belongs together**

Once you see that,
it becomes one of the easiest and fastest tools you have.
