#  **Binary Search — Complete Handbook**

Binary Search is far more than “searching in a sorted array.”
It is a **general-purpose optimization and decision-making strategy** used in:

* Feasibility checking
* Optimization problems
* Resource allocation
* Monotonic decision functions
* Continuous numerical solving
* Searching implicitly defined solutions

This handbook explains **how Binary Search works**, **why it works**, and — most importantly — **how to recognize when a problem demands it**.

---

# **Chapter 1 — Concept & Motivation**

Binary Search is based on one core idea:

> **If the search space is ordered and there exists a monotonic property,
> we can repeatedly cut the space in half.**

This yields:

```
Time Complexity: O(log N)
```

Binary Search is exponentially faster than linear scanning and is considered one of the most powerful algorithmic paradigms.

---

# **Chapter 2 — Core Theory**

Binary Search requires three conditions:

### ✔ 1. An ordered search domain

### ✔ 2. A monotonic predicate

### ✔ 3. A boundary to locate

The predicate must have the form:

```
False False False | True True True
                  ↑ boundary
```

or symmetrically:

```
True True True | False False False
```

Binary Search finds the transition point.

---

# **2.1 Mathematical Interpretation (Expert View)**

Binary Search can be formalized as:

Given a domain ( D \subseteq \mathbb{R} ) and a **monotonic function**
( P : D \to {True, False} ), we want:

```
boundary = min { x ∈ D | P(x) = True }
```

This explains why:

* Binary Search does **not** require a sorted array
* The searched value **may not exist** in the array
* The domain can be integers, reals, indexes, or abstract answers

Binary Search is simply an **inversion of a monotonic Boolean function**.

---

# **2.2 Binary Search Invariants (Most Important Section)**

Binary Search works only because it maintains **invariants**.

### **Classic Search**

```
Invariant:
If the target exists, it is always inside nums[left … right].
```

### **Lower Bound**

```
Invariant:
All indices < left satisfy nums[i] < target.
All indices ≥ right satisfy nums[i] ≥ target.
```

### **Binary Search on Answer**

```
Invariant:
hi is always a feasible answer.
lo is always an infeasible value + 1.
```

Maintaining correct invariants prevents infinite loops and guarantees correctness.

---

# **Chapter 3 — Binary Search Templates (with Invariants)**

## **Template 1 — Exact Search in Sorted Array**

```python
def binary_search(nums, target):
    left, right = 0, len(nums) - 1

    while left <= right:
        mid = (left + right) // 2

        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1
```

**Invariant**: target (if it exists) is always in `[left, right]`.

---

## **Template 2 — Lower Bound (first index with nums[i] ≥ target)**

```python
def lower_bound(nums, target):
    left, right = 0, len(nums)

    while left < right:
        mid = (left + right) // 2

        if nums[mid] < target:
            left = mid + 1
        else:
            right = mid

    return left
```

---

## **Template 3 — Upper Bound (first index with nums[i] > target)**

```python
def upper_bound(nums, target):
    left, right = 0, len(nums)

    while left < right:
        mid = (left + right) // 2

        if nums[mid] <= target:
            left = mid + 1
        else:
            right = mid

    return left
```

---

## **Template 4 — Binary Search on Answer (Most Important Template)**

Used for optimization problems such as:

* smallest x that satisfies a condition
* minimum time, maximum distance
* partitioning limits
* feasibility problems

```python
def binary_search_answer(lo, hi):
    while lo < hi:
        mid = (lo + hi) // 2

        if P(mid):      # mid is feasible
            hi = mid    # try smaller
        else:
            lo = mid + 1

    return lo
```

**Invariant**:
`hi` is always feasible; `lo` is always infeasible.

---

# **Chapter 4 — Types of Binary Search Problems**

Binary Search appears in many forms.
The 8 canonical categories used in Google / Meta training:

---

## **1. Exact Value Search**

Find target in a sorted array.

---

## **2. Lower Bound (first ≥ target)**

Classic in DP, LIS, searching insertion positions.

---

## **3. Upper Bound (first > target)**

Used for frequency counting, segments, scheduling.

---

## **4. Last Occurrence / Last ≤ target**

A simple variation using inversion.

