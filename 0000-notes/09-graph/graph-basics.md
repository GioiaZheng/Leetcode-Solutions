# Graph Basics  

This note is written for beginners who feel:

- “Graph problems look abstract and scary”
- “I don’t know when something is a graph problem”
- “Nodes, edges, adjacency lists confuse me”

If this sounds familiar, this note is for you.

---

## 1. What problem does a graph solve?

A graph models **relationships**.

Instead of thinking about numbers or indices,
think about:
> **things and how they are connected**

Examples:
- cities connected by roads
- people connected by friendships
- courses connected by prerequisites
- webpages connected by links

If a problem is about **connections**, it is probably a graph.

---

## 2. The simplest definition of a graph

A graph has only two components:

- **Nodes (vertices)** — the things
- **Edges** — the connections between things

That’s it.

Everything else is detail.

---

## 3. Directed vs undirected graphs

### Undirected graph
- connection goes both ways
- example: friendship

```

A — B

```

### Directed graph
- connection has a direction
- example: prerequisites

```

A → B

````

Always ask:
> “Is the relationship one-way or two-way?”

---

## 4. Weighted vs unweighted graphs

### Unweighted
- all edges are equal
- example: can I reach?

### Weighted
- edges have costs
- example: shortest distance, time, price

This affects which algorithms apply.

---

## 5. How graphs appear in coding problems

Many problems don’t say “graph”.

They say:
- “can you reach…”
- “minimum number of steps…”
- “connected components…”
- “path exists…”

These are **graph questions in disguise**.

---

## 6. Graph representations (important)

Graphs are usually represented as:

### Adjacency list (most common)

```python
graph = {
    0: [1, 2],
    1: [2],
    2: [0, 3],
    3: []
}
````

Meaning:

* node 0 connects to 1 and 2

---

### Adjacency matrix (less common)

```text
0 1 2 3
0 0 1 1 0
1 0 0 1 0
2 1 0 0 1
3 0 0 0 0
```

Use matrix only when graph is very small or dense.

---

## 7. Why adjacency list is preferred

Adjacency list:

* memory efficient
* easy to traverse
* natural for DFS / BFS

Most LeetCode graph problems use this form implicitly.

---

## 8. The two fundamental graph actions

All graph algorithms do one of these:

1. **Traverse** the graph
2. **Search** for paths / components

Traversal answers:

* “what can I reach?”

Search answers:

* “how do I reach optimally?”

---

## 9. BFS vs DFS (high-level intuition)

### DFS (Depth-First Search)

* go as deep as possible
* backtrack

Good for:

* exploring all possibilities
* connected components
* cycles

---

### BFS (Breadth-First Search)

* explore level by level

Good for:

* shortest path in unweighted graphs
* minimum steps
* nearest target

We will cover both in detail next.

---

## 10. Visited set: the most important rule

When traversing a graph:

> **Always remember what you have visited.**

Without this:

* infinite loops
* repeated work

Visited = memory of exploration.

---

## 11. Common beginner mistakes

### Mistake 1: Forgetting graph direction

This changes reachability.

### Mistake 2: Using wrong representation

Matrix when list is needed.

### Mistake 3: Not marking visited early

Leads to cycles.

---

## 12. Beginner checklist

When you see a problem, ask:

* What are the nodes?
* What are the edges?
* Is the graph directed?
* Is it weighted?
* Do I need traversal or shortest path?

If you can answer these, the problem is already half solved.

---

## 13. Related problems in this repository

Graph thinking applies to:

* path existence problems
* connectivity problems
* prerequisite problems
* traversal-based simulations

(BFS / DFS will make these concrete.)

---

## Final reminder

Graph is not a special topic.

It is:

> **a way to think about relationships**

Once you learn to identify nodes and edges,
graph problems stop looking mysterious.
