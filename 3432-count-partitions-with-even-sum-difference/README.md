# **LeetCode 3432 – Count Partitions with Even Sum Difference**

**Difficulty:** Easy  
**Tags:** Prefix Sum, Math, Parity  
**Link:** [https://leetcode.com/problems/count-partitions-with-even-sum-difference/](https://leetcode.com/problems/count-partitions-with-even-sum-difference/)

---

## **Problem Summary**

You are given an array `nums` of length `n`.
A partition index `i` (where `0 ≤ i < n − 1`) splits the array into:

* Left part: `nums[0..i]`
* Right part: `nums[i+1..n-1]`

A partition is considered valid if:

```
(sum(left) − sum(right)) is even.
```

Your task is to count how many such valid partitions exist.

---

## **Key Insight**

Let:

```
left  = sum of nums[0..i]
right = total_sum − left
```

Then:

```
left − right = 2*left − total_sum
```

Because `2 * left` is always even, the parity of the expression is determined solely by `total_sum`.

This leads to the key observation:

* If `total_sum` is **odd**, then `left − right` is always odd → **no valid partitions**.
* If `total_sum` is **even**, then `left − right` is always even → **all partitions are valid**.

Thus, if the total sum is even, the answer is simply:

```
n − 1
```

---

## **Approach**

1. Compute the total sum of the array.
2. If the sum is odd, return `0`.
3. If the sum is even, return `n − 1`, since every partition index is valid.

This eliminates the need for prefix sums or looping through possible partitions.

---

## **Example**

**Input**

```
nums = [1, 2, 3, 4]
```

**Explanation**

* Total sum = 10 (even)
* All partition indices (0, 1, 2) produce an even difference.

**Output**

```
3
```

---

## **Why This Works**

The difference:

```
left − right = 2*left − total_sum
```

has the same parity as `total_sum` because:

* Multiplying by 2 preserves evenness.
* Subtracting two numbers does not change the underlying parity relationship.

Since `left` can vary but `total_sum` is fixed, the parity of the difference never changes across partitions.
Therefore, the total sum alone determines the answer.

---

## **Complexity**

* **Time:** `O(n)` for computing the total sum
* **Space:** `O(1)`

---

## **What I Learned**

* How parity questions often simplify when expressions are algebraically reduced.
* Why total-sum parity determines the parity of left-right differences.
* How a seemingly partition-based problem can reduce to a constant-time conclusion after preprocessing.
