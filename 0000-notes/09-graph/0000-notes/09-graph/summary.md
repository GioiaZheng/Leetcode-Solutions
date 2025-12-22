# Graph — Summary  

This summary is written for learners who want:

- a quick decision guide
- a way to avoid misclassifying problems
- a mental map of graph-related techniques

Use this page before jumping into code.

---

## 1. What a graph problem really is (core idea)

A problem is a graph problem if it is about:

> **relationships and reachability**

Not about:
- array indices
- numeric order
- continuous ranges

But about:
- who connects to whom
- what can reach what
- how many steps between two things

---

## 2. How graph problems usually appear (disguises)

Most problems do NOT say “graph”.

They say:
- “can you reach…”
- “minimum number of steps…”
- “connected components…”
- “paths exist…”
- “spread / propagate / flow…”

If you see these words, suspect a graph.

---

## 3. First step: identify nodes and edges

Always ask:

- What are the **nodes**?
- What are the **edges**?
- Is the graph **directed or undirected**?
- Is it **weighted or unweighted**?

If you can answer these, the problem becomes concrete.

---

## 4. BFS vs DFS — the decision table

### Use BFS when:
- you want **minimum steps / distance**
- the graph is **unweighted**
- you care about **closest / earliest**

Typical phrases:
- “minimum moves”
- “shortest path”
- “fewest operations”

---

### Use DFS when:
- you want to **explore everything**
- you want to count **components / regions**
- you want to detect **cycles**
- distance does NOT matter

Typical phrases:
- “how many groups”
- “is it connected”
- “explore all possibilities”

---

## 5. BFS vs DFS (side-by-side intuition)

| BFS | DFS |
|---|---|
| Layer by layer | Go deep |
| Queue | Recursion / Stack |
| Shortest path (unweighted) | Full exploration |
| Distance-focused | Coverage-focused |

Choose based on **goal**, not preference.

---

## 6. Graphs on grids (very common)

Many “matrix” problems are actually graphs.

Mapping:
- cell → node
- adjacency → edges (up, down, left, right)

If you can move between cells → graph traversal.

---

## 7. Visited set is mandatory

In graph traversal:

> **Always mark visited nodes**

Why:
- avoid infinite loops
- avoid repeated work
- ensure correctness

Rule of thumb:
- mark visited when you **enqueue / recurse**
- not when you finish processing

---

## 8. Common beginner misclassifications

### Mistake 1: Using DP when traversal is enough
If no optimization or counting is needed → graph traversal.

### Mistake 2: Using DFS for shortest path
DFS does NOT guarantee shortest distance.

### Mistake 3: Forgetting direction
Directed vs undirected changes everything.

---

## 9. Graph vs DP vs Greedy (quick guide)

### Use Graph when:
- relationships are explicit
- reachability matters

### Use DP when:
- decisions affect future choices
- optimal / number of ways is asked

### Use Greedy when:
- a local choice is provably safe

Choosing the right model is half the solution.

---

## 10. Typical graph problem families

Graph traversal solves:
- reachability
- connected components
- shortest path (unweighted)
- flood fill / region counting
- cycle detection

Advanced graph topics build on this.

---

## 11. What comes AFTER basic BFS / DFS

Once BFS / DFS are solid, the next tools are:

- Union-Find (disjoint sets)
- Topological Sort
- Shortest Path (Dijkstra)
- Minimum Spanning Tree

All of them rely on **graph fundamentals**.

---

## 12. Problems in this repository using graph thinking

Graph ideas apply to:
- grid traversal problems
- reachability checks
- simulation with spreading
- prerequisite / dependency problems

Revisit them with this summary in mind.

---

## Final reminder

Graph problems are not special.

They are simply:
> **questions about connections**

Once you train yourself to see nodes and edges,
graph problems become structured and predictable.
