# BFS 广度优先搜索（中文版）

BFS 按“层”扩展，天然适合求无权图最短步数。

## 模板

```python
from collections import deque
q = deque([start])
vis = {start}
step = 0
while q:
    for _ in range(len(q)):
        u = q.popleft()
        if u == target: return step
        for v in neighbors(u):
            if v not in vis:
                vis.add(v)
                q.append(v)
    step += 1
```

## 例子：最短路径（网格）

- 每次从当前层扩展上下左右。
- 第一次到达终点时，步数最短。

## 易错点

- 入队时就标记 `visited`（避免重复入队）。
- 用层循环记录步数。
- 网格题注意边界和障碍。
