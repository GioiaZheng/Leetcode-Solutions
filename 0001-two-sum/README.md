# **LeetCode 1 – Two Sum**

**Difficulty:** Easy  
**Tags:** Array, Hash Table  
**Link:** [https://leetcode.com/problems/two-sum/](https://leetcode.com/problems/two-sum/)

---

## **Problem Summary**

Given an integer array `nums` and an integer `target`, return **indices** of the two numbers such that their sum equals `target`.

Constraints:

* You must use **two different elements**.
* Each input has **exactly one solution**.
* The answer may be returned in any order.

---

## **Key Insight**

The key relationship is:

$$
\text{num}_i + \text{num}_j = \text{target}
$$

Which implies:

$$
\text{num}_j = \text{target} - \text{num}_i
$$

So for each number, we check if its **complement** already appeared earlier.

A hash map lets us check this in **O(1)** time.

---

## **Approach**

1. Create a hash map (`seen`) that stores:

   ```
   number → index
   ```
2. Loop through the array:

   * Compute complement: `target - num`
   * If complement exists in the map → solution found
   * Otherwise, record current number and continue
3. Return the pair of indices.

Because the problem guarantees **exactly one solution**, we do not need extra checks.

---

## **Example**

### Example 1

```
nums = [2,7,11,15], target = 9
```

Explanation:

* At index 0: 2 → complement = 7 (not seen yet)
* At index 1: 7 → complement = 2 (seen at index 0)

Result:

```
[0, 1]
```

---

### Example 2

```
nums = [3,2,4], target = 6
Output: [1,2]
```

### Example 3

```
nums = [3,3], target = 6
Output: [0,1]
```

---

## **Why This Works**

* A hash map allows **O(1)** lookup for the complement.
* Each element is processed exactly once → **O(n)** time.
* This avoids the slow brute-force approach (**O(n²)**).

This is the classic optimal solution for Two Sum.

---

## **Complexity**

| Aspect | Complexity                                  |
| ------ | ------------------------------------------- |
| Time   | **O(n)**                                    |
| Space  | **O(n)** (hash map storing visited numbers) |

---

## **What I Learned**

* How hashing helps reduce a quadratic problem to linear time.
* The concept of computing a **complement** for target sum problems.
* Why storing value → index is enough to retrieve the correct pair.
