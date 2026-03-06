# 数组上的二分查找（中文版）

二分前提：搜索空间有序（单调）。

## 两种常见目标

1. 找某个值是否存在。
2. 找边界（第一个 >= target，最后一个 <= target）。

## 标准模板（左闭右闭）

```python
l, r = 0, n - 1
while l <= r:
    mid = (l + r) // 2
    if nums[mid] < target:
        l = mid + 1
    elif nums[mid] > target:
        r = mid - 1
    else:
        return mid
return -1
```

## 边界查找示例

找第一个 `>= target`：
- 若 `nums[mid] >= target`，收缩右边 `r = mid - 1`。
- 否则 `l = mid + 1`。

## 易错点

- 死循环：区间不缩小。
- `mid` 溢出（C++ 可用 `l + (r-l)/2`）。
- 模板混用（左闭右开与左闭右闭混乱）。
