# **LeetCode 1970 – Last Day Where You Can Still Cross**

**Difficulty:** Hard  
**Tags:** Binary Search, BFS, Graph, Matrix  
**Link:** [https://leetcode.com/problems/last-day-where-you-can-still-cross/](https://leetcode.com/problems/last-day-where-you-can-still-cross/)

---

## **Problem Summary**

You are given a grid with `row` rows and `col` columns.

* Initially (day `0`), all cells are **land**.
* Each day, **one cell becomes water**.
* You are given the flooding order in `cells`, where:

  ```
  cells[i] = [r, c]   (1-based)
  ```

  means cell `(r, c)` becomes water on day `i + 1`.

You can move **up, down, left, right** on land cells.

Your goal is to find the **last day** on which it is still possible to walk from:

* **any cell in the top row**
* to **any cell in the bottom row**

using only land cells.

---

## **Key Insight**

* As days go by, **more cells become water**.
* Once it becomes impossible to cross, it will **never become possible again**.

This gives a **monotonic property**:

```
Day:   0   1   2   3   4   ...
CanCross:
       T   T   T   F   F
```

This allows us to use **Binary Search on the answer**.

---

## **Approach**

### Step 1: Binary Search on Day

* Search for the **largest day `d`** such that crossing is still possible.
* Search range: `[0, row × col]`

---

### Step 2: Feasibility Check (`can_cross(day)`)

For a given day `d`:

1. Build the grid:

   * Mark the first `d` flooded cells as water.
2. Start BFS from **all land cells in the top row**.
3. Traverse only land cells.
4. If any BFS path reaches the **bottom row**, crossing is possible.

---

### Step 3: Return the Best Day

* If crossing is possible at `mid`, try later days.
* Otherwise, try earlier days.
* Track the maximum valid day.

---

## **Example**

### Example 1

```
Input:
row = 2, col = 2
cells = [[1,1],[2,1],[1,2],[2,2]]

Output: 2
```

Explanation:

```
Day 2 is the last day where a land path exists
```

---

### Example 2

```
Input:
row = 2, col = 2
cells = [[1,1],[1,2],[2,1],[2,2]]

Output: 1
```

---

### Example 3

```
Input:
row = 3, col = 3
cells = [[1,2],[2,1],[3,3],[2,2],[1,1],[1,3],[2,3],[3,2],[3,1]]

Output: 3
```

---

## **Why This Works**

* Flooding is irreversible → feasibility is monotonic.
* Binary search efficiently finds the boundary.
* BFS guarantees correct reachability checking.
* Grid size is limited, making repeated BFS feasible.

---

## **Complexity**

| Aspect | Complexity                |
| ------ | ------------------------- |
| Time   | **O(R × C × log(R × C))** |
| Space  | **O(R × C)**              |

Where:

* `R = row`
* `C = col`

---

## **What I Learned**

* How to recognize **Binary Search on Answer** problems.
* Why monotonicity is crucial for optimization.
* How BFS can be used as a feasibility checker.
* A classic Hard problem combining search and graph traversal.

---

### Notes

There is also an advanced solution using **Union-Find (DSU)**:

* Process days **in reverse**
* Turn water back into land
* Stop when top and bottom rows become connected

The binary search + BFS solution is usually preferred for clarity and interviews.

---

## **One-Line Interview Summary**

> “The feasibility of crossing is monotonic, so we binary search the day and use BFS to check reachability.”
