# 频次统计（中文版）

频次统计是哈希最常见子模式，适合“字母出现次数、数字重复次数”类题。

## 标准模板

```python
cnt = {}
for x in arr:
    cnt[x] = cnt.get(x, 0) + 1
```

或使用 `collections.Counter`。

## 典型场景

- 有效字母异位词
- 前 k 高频元素
- 是否可重排成目标形式

## 例子：判断异位词

```python
from collections import Counter
return Counter(s) == Counter(t)
```

## 进阶：频次 + 堆

前 k 高频常见做法：
1. 先统计频次。
2. 再用最小堆维护前 k。

## 易错点

- 统计对象错了（字符 vs 单词）。
- 忘记处理大小写与空格规则。
- 排序比较时，频次相同的 tie-break 未按题意处理。
