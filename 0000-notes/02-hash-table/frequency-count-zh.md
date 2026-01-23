# 频次统计（中文版）

本笔记聚焦“频次统计”这一类哈希应用。英文详版见：[frequency-count.md](frequency-count.md)。

---

## 核心思想

- 用哈希表记录每个元素出现次数。
- 常用于：
  - 找众数/最高频
  - 判断变位词
  - 频次差/频次匹配

---

## 模板

```python
from collections import Counter
freq = Counter(nums)
```

或手动更新：

```python
freq = {}
for x in nums:
    freq[x] = freq.get(x, 0) + 1
```

---

## 易错点

- 忘记初始化/更新
- 只统计一次，忽略增量维护
