# **LeetCode 3047 – Find the Largest Area of Square Inside Two Rectangles**

**Difficulty:** Medium  
**Tags:** Geometry, Brute Force, Enumeration  
**Link:** https://leetcode.com/problems/find-the-largest-area-of-square-inside-two-rectangles/

---

## **Problem Summary**

You are given `n` axis-aligned rectangles on a 2D plane.

Each rectangle `i` is defined by:
- `bottomLeft[i] = [ai, bi]`
- `topRight[i] = [ci, di]`

You must find the **maximum area of a square** that can fit **inside the intersection region of at least two rectangles**.

- The square must be fully contained in the intersection.
- The intersection may involve **more than two rectangles**, but considering pairs is sufficient.
- If **no two rectangles intersect**, return `0`.

---

## **Key Insight**

### 1️⃣ Intersection of Two Rectangles

The intersection of two axis-aligned rectangles (if it exists) is itself a rectangle.

For rectangles `i` and `j`:

- Bottom-left of intersection:
```

x_left   = max(x1_i, x1_j)
y_bottom = max(y1_i, y1_j)

```

- Top-right of intersection:
```

x_right = min(x2_i, x2_j)
y_top   = min(y2_i, y2_j)

```

The intersection exists **if and only if**:
```

x_left < x_right  AND  y_bottom < y_top

```

---

### 2️⃣ Largest Square Inside a Rectangle

If an intersection rectangle has:
```

width  = x_right - x_left
height = y_top - y_bottom

```

The **largest square** that can fit inside it has:
```

side = min(width, height)
area = side²

````

---

## **Approach**

### Step 1: Enumerate All Rectangle Pairs

Since `n ≤ 1000`, we can safely enumerate all pairs `(i, j)` with `i < j`.

---

### Step 2: Compute Intersection

For each pair:
- Compute the intersection rectangle
- If it exists, compute the largest square that fits inside it

---

### Step 3: Track Maximum Area

Keep a global maximum across all rectangle pairs.
---

## **Example**

### Example 1

```
Input:
bottomLeft = [[1,1],[2,2],[3,1]]
topRight   = [[3,3],[4,4],[6,6]]

Output:
1
```

Explanation:

* Rectangles (0,1) and (1,2) both intersect
* The largest square that fits has side length `1`
* Area = `1`

---

### Example 4

```
Input:
bottomLeft = [[1,1],[3,3],[3,1]]
topRight   = [[2,2],[4,4],[4,2]]

Output:
0
```

Explanation:

* No two rectangles intersect
* No square can be formed

---

## **Why This Works**

* Any square must lie inside the intersection of at least two rectangles
* The intersection geometry is simple and deterministic
* Checking all pairs guarantees no valid case is missed
* The largest square inside a rectangle is constrained by its smaller side

---

## **Complexity Analysis**

Let `n` be the number of rectangles.

| Aspect | Complexity |
| ------ | ---------- |
| Time   | **O(n²)**  |
| Space  | **O(1)**   |

This is efficient enough for `n ≤ 1000`.

---

## **What I Learned**

* Intersection of axis-aligned rectangles is easy to compute
* Geometry problems often reduce to careful boundary comparisons
* Brute-force pair enumeration can be optimal when constraints allow
* For square problems, the **minimum side length** is always the limiter

---

## **Related Problems**

* 2975. Maximum Square Area by Removing Fences From a Field
* 2943. Maximize Area of Square Hole in Grid
* 221. Maximal Square

---

## **One-Line Interview Summary**

> “Enumerate all rectangle pairs, compute their intersection, and the largest square inside it has area equal to the square of the minimum of the intersection’s width and height.”
