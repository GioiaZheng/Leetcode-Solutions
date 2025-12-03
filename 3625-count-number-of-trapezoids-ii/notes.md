# 3625.Count Number of Trapezoids II

This document provides a full mathematical and geometric explanation of the algorithm used to count trapezoids efficiently.

---

# 1. Problem Overview

Given `n ≤ 500` distinct points, we want to count the number of trapezoids, defined as convex quadrilaterals with **at least one pair of parallel sides**.

A direct brute-force check over all quadruples (`C(n,4) ≈ 2.6 billion`) is impossible.  
Thus, geometry and number theory are required.

---

# 2. Key Observation

A quadrilateral is a trapezoid ⇔ it has **≥ 1 pair of parallel sides**.

Parallelograms also satisfy this condition (they have 2 parallel pairs), and thus must be handled carefully.

We compute:

```

Trapezoids = (All quadrilaterals with parallel sides) − (Parallelograms)

```

---

# 3. Representing Lines From Point Pairs

Every pair of points `(x1, y1)` and `(x2, y2)` defines a line segment.  
We want to group these segments according to:

1. **Slope** → identifies direction (parallelism)
2. **Intercept-like constant** → identifies which parallel line the segment lies on

---

# 4. Normalizing the Slope

Let:

```

dx = x2 − x1
dy = y2 − y1

```

Normalize by:

1. Making the direction consistent:
```

(dx > 0) or (dx == 0 and dy > 0)

```

2. Reducing by the greatest common divisor:

```

g = gcd(dx, |dy|)
sx = dx / g
sy = dy / g

```

Now `(sx, sy)` is a unique reduced slope for all parallel lines.

---

# 5. Computing a Line Identifier (Parallel Classes)

For the normalized slope `(sx, sy)`:

The quantity

```

constant = sx * y − sy * x

```

is invariant for any point `(x, y)` on the same line.

For fixed slope:
- Same constant → same exact line
- Different constants → parallel but distinct lines

Thus, we store:

```

t[(sx, sy)][constant] += 1

```

where the value is the number of segments lying on that line.

---

# 6. Counting All Quadrilaterals With Parallel Sides

For each slope group:

Let the parallel lines have segment counts:

```

c1, c2, c3, ..., ck

```

Any pair of lines `(i, j)` creates:

```

c_i * c_j

```

quadrilaterals that have at least one pair of parallel sides.

Summing over all slope groups gives:

```

parallel_pairs

```

---

# 7. Detecting Parallelograms

A parallelogram’s diagonals share the same midpoint.

For segment between points i and j:

```

midpoint = (x_i + x_j, y_i + y_j)

```

(using doubled integer form)

Segments with the same midpoint pair to form parallelograms.

If a midpoint appears `m` times, it forms:

```

C(m,2)

```

parallelograms.

However, each parallelogram is counted twice (AB–CD and AD–BC),  
so we divide the total by 2.

We compute these midpoint groups using the original direction vector `(dx, dy)`:

```

v[(dx,dy)][constant] += 1

```

Finally:

```

parallelogram_pairs = count(v) / 2

```

---

# 8. Final Answer

```

Answer = parallel_pairs − parallelogram_pairs

```

Ensuring that parallelograms are not counted as trapezoids.

---

# 9. Time Complexity Analysis

- We iterate through all point pairs: `O(n²)`
- Hash map operations are `O(1)` on average
- Total time: `O(n²)` which is optimal for `n = 500`

This is efficient, elegant, and mathematically complete.
