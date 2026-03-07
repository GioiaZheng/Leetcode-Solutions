# **LeetCode 3779 – Minimum Number of Operations to Have Distinct Elements**

**Difficulty:** Medium  
**Tags:** Hash Table, Greedy, Simulation  
**Link:** [https://leetcode.com/problems/minimum-number-of-operations-to-have-distinct-elements/](https://leetcode.com/problems/minimum-number-of-operations-to-have-distinct-elements/)

---

## **Problem Summary**

You are given an integer array `nums`.

In one operation, you remove the **first three elements** of the current array.
If fewer than three elements remain, **all remaining elements are removed**.

You repeat this operation until one of the following happens:

* The array becomes **empty**, or
* The array contains **only distinct elements** (no duplicates)

Return the **minimum number of operations** required.

---

## **Key Insight**

The operation **always removes the first three elements**, so the array is effectively processed **from left to right in chunks of size 3**.

Instead of actually rebuilding the array after every operation, we can:

* Track the **frequency of each number**
* Track how many values currently appear **more than once**
* Simulate removing elements from the front while updating frequencies

The moment **no duplicates remain**, we can stop immediately.

---

## **Why This Approach Works**

Let:

* `freq[x]` = how many times number `x` appears
* `duplicates` = how many values currently have `freq[x] > 1`

When removing elements:

* If a value’s frequency changes from **2 → 1**, one duplicate disappears
* If it changes from **3 → 2**, it **still remains a duplicate**

So we only reduce `duplicates` when a count drops **from 2 to 1**.

Because we only remove elements from the **front**, we can simply maintain an index pointer rather than modifying the array.

---

## **Algorithm**

1. Count frequencies using `Counter`
2. Compute how many values currently have `frequency > 1`
3. Maintain:

   * `operations` → number of operations performed
   * `index` → current position in the array
4. Repeat:

   * If `duplicates == 0`, stop
   * Remove up to **3 elements**
   * Update frequencies and duplicate count
5. Increment `operations` each round
6. Return the result

---

## **Example**

### Example 1

```
Input: nums = [3,8,3,6,5,8]
```

Initial frequencies:

```
3 → 2
8 → 2
6 → 1
5 → 1
```

Duplicates: `3, 8`

Operation 1:

```
Remove first three elements → [3,8,3]

Remaining array → [6,5,8]
```

Frequencies now:

```
6 → 1
5 → 1
8 → 1
```

All elements are distinct.

Answer:

```
1
```

---

### Example 2

```
Input: nums = [2,2]
```

Operation 1 removes everything:

```
[]
```

Array is empty → stop.

Answer:

```
1
```

---

### Example 3

```
Input: nums = [4,3,5,1,2]
```

All values are already distinct.

No operations needed.

Answer:

```
0
```

---

## **Complexity Analysis**

| Aspect             | Complexity |
| ------------------ | ---------- |
| Frequency counting | **O(n)**   |
| Simulation         | **O(n)**   |
| Total Time         | **O(n)**   |
| Extra Space        | **O(n)**   |

`n ≤ 10^5`, so a single linear scan is efficient.

---

## **Common Mistakes**

* Rebuilding the array after each operation (unnecessary and slow)
* Forgetting that **fewer than 3 elements means removing all remaining**
* Decreasing duplicate count incorrectly when frequency drops from `3 → 2`
* Continuing operations even after duplicates are gone

The key is to **track frequencies dynamically while moving a pointer forward**.

---

## **One-Line Interview Summary**

> “Track frequencies with a counter, simulate removing elements from the front in groups of three, and stop once no value appears more than once.”
