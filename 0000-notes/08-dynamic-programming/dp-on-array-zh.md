# 数组上的 DP（中文版）

数组 DP 常见于“到 i 位置的最优值/方案数”。

## 典型题型

- 最大子数组和
- 最长递增子序列
- 打家劫舍

## 例子：最大子数组和（Kadane）

```python
best = cur = nums[0]
for x in nums[1:]:
    cur = max(x, cur + x)
    best = max(best, cur)
```

含义：`cur` 是“必须以当前位置结尾”的最大和。

## 例子：打家劫舍

`dp[i] = max(dp[i-1], dp[i-2] + nums[i])`

## 易错点

- 把“以 i 结尾”和“前 i 个元素最优”混为一谈。
- 初始条件漏掉 `n=1`。
