# **LeetCode 3379 – Transformed Array**

**Difficulty:** Easy  
**Tags:** Array, Simulation, Modulo  
**Link:** [https://leetcode.com/problems/transformed-array/](https://leetcode.com/problems/transformed-array/)

---

## **Problem Summary**

You are given an integer array `nums` representing a **circular array**.

You need to create a new array `result` of the same length, where for each index `i`:

* If `nums[i] > 0`
  → Move `nums[i]` steps **to the right** from index `i`
* If `nums[i] < 0`
  → Move `abs(nums[i])` steps **to the left** from index `i`
* If `nums[i] == 0`
  → `result[i] = 0`

Because the array is **circular**, moving past either end wraps around.

Return the transformed array `result`.

---

## **Key Insight**

This is a **direct simulation** problem.

The only tricky part is handling the **circular movement**, which can be solved cleanly using:

> **Modulo arithmetic**

Instead of manually wrapping indices, we can directly compute the destination index.

---

## **Core Observation**

For any index `i`:

```
target_index = (i + nums[i]) % n
```

Why this works:

* Positive `nums[i]` → moves right
* Negative `nums[i]` → moves left
* Python’s `% n` automatically wraps indices into `[0, n-1]`

Special case:

* If `nums[i] == 0`, the result is simply `0`

---

## **Algorithm**

1. Let `n` be the length of `nums`
2. Initialize result array `res` with size `n`
3. For each index `i`:

   * If `nums[i] == 0`, set `res[i] = 0`
   * Otherwise, compute `(i + nums[i]) % n` and copy that value
4. Return `res`

---

## **Example**

### Example 1

```
Input: nums = [3, -2, 1, 1]
```

Step-by-step:

```
Index 0: 0 + 3 → index 3 → value 1
Index 1: 1 - 2 → index 3 → value 1
Index 2: 2 + 1 → index 3 → value 1
Index 3: 3 + 1 → index 0 → value 3
```

```
Output: [1, 1, 1, 3]
```

---

### Example 2

```
Input: nums = [-1, 4, -1]
```

```
Index 0: 0 - 1 → index 2 → -1
Index 1: 1 + 4 → index 2 → -1
Index 2: 2 - 1 → index 1 → 4
```

```
Output: [-1, -1, 4]
```

---

## **Complexity Analysis**

| Aspect      | Complexity |
| ----------- | ---------- |
| Time        | **O(n)**   |
| Extra Space | **O(n)**   |

---

## **Common Mistakes**

* ❌ Forgetting the array is circular
* ❌ Manually looping step-by-step instead of using modulo
* ❌ Not handling negative indices properly
* ❌ Overcomplicating with extra data structures

---

## **One-Line Interview Summary**

> “For each index, move `nums[i]` steps and use modulo to wrap around the circular array.”
