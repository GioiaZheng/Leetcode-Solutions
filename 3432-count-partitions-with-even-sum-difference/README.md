# **3432. Count Partitions with Even Sum Difference**

**Difficulty:** Easy
**Topics:** Prefix Sum, Parity, Math
**Link:** [https://leetcode.com/problems/count-partitions-with-even-sum-difference/](https://leetcode.com/problems/count-partitions-with-even-sum-difference/)

---

##  Problem Summary

You are given an integer array `nums` of length `n`.

A **partition index** `i` (where `0 ≤ i < n − 1`) splits the array into:

* Left subarray: `nums[0…i]`
* Right subarray: `nums[i+1…n−1]`

A partition is **valid** if:

```
(sum(left) − sum(right)) is even
```

Return the **number of valid partitions**.

---

##  Key Insight

Let:

```
left  = prefix sum up to i
right = total − left
```

We need:

```
(left − right) % 2 == 0
```

Using parity rules:

```
(left − right) is even  ⇔  left % 2 == right % 2
```

Substitute `right = total − left`:

```
right % 2 = (total % 2) XOR (left % 2)
```

Setting `left % 2 == right % 2` implies:

```
total % 2 == 0
```

Thus, the entire condition depends solely on the **parity of the total sum**.

---

##  Algorithm

```
1. Compute total = sum(nums)
2. If total is odd → return 0
3. Else → return n − 1
```

---

##  Examples

### Example 1

```
nums = [10,10,3,7,6]
total = 36 (even)

All 4 partitions are valid.

Output: 4
```

### Example 2

```
nums = [1,2,2]
total = 5 (odd)

No valid partitions.

Output: 0
```

### Example 3

```
nums = [2,4,6,8]
total = 20 (even)

All 3 partitions are valid.

Output: 3
```

---

##  Complexity

```
Time:   O(1)
Space:  O(1)
```

---

##  Final Conclusion (Bottom)

### If total sum is **odd** → No valid partitions

### If total sum is **even** → **All (n − 1)** partitions are valid

A simple parity check gives the optimal **O(1)** solution.

要不要我帮你做这些？
