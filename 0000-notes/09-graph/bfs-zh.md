# BFS 广度优先搜索（中文版）

本笔记介绍 BFS 的使用场景与模板。英文详版见：[bfs.md](bfs.md)。

---

## 适用场景

- 无权图最短路径
- 分层遍历
- 多源扩散

---

## 模板

```python
from collections import deque
queue = deque([start])
visited = {start}

while queue:
    node = queue.popleft()
    for nxt in graph[node]:
        if nxt not in visited:
            visited.add(nxt)
            queue.append(nxt)
```

---

## 注意点

- 先入队再标记，避免重复
- 多源 BFS 可先把所有源入队
