# **LeetCode 1458 – Max Dot Product of Two Subsequences**

**Difficulty:** Hard  
**Tags:** Dynamic Programming, Array, Subsequence  
**Link:** [https://leetcode.com/problems/max-dot-product-of-two-subsequences/](https://leetcode.com/problems/max-dot-product-of-two-subsequences/)

---

## **Problem Summary**

You are given two integer arrays `nums1` and `nums2`.

Your task is to select:

* A **non-empty subsequence** from `nums1`
* A **non-empty subsequence** from `nums2`
* Both subsequences must have the **same length**

Then compute their **dot product**, defined as:

```
a1*b1 + a2*b2 + ... + ak*bk
```

Return the **maximum possible dot product**.

⚠️ Important:

* Subsequences must be **non-empty**
* Values can be **negative**
* The result may also be negative

---

## **Key Insight**

This is a **subsequence DP problem**, similar in structure to:

* Longest Common Subsequence (LCS)
* Maximum sum subsequence alignment

However, there is a crucial twist:

> The subsequence **must be non-empty**, even if all products are negative.

This means:

* We **cannot initialize DP with 0**
* We must allow **negative values** as valid answers

---

## **DP State Definition**

Let:

```
dp[i][j] = maximum dot product using
           nums1[i:] and nums2[j:],
           with at least one pair chosen
```

This ensures:

* Subsequences are aligned
* Non-empty constraint is enforced

---

## **DP Transition**

At position `(i, j)`, we have three choices:

 **Take both elements**

```
nums1[i] * nums2[j] + max(0, dp[i+1][j+1])
```

 **Skip nums1[i]**

```
dp[i+1][j]
```

 **Skip nums2[j]**

```
dp[i][j+1]
```

So:

```
dp[i][j] = max(
    nums1[i] * nums2[j] + max(0, dp[i+1][j+1]),
    dp[i+1][j],
    dp[i][j+1]
)
```

---

## **Why `max(0, dp[i+1][j+1])`?**

* If continuing the subsequence **hurts the sum**, we stop
* This allows starting a new subsequence at `(i, j)`
* Ensures at least one pair is chosen

This is the **key trick** of the problem.

---

## **Example**

### Example 1

```
nums1 = [2,1,-2,5]
nums2 = [3,0,-6]
```

Optimal choice:

```
[2, -2] and [3, -6]
Dot product = 2*3 + (-2)*(-6) = 18
```

---

### Example 3 (All negative result)

```
nums1 = [-1,-1]
nums2 = [1,1]
```

Only valid result:

```
-1 * 1 = -1
```

Answer is **-1**, not 0.

---

## **Why This Works**

* Dynamic programming explores all valid alignments
* The transition ensures:

  * Subsequences remain aligned
  * At least one pair is selected
* Negative-only cases are handled correctly
* The DP structure mirrors classical sequence alignment problems

---

## **Complexity**

Let:

* `n = len(nums1)`
* `m = len(nums2)`

| Aspect | Complexity   |
| ------ | ------------ |
| Time   | **O(n · m)** |
| Space  | **O(n · m)** |

With `n, m ≤ 500`, this is acceptable.

---

## **What I Learned**

* How to adapt LCS-style DP to optimization problems
* Handling **non-empty constraints** in DP
* Why zero-initialization can break correctness
* A classic example of **Hard DP modeling**

---

### Notes

This problem is closely related to:

* 1035. Uncrossed Lines
* 1143. Longest Common Subsequence
* Sequence alignment problems in algorithms

Understanding this greatly strengthens DP intuition.

---

## **One-Line Interview Summary**

> “Use DP like LCS, but maximize dot product and enforce non-empty subsequences by allowing negative results.”
