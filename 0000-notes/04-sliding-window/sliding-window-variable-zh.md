# 可变长度滑动窗口（中文版）

本笔记介绍可变窗口的典型题型。英文详版见：[sliding-window-variable.md](sliding-window-variable.md)。

---

## 适用条件

- 区间需满足某种**约束**（如和≤k）
- 寻找最长/最短满足条件的子数组

---

## 模板（双指针）

```python
left = 0
for right in range(n):
    # 扩展窗口
    while condition_not_met:
        # 收缩窗口
        left += 1
```

---

## 关键点

- 扩展时更新状态，收缩时恢复状态
- 维护“窗口内是否满足条件”的判断
