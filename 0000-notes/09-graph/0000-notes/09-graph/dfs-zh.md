# DFS 深度优先搜索（中文版）

DFS 通过“先一路走到底，再回溯”来遍历图/树。

## 适用场景

- 连通分量计数
- 路径搜索
- 拓扑排序（后序）
- 回溯枚举

## 递归模板

```python
def dfs(u):
    vis.add(u)
    for v in g[u]:
        if v not in vis:
            dfs(v)
```

## 迭代模板

```python
stack = [start]
while stack:
    u = stack.pop()
    if u in vis:
        continue
    vis.add(u)
    for v in g[u]:
        if v not in vis:
            stack.append(v)
```

## 例子：岛屿数量

- 遍历网格，遇到陆地且未访问时启动 DFS。
- 一次 DFS 会“淹没”整个岛屿，计数加 1。

## 易错点

- 忘记 visited，导致无限递归。
- 递归深度过深（可改迭代）。
- 网格题方向数组写错。
