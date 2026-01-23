# 最短路径（Dijkstra）（中文版）

本笔记介绍 Dijkstra 算法的核心思路。英文详版见：[shortest-path-dijkstra.md](shortest-path-dijkstra.md)。

---

## 适用场景

- **非负权重**图的最短路径

---

## 核心思路

- 使用优先队列每次取当前最短节点
- 松弛邻边并更新距离

---

## 注意点

- 图中不能有负权边
- 可能需要处理重复入堆
