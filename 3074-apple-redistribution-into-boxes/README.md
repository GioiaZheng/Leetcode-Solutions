# **LeetCode 3074 – Apple Redistribution into Boxes**

**Difficulty:** Easy  
**Tags:** Array, Greedy  
**Link:** [https://leetcode.com/problems/apple-redistribution-into-boxes/](https://leetcode.com/problems/apple-redistribution-into-boxes/)

---

## **Problem Summary**

You are given:

* An array `apple`, where `apple[i]` is the number of apples in the `i`-th pack
* An array `capacity`, where `capacity[j]` is the capacity of the `j`-th box

You want to redistribute all apples into boxes.

Rules:

* Apples from the same pack **can be split** across different boxes.
* Each box has a fixed maximum capacity.
* It is guaranteed that redistribution is possible.

Return the **minimum number of boxes** needed to store all apples.

---

## **Key Insight**

* Since apples can be split freely, we only care about the **total number of apples**.
* The problem reduces to:

  > Pick the **minimum number of box capacities** whose sum is **at least** the total number of apples.
* To minimize the number of boxes, we should always choose the **largest capacity boxes first**.

This leads directly to a greedy solution.

---

## **Approach**

1. Compute the total number of apples.
2. Sort the `capacity` array in **descending order**.
3. Keep adding box capacities until the accumulated capacity is enough.
4. Count how many boxes are used.

---

## **Example**

### Example 1

```
Input: apple = [1,3,2], capacity = [4,3,1,5,2]
Output: 2
```

Explanation:

```
Total apples = 6
Use boxes with capacities 5 and 4 → total capacity = 9
```

---

### Example 2

```
Input: apple = [5,5,5], capacity = [2,4,2,7]
Output: 4
```

Explanation:

```
Total apples = 15
All boxes are needed to reach sufficient capacity
```

---

## **Why This Works**

* Apples can be distributed arbitrarily, so no structural constraints exist.
* Choosing a larger box always dominates choosing a smaller one.
* The greedy choice at each step leads to the optimal global solution.

---

## **Complexity**

| Aspect | Complexity     |
| ------ | -------------- |
| Time   | **O(m log m)** |
| Space  | **O(1)**       |

Where `m = len(capacity)`.

---

## **What I Learned**

* How problem constraints can simplify a problem significantly.
* Why greedy strategies are effective when items are divisible.
* A classic example of a “minimum containers to cover capacity” problem.
* An Easy-level problem that clearly demonstrates greedy thinking.

---

### Notes

This pattern appears frequently in problems involving:

* Minimum number of containers
* Capacity coverage
* Resource allocation with divisible items
