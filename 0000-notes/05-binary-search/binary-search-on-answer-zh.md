# 二分答案（中文版）

核心思想：不直接找答案值，而是二分“可行性阈值”。

## 适用条件

- 答案范围可枚举（整数区间）。
- 存在单调性：
  - 若 `x` 可行，则更大（或更小）也可行。

## 模板

```python
def check(mid):
    # mid 是否可行
    ...

l, r = low, high
while l < r:
    mid = (l + r) // 2
    if check(mid):
        r = mid
    else:
        l = mid + 1
return l
```

## 例子：最小化最大工作量

- `mid` 表示允许的最大工作量。
- `check(mid)`：是否能在给定人数内完成分配。

## 易错点

- `check` 逻辑方向写反。
- 上下界取值过窄/过宽。
- `while l < r` 与更新规则不匹配。
