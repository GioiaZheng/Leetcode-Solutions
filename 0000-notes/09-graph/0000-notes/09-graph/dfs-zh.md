# 深度优先搜索 DFS（中文版）

本笔记帮助你理解 DFS 的适用场景与写法。英文详版见：[dfs.md](dfs.md)。

---

## DFS 解决什么问题

- **深度探索**所有可能路径
- 关注“能否到达”“覆盖范围”“是否有环”

典型问题：
- 连通分量
- 是否存在路径
- 枚举所有路径/区域

---

## 直观理解

像走迷宫：
- 先一直往里走
- 走不通就回退再换路

---

## 递归模板

```python
visited = set()

def dfs(node):
    visited.add(node)
    for nei in graph[node]:
        if nei not in visited:
            dfs(nei)
```

---

## 迭代模板

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

---

## 适用判断

- 需要**全面探索**或**检测环** → DFS
- 不关心最短距离 → DFS
