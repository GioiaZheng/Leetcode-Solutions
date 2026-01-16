# **LeetCode 2975 – Maximum Square Area by Removing Fences From a Field**

**Difficulty:** Medium  
**Tags:** Geometry, Hash Set, Greedy  
**Link:** https://leetcode.com/problems/maximum-square-area-by-removing-fences-from-a-field/

---

## **Problem Summary**

You are given a large rectangular field with corners at `(1, 1)` and `(m, n)`.

The field is divided by:
- **Horizontal fences** at rows `hFences[i]`
- **Vertical fences** at columns `vFences[i]`

Additionally:
- The **outer boundary fences** at `1` and `m` (horizontal), `1` and `n` (vertical) **cannot be removed**
- Internal fences **can be removed**

Your task is to determine the **maximum possible area of a square field** that can be formed by removing some fences (possibly none).

If **no square** can be formed, return `-1`.

The answer should be returned **modulo `10^9 + 7`**.

---

## **Key Insight**

Removing fences allows you to **merge adjacent rectangular regions**.

A square field is possible **if and only if**:
- The **vertical distance** between two horizontal fences
- Equals the **horizontal distance** between two vertical fences

So the problem becomes:

> **Find the largest common distance that appears in both horizontal gaps and vertical gaps.**

---

## **Reformulation**

1. Consider all horizontal fence positions:
```

[1] + hFences + [m]

```
2. Consider all vertical fence positions:
```

[1] + vFences + [n]

```
3. By removing all fences between two positions, you create a field with:
- Height = difference between two horizontal positions
- Width  = difference between two vertical positions

We want:
```

height == width

```

and maximize:
```

area = side²

```

---

## **Approach**

### Step 1: Collect All Possible Gaps

- Sort horizontal fence positions
- Compute **all possible differences** between pairs → horizontal gaps
- Do the same for vertical fence positions → vertical gaps

---

### Step 2: Find Common Side Lengths

- Store horizontal gaps in a set
- For each vertical gap, check if it exists in the horizontal set
- Track the **maximum common gap**

---

### Step 3: Return Result

- If no common gap exists → return `-1`
- Else return:
```

(max_gap²) % (10^9 + 7)

```

---

## **Example**

### Example 1
```

Input:
m = 4, n = 3
hFences = [2,3]
vFences = [2]

Output:
4

```

Explanation:
- Horizontal gaps: {1, 2}
- Vertical gaps: {1, 2}
- Largest common side = 2
- Area = 2² = 4

---

### Example 2
```

Input:
m = 6, n = 7
hFences = [2]
vFences = [4]

Output:
-1

````

No common horizontal and vertical gap → no square possible.
---

## **Why This Works**

* Removing fences merges regions defined by fence coordinates
* Any square must align with fence lines
* The side length must appear **both horizontally and vertically**
* Brute force is feasible because fence counts are small (≤ 600)

---

## **Complexity Analysis**

Let:

* `H = len(hFences) + 2`
* `V = len(vFences) + 2`

| Aspect | Complexity     |
| ------ | -------------- |
| Time   | **O(H² + V²)** |
| Space  | **O(H²)**      |

This is efficient enough given the constraints.

---

## **What I Learned**

* Geometry problems often reduce to **distance matching**
* Using a **set for fast lookup** simplifies the solution
* Boundary conditions (fixed fences) are crucial
* Sometimes brute force on differences is acceptable and clean

---

## **Related Problems**

* 2943. Maximize Area of Square Hole in Grid
* 221. Maximal Square
* 84. Largest Rectangle in Histogram

---

## **One-Line Interview Summary**

> “Compute all possible distances between horizontal and vertical fences, find the largest common distance, and return its square as the maximum square area.”
