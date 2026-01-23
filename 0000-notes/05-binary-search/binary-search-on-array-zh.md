# 数组上的二分查找（中文版）

本笔记总结在有序数组上进行二分的要点。英文详版见：[binary-search-on-array.md](binary-search-on-array.md)。

---

## 核心要点

- 二分的前提：**有序**或**单调**。
- 明确目标：找等值、最左、最右、插入位置。

---

## 模板

```python
left, right = 0, n - 1
while left <= right:
    mid = (left + right) // 2
    if nums[mid] < target:
        left = mid + 1
    else:
        right = mid - 1
```

---

## 易错点

- 循环条件（<= vs <）
- mid 计算与边界更新
- 最终返回 left 还是 right
