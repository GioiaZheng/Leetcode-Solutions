# 固定长度滑动窗口（中文版）

本笔记介绍固定窗口的典型结构。英文详版见：[sliding-window-fixed.md](sliding-window-fixed.md)。

---

## 核心场景

- 子数组长度固定
- 连续区间内求和/最值/计数

---

## 模板

```python
window_sum = sum(nums[:k])
ans = window_sum

for i in range(k, n):
    window_sum += nums[i] - nums[i - k]
    ans = max(ans, window_sum)
```

---

## 注意点

- 初始化第一段窗口
- 更新顺序别写反
- k 可能等于 n
