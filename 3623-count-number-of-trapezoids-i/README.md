# **LeetCode 3623 – Count Number of Trapezoids I**

**Difficulty:** Medium
**Tags:** Array, Geometry, Combinatorics
**Link:** [https://leetcode.com/problems/count-number-of-trapezoids-i/](https://leetcode.com/problems/count-number-of-trapezoids-i/)

---

## **Problem Summary**

You are given an array representing the lengths of multiple line segments.
Your task is to count the number of **distinct quadruples** of segments that can form a **trapezoid**.

A trapezoid is defined as a quadrilateral where **at least one pair of opposite sides is parallel**.
In this simplified version of the problem (I), the condition is modeled as follows:

A quadruple of segment lengths forms a trapezoid if:

* After sorting the four chosen lengths (a \le b \le c \le d),
* They satisfy the inequality:

  ```
  c + d > a + b
  ```

This condition corresponds to the quadrilateral inequality under trapezoid constraints.

---

## **Key Insight**

For four segments to form any quadrilateral (including a trapezoid), the **largest two sides** must exceed the sum of the **smallest two sides**.
Thus, for a valid quadruple:

```
c + d > a + b
```

Given a sorted array, we can choose indices `i < j < k < m` and check the inequality efficiently by fixing the larger sides and using two pointers to find how many pairs of smaller sides satisfy the condition.

This reduces the brute-force (O(n^4)) approach to a more manageable combinatorial sweep.

---

## **Approach**

1. Sort the array of segment lengths.
2. Select two indices representing the **two largest sides** of the quadruple:

   * Let these be `k` and `m`.
3. For each pair `(k, m)`:

   * Use two pointers (`i` and `j`) to enumerate all valid smaller-side pairs.
   * Move the pointers according to whether:

     ```
     nums[i] + nums[j] < nums[k] + nums[m]
     ```
4. Accumulate the number of valid `(i, j)` pairs for each `(k, m)`.

Sorting ensures that the inequality behaves monotonically, enabling an efficient scanning process.

---

## **Example**

**Input**

```
nums = [1, 2, 3, 4, 5]
```

**Explanation**
After sorting:

```
[1, 2, 3, 4, 5]
```

All valid quadruples where the two largest sides exceed the sum of the two smallest sides are counted.

**Output**

```
4
```

(Exact quadruple enumeration depends on valid combinations satisfying the trapezoid inequality.)

---

## **Why This Works**

The inequality:

```
largest_two_sum > smallest_two_sum
```

characterizes the trapezoid-forming condition in this simplified version of the problem.

Sorting the array ensures:

* Predictable behavior of sums
* Valid use of two pointers
* Efficient pruning of invalid combinations

By iterating over only the larger sides and counting pairs of smaller sides, the total time complexity is significantly reduced from brute force.

---

## **Complexity**

* **Time:** Typically `O(n^3)` with pointer optimization
* **Space:** `O(1)` aside from sorting

---

## **What I Learned**

* How geometric inequalities translate into array-based constraints.
* Why sorting and two-pointer methods are effective for sum-based combinatorial checks.
* How selecting larger elements first simplifies reasoning about valid combinations.
