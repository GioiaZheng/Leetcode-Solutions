# 26. Remove Duplicates from Sorted Array

**Difficulty:** Easy  
**Topics:** Array, Two Pointers  
**Link:** https://leetcode.com/problems/remove-duplicates-from-sorted-array/

---

##  Problem Description

You are given a sorted integer array `nums`.  
You must remove duplicates *in-place* such that each unique element appears **only once**, and the relative order stays the same.

Let the number of unique elements be **k**.  
Your function should:

1. Return `k`
2. Ensure the first `k` elements of `nums` contain the unique values in sorted order
3. The remaining elements can be ignored

### The judge will run:
```

k = removeDuplicates(nums)
assert k == expected_length
assert nums[:k] == expected_array

```

---

##  Examples

### Example 1
```

Input: nums = [1,1,2]
Output: 2, nums = [1,2,_]

```

### Example 2
```

Input: nums = [0,0,1,1,1,2,2,3,3,4]
Output: 5, nums = [0,1,2,3,4,*,*,*,*,_]

```

---

##  Key Idea — Two Pointers

Because the array is sorted, all duplicates are adjacent.

We use:

- `i` → the position where the next **unique element** should be written  
- `j` → scans through the array

Whenever we encounter a new number:

```

nums[j] != nums[i]
→ move i forward
→ write nums[j] into nums[i]

```

### Final answer:
```

k = i + 1

```

---

##  Algorithm

1. Start with `i = 0`
2. Loop `j` from 1 to end
3. When `nums[j] != nums[i]`, move i and copy:
```

i += 1
nums[i] = nums[j]

```
4. Return `i + 1`

---

##  Complexity

```

Time:  O(n)
Space: O(1)

````

---

## ✔ Summary

* Use two pointers
* Only overwrite when a new value appears
* Result stored in first `k` positions
* In-place and O(1) extra space

Perfect for interviews.

