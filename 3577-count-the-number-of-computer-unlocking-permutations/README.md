# **LeetCode 3577 – Count the Number of Computer Unlocking Permutations**

**Difficulty:** Medium  
**Tags:** Sorting, Feasibility Check, Combinatorics  
**Link:** [https://leetcode.com/problems/count-the-number-of-computer-unlocking-permutations/](https://leetcode.com/problems/count-the-number-of-computer-unlocking-permutations/)

---

## **Problem Summary**

You are given an array `complexity` of length `n`, where each `complexity[i]` represents the password complexity of computer `i`.

Computer **0 is already unlocked**.
Every other computer `i` must be unlocked using some previously unlocked computer `j`, and this is only allowed when:

```
j < i   AND   complexity[j] < complexity[i]
```

A permutation of `[0, 1, 2, ..., n−1]` is valid if it represents an order in which all computers can be legally unlocked.

Your task is to count the number of such valid permutations and return the answer modulo `10^9 + 7`.

---

# **Key Insight (based on this solution)**

Instead of counting permutations through layers or DAG reasoning,
we observe a **much simpler structural fact**:

###  If every computer `i > 0` has **at least one earlier index `j < i` with lower complexity**,

then the unlocking is always feasible **regardless of permutation**,
except for one constraint:

### Computer **0 must appear first**,

because only computer 0 is unlocked at the start.

Once computer `0` is placed first:

* All other computers already satisfy the unlocking condition
* There are **no additional ordering constraints**
* Therefore all remaining `(n−1)!` permutations are valid

###  If any computer violates the condition:

```
min(complexity[0..i−1]) >= complexity[i]
```

then **computer i cannot be unlocked in any sequence**,
and the answer is **0**.

So the entire problem reduces to:

1. **Check feasibility using bisect**
   For each `i`, ensure someone before it has lower complexity.

2. If all pass → answer = `(n−1)! mod 1e9+7`.

This is exactly what your code implements.

---

# **Algorithm Explanation**

### **1. Maintain a sorted multiset of previous complexities**

We insert `complexity[0]`, then for each `i`:

```
cnt = number of previous complexities < complexity[i]
```

This is computed using:

```python
cnt = bisect_left(sortedc, complexity[i])
```

If `cnt == 0`, unlocking is impossible → return `0`.

Otherwise insert the new value using:

```python
bisect.insort(sortedc, complexity[i])
```

---

### **2. If feasibility holds for all nodes**

There is no further dependency.

Only rule:
Computer `0` must be placed first.

Thus:

```
Answer = factorial(n−1) mod (1e9 + 7)
```

Your code computes this iteratively.

---

# **Correctness Intuition**

Why `(n−1)!`?

After verifying feasibility:

1. Computer 0 must be first (already unlocked).
2. Every computer `i > 0` has at least one smaller-complexity predecessor by index.
3. This property **does not depend on permutation order** anymore.

That means:

* Any permutation of the remaining `n−1` computers is valid.
* Those computers impose no additional constraints on each other.

So total valid sequences:

```
1 (fixed first element) × (n−1)! = (n−1)!
```

---

# **Time & Space Complexity**

| Component                     | Complexity   |
| ----------------------------- | ------------ |
| Feasibility check with bisect | `O(n log n)` |
| Computing factorial(n−1)      | `O(n)`       |
| Space usage                   | `O(n)`       |

---

# **What I Learned**

* How to convert dependency rules into a simple feasibility check.
* Using `bisect_left` to efficiently count “how many previous values are smaller.”
* Why only index ordering matters for unlockability, not permutation ordering.
* How feasibility collapses the problem into a simple factorial.
* A clean and optimized `O(n log n)` implementation.
