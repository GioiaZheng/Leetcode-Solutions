# Graph Summary

Use this page as a quick decision guide before choosing a graph technique.

## Core Idea

A problem is graph-shaped when it is about relationships and reachability:

- who connects to whom
- what can reach what
- how many steps separate two states
- how information, flow, or constraints propagate

The first modeling step is always:

1. Define the nodes.
2. Define the edges.
3. Decide whether the graph is directed or undirected.
4. Decide whether the graph is weighted or unweighted.

## Technique Guide

| Goal | Usually Use |
|---|---|
| Visit all reachable nodes | BFS or DFS |
| Count connected components | DFS, BFS, or Union-Find |
| Shortest path in an unweighted graph | BFS |
| Shortest path with non-negative weights | Dijkstra |
| Maintain dynamic connectivity | Union-Find |
| Resolve dependency order | Topological sort |
| Explore all paths / choices | DFS or backtracking |

## BFS vs DFS

Use BFS when:

- the problem asks for minimum steps, moves, distance, or earliest time
- all edges have equal weight
- level order matters

Use DFS when:

- the problem asks for full exploration
- you need connected components, cycle checks, subtree logic, or backtracking
- distance is not the primary objective

## Common Mistakes

- Using DFS for shortest path in an unweighted graph when BFS is required.
- Forgetting `visited` in cyclic graphs.
- Treating a directed graph as undirected.
- Building the graph before confirming what the nodes and edges actually are.
- Missing that a grid can be modeled as a graph of cells.

## Repository Examples

- [`2092-find-all-people-with-secret`](../../problems/2092-find-all-people-with-secret/) - time-bucketed graph traversal.
- [`1970-last-day-where-you-can-still-cross`](../../problems/1970-last-day-where-you-can-still-cross/) - grid reachability with binary search.
- [`2872-maximum-number-of-k-divisible-components`](../../problems/2872-maximum-number-of-k-divisible-components/) - tree DFS.
- [`1161-maximum-level-of-a-binary-tree`](../../problems/1161-maximum-level-of-a-binary-tree/) - BFS by tree level.

## Next Notes

- [BFS](bfs.md)
- [DFS](dfs.md)
- [Union-Find](union-find.md)
- [Topological Sort](topological-sort.md)
- [Dijkstra](shortest-path-dijkstra.md)
