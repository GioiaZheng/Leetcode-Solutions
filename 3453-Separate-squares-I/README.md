# **LeetCode 3453 – Separate Squares I**

**Difficulty:** Medium  
**Tags:** Binary Search, Geometry, Prefix Area  
**Link:** https://leetcode.com/problems/separate-squares-i/

---

## **Problem Summary**

You are given several axis-aligned squares on a 2D plane.

Each square is represented as:
```

[xi, yi, li]

```
- `(xi, yi)` is the **bottom-left corner**
- `li` is the **side length**

Your task is to find the **minimum y-coordinate** of a horizontal line such that:

> The **total area of all squares above the line** equals the **total area below the line**

### Important Notes
- Squares **may overlap**
- Overlapping areas are **counted multiple times**
- Answers within **1e-5** of the correct value are accepted

---

## **Key Insight**

The problem can be reduced to finding a value `y = h` such that:

```

Area_below(h) = Total_area / 2

```

### Why this works:
- For any horizontal line `y = h`, the **area below the line** is a **continuous and monotonic increasing function**
- As `h` increases, more of each square lies below the line
- This makes the problem a perfect candidate for **Binary Search on Answer**

---

## **How Area Is Computed**

For a single square `[x, y, l]`:

- If `h ≤ y`  
  → The square is completely above the line → contributes `0`
- If `h ≥ y + l`  
  → The square is completely below the line → contributes `l²`
- Otherwise  
  → The line cuts the square → contributes `l × (h − y)`

The total area below the line is the sum of contributions from all squares.

---

## **Approach**

### Step 1: Compute Total Area
Sum up `l²` for all squares and divide by 2 to get the target area.

---

### Step 2: Binary Search on y-coordinate

Search range:
- `low = min(yi)`
- `high = max(yi + li)`

At each step:
- Compute `mid`
- If `area_below(mid) < target` → move line upward
- Otherwise → move line downward

Repeat until the desired precision is reached.

---

## **Example**

### Example 1
```

Input:
[[0,0,1],[2,2,1]]

Output:
1.00000

```

Explanation:
Any horizontal line between `y = 1` and `y = 2` splits the total area equally.
The smallest valid value is `1`.

---

### Example 2
```

Input:
[[0,0,2],[1,1,1]]

Output:
1.16667

````

The areas above and below `y = 7/6` are equal.

---

## **Why This Works**

* Area accumulation is **linear and continuous**
* The function is **monotonic**, enabling binary search
* Overlapping squares do not complicate the logic because areas are counted independently
* Avoids complex geometry or sweep-line techniques

---

## **Complexity Analysis**

Let `n` be the number of squares.

| Aspect | Complexity       |
| ------ | ---------------- |
| Time   | **O(n · log R)** |
| Space  | **O(1)**         |

> `R` is the numeric range of y-values, not the number of squares.

---

## **What I Learned**

* How to apply **binary search on continuous answers**
* Modeling geometry problems using monotonic functions
* Handling overlaps correctly by counting areas independently
* Precision control in floating-point binary search

---

## **Related Problems**

* 218. The Skyline Problem
* 699. Falling Squares
* 850. Rectangle Area II

---

## **One-Line Interview Summary**

> “Model the area below a horizontal line as a monotonic function of y and use binary search to find where it equals half of the total square area.”
