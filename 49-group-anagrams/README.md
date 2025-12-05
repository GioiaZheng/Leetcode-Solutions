# **LeetCode 3625 – Count Number of Trapezoids II**

**Difficulty:** Medium  
**Tags:** Array, Geometry, Combinatorics  
**Link:** [https://leetcode.com/problems/count-number-of-trapezoids-ii/](https://leetcode.com/problems/count-number-of-trapezoids-ii/)

---

## **Problem Summary**

You are given a list of segment lengths.
Your task is to count the number of **distinct quadruples** of segments that can form a **trapezoid** under the extended condition for this version of the problem.

A trapezoid is defined as a quadrilateral with at least one pair of parallel sides.
The problem models this via segment-length constraints that differ slightly from Part I.

In this version, the quadruple ((a, b, c, d)), sorted as:

```
a ≤ b ≤ c ≤ d
```

forms a trapezoid if both of the following hold:

1. The quadrilateral inequality:

   ```
   a + b + c > d
   ```
2. The trapezoid constraint:

   ```
   a + d > b + c
   ```

Both conditions must be satisfied.

---

## **Key Insight**

The validity of a quadruple depends on a pair of inequalities involving both the largest and smallest sides.

Observations:

* Sorting imposes structure:
  (a) and (b) are always the two smaller sides; (c) and (d) are the larger sides.
* The first inequality ensures the four segments can form **any** quadrilateral.
* The second inequality imposes the **specific trapezoid shape** constraint.

Because the inequalities behave monotonically under sorted order, the problem can be solved using nested loops combined with two-pointer techniques to count valid combinations efficiently.

---

## **Approach**

1. Sort the array of segment lengths.

2. Enumerate possible positions for the two largest sides:

   * Let indices `k` and `m` represent the sides `c` and `d`.

3. For the remaining sides (`a` and `b`), use two pointers to find pairs `(i, j)` that satisfy:

   * Quadrilateral inequality:

     ```
     nums[i] + nums[j] + nums[k] > nums[m]
     ```

   * Trapezoid constraint:

     ```
     nums[i] + nums[m] > nums[j] + nums[k]
     ```

4. For valid ranges of `(i, j)`, count all contributing pairs.

5. Continue for all valid `(k, m)` choices.

Sorting ensures that increasing or decreasing a pointer produces predictable effects on the inequalities, enabling efficient counting rather than brute-force enumeration.

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

Only certain quadruples satisfy both required inequalities.
The exact count depends on combinations meeting the extended trapezoid constraints.

**Output**

```
2
```

---

## **Why This Works**

The problem reduces to checking all quadruples that satisfy two inequalities.
Because the array is sorted, inequalities become monotonic:

* Increasing larger sides raises the right-hand side of one inequality.
* Increasing smaller sides raises the left-hand side of both inequalities.

This structure allows efficient two-pointer scanning for `(a, b)` once `(c, d)` are fixed.

Instead of checking every possible combination explicitly, we exploit monotonicity to count valid pairs in linear time per `(c, d)` selection.

---

## **Complexity**

* **Time:** Approximately `O(n^3)` with efficient pointer movement
* **Space:** `O(1)` aside from sorting

---

## **What I Learned**

* How trapezoid constraints translate into algebraic conditions on sorted segment lengths.
* How to navigate dual inequality constraints using pointer-based enumeration.
* How geometric counting problems benefit from structural ordering of input values.
