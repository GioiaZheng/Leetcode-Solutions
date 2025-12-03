# 3625 — Count Number of Trapezoids II

This problem asks for the number of unique trapezoids that can be formed from a set of distinct points on the 2D plane.  
A trapezoid is defined as a **convex quadrilateral with at least one pair of parallel sides**.

Direct combinatorial enumeration of all 4-point subsets is impossible (up to 2.6 billion combinations), so the solution requires a mathematical and geometric approach.

## Key Idea

A quadrilateral is a trapezoid if and only if it has **at least one pair of parallel sides**.  
Thus, we count:

```

(All quadrilaterals with ≥1 pair of parallel sides)
− (All parallelograms)

```

Parallelograms must be removed because they contain **two** pairs of parallel sides.

### Main Components

1. **Parallel lines detection**
   - For each pair of points, compute the reduced slope `(sx, sy)` and line constant `sx*y − sy*x`.
   - Parallel lines share the same slope but have different constants.
   - If two different parallel lines have `c1` and `c2` segments, they can form `c1*c2` quadrilaterals with a pair of parallel sides.

2. **Parallelogram detection**
   - A parallelogram’s diagonals have the same midpoint.
   - Count all pairs of segments with the same midpoint (using doubled coordinates).
   - Each parallelogram is counted twice → divide by 2.

### Final formula

```

Answer = parallel_line_pairs − (parallelogram_pairs / 2)

```

## Time Complexity

```

O(n^2)

```

Works for up to n = 500.

## Files

- `solution.py` — Final efficient implementation
- `Notes.md` — Full mathematical explanation and reasoning
