# 回溯模板（中文版）

回溯用于枚举“所有可能解”，本质是 DFS + 撤销选择。

## 标准模板

```python
ans = []
path = []

def dfs(start):
    if 满足结束条件:
        ans.append(path[:])
        return
    for choice in 可选集合:
        if 不合法:
            continue
        path.append(choice)      # 做选择
        dfs(下一状态)            # 进入下一层
        path.pop()               # 撤销选择
```

## 经典题型

- 全排列
- 组合总和
- 子集
- N 皇后

## 剪枝思想

- 提前判断不可能成功的分支。
- 排序后跳过重复元素。

## 例子：子集

每个元素只有“选/不选”两种选择，按索引递归展开。

## 易错点

- 忘记回退 `pop()`。
- 结果直接 append(path) 导致引用问题（应拷贝）。
- 去重条件写错导致漏解或重解。