---

## **5. Unimodal / Peak Search**

Function increases then decreases (mountain array).

---

## **6. Predicate Search**

Find the smallest x such that P(x) is True.
The most common form in real algorithmic problems.

---

## **7. Binary Search on Answer**

Search a numeric answer (capacity, days, speed, cost).

Works even if answer is outside or not inside the input array.

---

## **8. Implicit Binary Search**

Binary Search on something not explicitly stored:

* LC 4 Median of Two Sorted Arrays
* Partition index search
* Derivatives of monotonic structures

This is the highest-level usage.

---

# **Chapter 5 — Binary Search on Continuous Space (Reals)**

Binary Search also works on floating-point domains.

Used to solve equations or minimize/maximize continuous values.

```python
def binary_search_real(lo, hi, eps=1e-6):
    while hi - lo > eps:
        mid = (lo + hi) / 2
        
        if P(mid):
            hi = mid
        else:
            lo = mid
            
    return lo
```

Applications:

* square roots
* physics optimization
* minimize maximum distance (LC 774)
* probabilities in monotonic functions

---

# **Chapter 6 — Applications & Pattern Recognition**

To identify a Binary Search problem, ask:

### ✔ Is the problem asking for a **minimum / maximum**?

### ✔ Can we check if a candidate x is **feasible**?

### ✔ Is feasibility monotonic?

If YES → **Binary Search on Answer**.

Common phrases indicating Binary Search:

> “Find the minimum x such that …”
> “Find the maximum possible distance …”
> “Determine the smallest threshold that …”
> “Can we do this in ≤ x time?”

---

# **Chapter 7 — Common Mistakes (Professional)**

### ❌ Using the wrong loop condition

* `while left <= right` → exact search
* `while left < right` → boundary finding

---

### ❌ Predicate is not monotonic

Binary Search requires monotonicity:

```
True False True False → INVALID
```

---

### ❌ Infinite loops due to mid not eliminated

Wrong:

```
lo = mid
```

Correct:

```
lo = mid + 1
```

---

### ❌ Wrong initialization of lo and hi

For answer search:

```
lo = smallest possible candidate
hi = largest possible candidate
```

---

### ❌ Overflow in non-Python languages

Write:

```
mid = left + (right - left) // 2
```

---

# **Chapter 8 — Classic Examples**

### **LC 875 — Koko Eating Bananas**

Binary search eating speed.

Predicate:
`P(speed): can finish within H hours?`

---

### **LC 410 — Split Array Largest Sum**

Binary search maximum allowed subarray sum.

---

### **LC 2141 — Maximum Running Time of N Computers**

Binary search time.

Predicate:
`sum(min(battery[i], t)) ≥ n * t`

---

### **LC 1482 — Minimum Days to Make m Bouquets**

Binary search number of days.

---

### **LC 162 — Find Peak Element**

Binary search on gradient.

---

### **LC 153 — Find Minimum in Rotated Sorted Array**

Uses structural monotonicity + ordering analysis.

---

### **LC 1201 — Ugly Number III**

Binary search the k-th valid integer.

---

### **LC 774 — Minimize Max Distance to Gas Station**

Binary search on **real numbers**.

---

# **Chapter 9 — Binary Search Checklist (Interview-Ready)**

### **Before Coding**

✔ What is my search space?  
✔ Is it ordered?  
✔ Is the predicate monotonic?  
✔ Am I searching for the first True or first False?  
✔ What are correct initial values of `lo` and `hi`?  
✔ When P(mid) is True, do I move `hi` or `lo`?  
✔ What is the invariant?  

### **After Coding**

✔ Test extreme values  
✔ Test boundary transitions  
✔ Test cases with all True / all False  
✔ Ensure loop terminates  
✔ Ensure `lo == hi` is the solution  

---

# **Chapter 10 — Exercises for Mastery**

1. Implement a generic binary search with predicate injection.
2. Solve LC 875, LC 410, LC 2141 using Template 4.
3. Prove the correctness of `while left < right` boundary search.
4. Implement binary search on real numbers.
5. Derive predicates for scheduling, partitioning, and distance problems.
6. Show an example where binary search fails due to non-monotonicity.
