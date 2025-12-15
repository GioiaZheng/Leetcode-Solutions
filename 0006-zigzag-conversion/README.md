# **LeetCode 6 – Zigzag Conversion**

**Difficulty:** Medium  
**Tags:** String, Simulation  
**Link:** [https://leetcode.com/problems/zigzag-conversion/](https://leetcode.com/problems/zigzag-conversion/)

---

## **Problem Summary**

You are given a string `s` and an integer `numRows`.

The string is written in a **zigzag pattern** across `numRows` rows, then read **row by row** to form a new string.

Your task is to return the resulting string after performing this zigzag conversion.

---

## **Key Insight**

The zigzag pattern is essentially a **simulation of moving vertically and diagonally across rows**.

Instead of constructing a 2D matrix, we can observe that:

* Characters are added **row by row**
* The current row moves:

  * **Down** until the last row
  * Then **up** until the first row
* This movement repeats until all characters are processed

So the problem reduces to:

> Simulate the row movement and collect characters for each row.

---

## **Approach**

We simulate the zigzag traversal using three variables:

* `rows`: a list of strings, one for each row
* `curr_row`: the current row index
* `direction`: indicates whether we are moving **down (+1)** or **up (−1)**

### Step-by-step logic:

1. Handle edge cases:

   * If `numRows == 1` or `numRows >= len(s)`, the zigzag pattern does not exist.
     Return `s` directly.
2. Initialize an array of empty strings for each row.
3. Traverse each character in `s`:

   * Append the character to `rows[curr_row]`
   * Reverse direction when reaching the top (`0`) or bottom (`numRows - 1`)
   * Move to the next row based on the current direction
4. Concatenate all rows to produce the final string.

---

## **Algorithm**

```python
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s

        rows = [""] * numRows
        curr_row = 0
        direction = -1

        for ch in s:
            rows[curr_row] += ch

            if curr_row == 0 or curr_row == numRows - 1:
                direction *= -1

            curr_row += direction

        return "".join(rows)
```

---

## **Example Walkthrough**

### **Input**

```
s = "PAYPALISHIRING"
numRows = 3
```

### **Zigzag Layout**

```
P   A   H   N
A P L S I I G
Y   I   R
```

### **Row-wise Reading**

```
"PAHNAPLSIIGYIR"
```

---

### **Another Example**

```
s = "PAYPALISHIRING"
numRows = 4
```

Zigzag layout:

```
P     I    N
A   L S  I G
Y A   H R
P     I
```

Output:

```
"PINALSIGYAHRPI"
```

---

## **Why This Works**

The zigzag pattern follows a predictable vertical movement:

* Downward traversal until the bottom row
* Upward traversal until the top row
* Direction switches only at boundaries

By tracking the current row and direction, we replicate this movement exactly without extra space or complex indexing.

This approach avoids unnecessary 2D structures while remaining easy to understand and implement.

---

## **Complexity Analysis**

* **Time Complexity:** `O(n)`
  Each character is processed once.

* **Space Complexity:** `O(n)`
  Additional space is used to store row strings.

---

## **What I Learned**

* How to model zigzag traversal using simple state variables
* Why simulation is often the clearest solution for pattern-based problems
* How to handle edge cases that eliminate the zigzag structure entirely
* How to transform a visual pattern problem into linear string construction
