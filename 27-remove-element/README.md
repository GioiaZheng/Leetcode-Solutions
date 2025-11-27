# 27. Remove Element

**Difficulty:** Easy  
**Topics:** Array, Two Pointers  
**Link:** https://leetcode.com/problems/remove-element/

---

##  Problem Description

Given an array `nums` and an integer `val`, remove **all occurrences** of `val` in-place and return the number of remaining elements.

The first `k` elements of `nums` should contain the elements that are **not equal to val**. Order does not matter.

---

##  Examples

### Example 1
```

Input: nums = [3,2,2,3], val = 3
Output: 2, nums = [2,2,*,*]

```

### Example 2
```

Input: nums = [0,1,2,2,3,0,4,2], val = 2
Output: 5, nums = [0,1,4,0,3,*,*,_]

```

---

##  Key Idea — Two Pointers

Use:

- `i` as the scanning pointer
- `index` as the position to write the next element that is not equal to `val`

Process:

1. If `nums[i] != val`, copy it to the front.
2. Increase `index`
3. Return `index + 1` as the number of remaining elements.

---

##  Complexity

```

Time:  O(n)
Space: O(1)

````

---

## ✔ Summary

* Efficient in-place algorithm
* Works in one pass
* Does not preserve order (which is allowed)
* Matches LeetCode judge requirements



你要继续下一题吗？
