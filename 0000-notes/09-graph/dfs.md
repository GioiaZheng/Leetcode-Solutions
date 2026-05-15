# Depth-First Search (DFS)  

This note is written for beginners who feel:

- “I don’t know when to use DFS instead of BFS”
- “Recursion in DFS scares me”
- “DFS sometimes works, sometimes gives wrong answers”

If this sounds familiar, this note is for you.

---

## 1. What problem does DFS solve?

DFS is used when you want to:

> **Explore all possibilities deeply before backtracking**

Typical questions DFS answers:
- Can I reach all nodes?
- How many connected components are there?
- Is there a cycle?
- Enumerate all paths / regions

If the problem is about **exploration**, not distance → DFS.

---

## 2. Intuitive idea (no code)

Imagine exploring a maze:

- You choose a path
- Keep walking until you hit a wall
- Go back to the last fork
- Try another path

This is exactly DFS.

---

## 3. DFS core behavior

DFS always follows this rule:

> **Go as deep as possible before switching direction**

This depth-first behavior is what distinguishes it from BFS.

---

## 4. DFS via recursion (most common)

Recursive DFS mirrors the thinking process naturally.

Canonical template:

```python
visited = set()

def dfs(node):
    visited.add(node)
    for nei in graph[node]:
        if nei not in visited:
            dfs(nei)

dfs(start)
````

Each recursive call explores **one branch** fully.

---

## 5. DFS via stack (iterative)

DFS can also be written iteratively:

```python
stack = [start]
visited = set([start])

while stack:
    node = stack.pop()
    for nei in graph[node]:
        if nei not in visited:
            visited.add(nei)
            stack.append(nei)
```

This avoids recursion depth limits.

---

## 6. Why recursion fits DFS so well

Recursion naturally handles:

* “go deeper”
* “come back”

Each function call:

* represents one position in the graph
* automatically remembers where you came from

This is why DFS + recursion feels intuitive.

---

## 7. When DFS is better than BFS

Use DFS when:

* you need to explore entire components
* you need to detect cycles
* you need to enumerate all paths
* distance / steps do NOT matter

DFS is about **coverage**, not closeness.

---

## 8. DFS on grids (very common)

Grid DFS pattern:

```python
def dfs(x, y):
    if out_of_bounds or visited[x][y]:
        return
    visited[x][y] = True
    for dx, dy in directions:
        dfs(x + dx, y + dy)
```

This pattern appears in:

* islands
* regions
* flood fill
* area counting

---

## 9. Connected components intuition

DFS is perfect for this question:

> “How many disconnected groups exist?”

Algorithm:

* loop through all nodes
* if a node is unvisited → start DFS
* each DFS marks one component

---

## 10. DFS and cycles

DFS can detect cycles by:

* tracking visited nodes
* sometimes tracking recursion stack (directed graphs)

Cycle detection is a classic DFS use case.

---

## 11. Common beginner mistakes

### Mistake 1: Forgetting visited

Leads to infinite recursion.

### Mistake 2: Using DFS for shortest path

DFS does NOT guarantee shortest path.

### Mistake 3: Stack overflow on deep graphs

Use iterative DFS or increase recursion limit.

---

## 12. DFS vs BFS (final contrast)

| DFS                | BFS                   |
| ------------------ | --------------------- |
| Go deep            | Go wide               |
| Explore all        | Find closest          |
| Recursion friendly | Queue based           |
| Not shortest       | Shortest (unweighted) |

Choose based on **problem goal**, not habit.

---

## 13. Beginner checklist

Before using DFS, ask:

* Do I need to explore everything?
* Is distance irrelevant?
* Is recursion depth manageable?

If yes → DFS is a good fit.

---

## 14. Related problems in this repository

DFS thinking applies to:

* connected components problems
* grid region problems
* reachability checks
* cycle detection

---

## Final reminder

DFS is not about recursion.

It is about:

> **commit to a path, explore fully, then backtrack**

Once you see that pattern,
DFS becomes a very natural tool.

---

## Interview quick reference

### Pattern description
DFS explores one branch fully before backtracking. It can be recursive or stack-based and is ideal for reachability and component exploration.

### When to use it
- Connected components.
- Tree/subtree recursion.
- Exhaustive path search.
- Cycle detection or topological reasoning.
- Grid flood fill / island-style problems.

### Template code

```python
def dfs(node):
    visited.add(node)
    for nei in graph[node]:
        if nei not in visited:
            dfs(nei)

visited = set()
dfs(start)
```

Iterative version:

```python
stack = [start]
visited = {start}
while stack:
    node = stack.pop()
    for nei in graph[node]:
        if nei not in visited:
            visited.add(nei)
            stack.append(nei)
```

### Common pitfalls
- Forgetting `visited` in cyclic graphs.
- Using DFS for shortest path in unweighted graphs when BFS is required.
- Hitting recursion depth on long chains.
- Mutating shared path state without backtracking.

### Linked solved problems
- [`0756-pyramid-transition-matrix`](../../0756-pyramid-transition-matrix/)
- [`2872-maximum-number-of-k-divisible-components`](../../2872-maximum-number-of-k-divisible-components/)
- [`0865-smallest-subtree-with-all-the-deepest-nodes`](../../0865-smallest-subtree-with-all-the-deepest-nodes/)
- [`1339-maximum-product-of-splitted-binary-tree`](../../1339-maximum-product-of-splitted-binary-tree/)
