# 回溯模板（中文版）

本笔记提供回溯的基本模板与思路。英文详版见：[backtracking-template.md](backtracking-template.md)。

---

## 典型问题

- 组合/排列/子集
- 约束满足（数独/分割）

---

## 模板

```python
path = []

def backtrack(start):
    if 满足结束条件:
        记录答案
        return
    for i in range(start, n):
        选择
        backtrack(i + 1)
        撤销选择
```

---

## 注意点

- 选择与撤销必须成对
- 剪枝条件越早越好
