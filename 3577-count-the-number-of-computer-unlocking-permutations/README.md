# **LeetCode 3577 – Count the Number of Computer Unlocking Permutations**

**Difficulty:** Medium  
**Tags:** Combinatorics, Sorting, Dependency Constraints  
**Link:** [https://leetcode.com/problems/count-the-number-of-computer-unlocking-permutations/](https://leetcode.com/problems/count-the-number-of-computer-unlocking-permutations/)

---

## **Problem Summary**

You are given an array `complexity` of length `n`, where each `complexity[i]` represents the password complexity of computer `i`.

Computer **0 is already unlocked**, and every other computer must be unlocked using some previously unlocked computer.

A computer `i` can be unlocked using computer `j` **if and only if**:

```
j < i   AND   complexity[j] < complexity[i]
```

A permutation of `[0, 1, 2, ..., n−1]` is valid if it represents an order in which all computers can be legally unlocked.

Your task is to count the number of such valid permutations and return the answer modulo `10^9 + 7`.

---

## **Key Insight**

This is not a simple permutation counting problem.
The unlocking rule imposes **strict dependency constraints**:

### A computer `i` can only be unlocked if, before position `i`,

there exists **at least one** computer with **lower complexity**.

This divides computers into **layers**, where:

* A "layer" is a set of computers with the same complexity.
* A layer can only be unlocked after **all earlier layers** have at least one index smaller than each of its members.

### The process becomes:

1. Sort computers by **complexity value** into layers.
2. Layer 0 must contain index **0** (root unlocking source).
   If not → **no valid sequences**.
3. Each later layer can be inserted arbitrarily **after** all earlier layers,
   because all dependencies point to earlier layers.

This means the answer equals a product of **binomial coefficients**, representing:

> How many ways to interleave each layer after prior ones while keeping internal order flexible.

---

## **Approach**

### **1. Group indices by complexity**

Computers with identical complexity form one layer.

Example:

```
complexity = [1, 2, 2, 5, 7]
groups = {1:[0], 2:[1,2], 5:[3], 7:[4]}
```

### **2. Sort layers by increasing complexity**

Unlock conditions depend strictly on complexity.

### **3. Feasibility check**

For each computer `i`:

```
We must verify: exists j < i such that complexity[j] < complexity[i].
```

If a computer has no valid parent, the answer is `0`.

For example:

```
[3, 3, 3, 4, 4, 4] → result = 0
because computers at index 1 and 2 cannot be unlocked by any earlier index.
```

### **4. Count permutations using combinatorics**

Let layer sizes be:

```
L1, L2, L3, ...
```

Layer 1 must contain index `0`.

For each new layer with size `k`, when we have already placed `total` nodes:

Number of ways to insert this layer:

```
C(total + k - 1, k)
```

This corresponds to placing `k` new items into `total` existing positions while ensuring the unlocking constraints.

Final answer is the product of all such binomial coefficients.

### **5. Use factorials + modular inverses**

Combination values require fast computation under modulo `1e9+7`.

---

## **Example**

### **Input**

```
complexity = [1, 2, 3]
```

### Layers

```
1 → [0]
2 → [1]
3 → [2]
```

### Counting

* Layer 1: must start → 1 way
* Layer 2: C(1, 1) = 1
* Layer 3: C(2, 1) = 2

### **Output**

```
2
```

Valid sequences:

```
[0, 1, 2]
[0, 2, 1]
```

---

## **Why This Works**

The unlocking condition forms a **layered DAG structure**:

* All nodes in higher layers depend on at least one node in earlier layers.
* Nodes inside a layer cannot unlock each other because they have equal complexity.
* Unlocking is always possible as long as each layer has at least one dependency in earlier layers.
* Ordering between layers is flexible → combinatorial counting.

Thus, the problem reduces to:

> A layered topological sorting count
> = product of binomial coefficients representing interleaving ways.

This transforms a difficult dependency problem into a clean combinatorics problem.

---

## **Complexity**

| Operation                       | Cost         |
| ------------------------------- | ------------ |
| Sorting complexities            | `O(n log n)` |
| Feasibility checking            | `O(n)`       |
| Precomputing factorials         | `O(n)`       |
| Final combinatorial calculation | `O(n)`       |

**Overall:** `O(n log n)`
**Space:** `O(n)`

---

## **What I Learned**

* How dependency rules can form a layered structure allowing combinatorial counting.
* Why equal-complexity computers cannot unlock each other.
* How to detect impossible scenarios by analyzing index ordering.
* How to transform a DAG-topological-count problem into combinatorics.
* Efficient use of factorials and modular inverses to compute large binomial coefficients.
