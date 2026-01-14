# **LeetCode 3454 – Separate Squares II**

**Difficulty:** Hard  
**Tags:** Sweep Line, Segment Tree, Geometry, Binary Search  
**Link:** [https://leetcode.com/problems/separate-squares-ii/](https://leetcode.com/problems/separate-squares-ii/)

---

## **Problem Summary**

You are given multiple axis-aligned squares on a 2D plane.

Each square is described as:

```
[xi, yi, li]
```

* `(xi, yi)` → bottom-left corner
* `li` → side length

Your task is to find the **minimum y-coordinate** of a horizontal line such that:

> The **total covered area above the line** equals the **total covered area below the line**

---

### ⚠️ Critical Difference from 3453

| Version                        | Overlapping Area           |
| ------------------------------ | -------------------------- |
| **3453 – Separate Squares I**  | counted **multiple times** |
| **3454 – Separate Squares II** | counted **only once**      |

 This single change **completely breaks** the simple binary-search-with-sum approach.

---

## **Why 3453 Strategy Fails Here**

In **3453**, area below `y = h` was:

```
sum of each square's contribution
```

In **3454**, area below `y = h` is:

```
area of UNION of rectangles clipped by y ≤ h
```

That means:

* Overlaps must be **merged**
* You must compute **union area**, not sum
* Area function is **piecewise linear**, not directly additive

---

## **Key Insight**

### 1️⃣ Convert squares into vertical strips

Each square defines:

```
x ∈ [xi, xi + li]
y ∈ [yi, yi + li]
```

We care about **area distribution along y**.

---

### 2️⃣ Use a **Sweep Line on y-axis**

Classic computational geometry trick:

* Treat square bottoms and tops as **events**
* Between consecutive y-events, the set of active x-intervals is constant
* For each horizontal slice:

  ```
  area = (covered x-length) × (height)
  ```

---

### 3️⃣ Reduce problem to:

> Find y where accumulated union-area reaches **total_area / 2**

---

## **High-Level Algorithm**

### Step 1: Create y-events

For each square:

```
(y_start = yi, + interval [xi, xi+li])
(y_end   = yi+li, - interval [xi, xi+li])
```

Sort all events by y.

---

### Step 2: Sweep upward, tracking active x-coverage

Maintain a data structure that supports:

* Add interval `[l, r)`
* Remove interval `[l, r)`
* Query total **union length on x-axis**

 This requires a **Segment Tree + coordinate compression**.

---

### Step 3: Compute total union area

While sweeping:

```
area += (current_x_coverage) × (delta_y)
```

Store prefix area for each y-segment.

---

### Step 4: Find y where area reaches half

Once total area is known:

```
target = total_area / 2
```

Scan segments again (or binary search) to find the **lowest y** where:

```
area_below(y) ≥ target
```

Interpolate linearly within the segment.

---

## **Why This Works**

* Sweep line handles **overlaps correctly**
* Segment tree guarantees exact union length
* Area accumulation is deterministic and precise
* Linear interpolation ensures floating-point accuracy

---

## **Conceptual Diagram**

```
y ↑
│ ┌─────┐
│ │     │     overlapping squares
│ └──┐  │
│    └──┘
│────────── y = h  ← find this line
│██████████ area below
```

Only the **outer boundary** counts.

---

## **Complexity Analysis**

Let `n = number of squares`.

| Aspect                 | Complexity   |
| ---------------------- | ------------ |
| Events                 | `2n`         |
| Coordinate compression | `O(n log n)` |
| Sweep + segment tree   | `O(n log n)` |
| Space                  | `O(n)`       |

 Efficient enough for `n = 5 × 10⁴`

---

## **Why This Is a Hard Problem**

* Requires recognizing **union-area geometry**
* Needs **sweep line + segment tree**
* Binary search alone is insufficient
* Floating-point + geometry + data structures combined

This is **contest-level Hard**, not “tricky Medium”.

---

## **Comparison with 3453**

| Aspect           | 3453               | 3454         |
| ---------------- | ------------------ | ------------ |
| Overlap handling | counted repeatedly | merged       |
| Area function    | simple sum         | union        |
| Technique        | binary search      | sweep line   |
| Data structure   | none               | segment tree |
| Difficulty       | Medium             | Hard         |

---

## **One-Line Interview Summary**

> “Use a sweep line on the y-axis with a segment tree to track x-interval union length, accumulate union area, and find the lowest y where cumulative area reaches half.”

---

## **What You Should Take Away**

* If **overlaps count once** → think **union area**
* Union area in 2D → **sweep line**
* Balance problems → **prefix area + interpolation**
* This is a **template problem** for advanced geometry
