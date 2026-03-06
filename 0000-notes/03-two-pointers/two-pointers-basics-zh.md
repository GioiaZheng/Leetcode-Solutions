# 双指针基础（中文版）

双指针适合处理“顺序结构 + 两端或同向收缩扩展”。

## 两类双指针

1. **对撞指针**：左右向中间移动（如两数之和 II）。
2. **同向指针**：快慢指针（去重、原地删除）。

## 例子：有序数组两数之和

```python
l, r = 0, len(nums)-1
while l < r:
    s = nums[l] + nums[r]
    if s == target: return [l, r]
    if s < target: l += 1
    else: r -= 1
```

## 例子：删除有序数组重复项

```python
k = 0
for x in nums:
    if k == 0 or x != nums[k-1]:
        nums[k] = x
        k += 1
```

## 易错点

- 指针移动条件写反导致死循环。
- 忘记循环条件是 `<` 还是 `<=`。
- 同向指针时覆盖顺序错误。
