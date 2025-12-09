# **LeetCode 2 – Add Two Numbers**

**Difficulty:** Medium  
**Tags:** Linked List, Math  
**Link:** [https://leetcode.com/problems/add-two-numbers/](https://leetcode.com/problems/add-two-numbers/)

---

## **Problem Summary**

You are given two non-empty linked lists representing two non-negative integers.
The digits are stored in **reverse order**, and each node contains a single digit.

The task is to return their **sum**, also represented as a linked list in reverse order.

No number includes leading zeros except 0 itself.

---

## **Key Insight**

* We process the lists **digit by digit**, simulating elementary school addition.
* Carry must be propagated across digits.
* Linked lists may have **different lengths**.
* If a carry remains after the last digit, we append a new node.

Thus, the core logic is:

$$
\text{digit} = (v_1 + v_2 + \text{carry}) \mod 10
$$

$$
\text{carry} = \left\lfloor \frac{v_1 + v_2 + \text{carry}}{10} \right\rfloor
$$

---

## **Approach**

1. Create a dummy head to simplify pointer handling.
2. Loop while:

   * `l1` exists
   * `l2` exists
   * or carry exists
3. Extract values (use `0` if a list is shorter).
4. Compute sum and update carry.
5. Append a new node with the digit.
6. Move forward in both lists.

---

## **Example**

### Example 1

```
l1 = [2,4,3]
l2 = [5,6,4]
```

342 + 465 = **807**

Reversed result → `[7,0,8]`

---

### Example 2

```
l1 = [0]
l2 = [0]
Output: [0]
```

---

### Example 3

```
l1 = [9,9,9,9,9,9,9]
l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]
```

---

## **Why This Works**

* Direct simulation of addition ensures correctness.
* Dummy node simplifies result handling.
* Carry ensures multi-digit sums work correctly.
* Works efficiently even for the longest allowed lists.

---

## **Complexity**

| Aspect | Complexity                     |
| ------ | ------------------------------ |
| Time   | **O(max(n, m))**               |
| Space  | **O(max(n, m))** (result list) |

---

## **What I Learned**

* How to simulate multi-digit addition using linked lists.
* Handling different list lengths carefully.
* Using a dummy node to simplify pointer handling.
* How to manage carry propagation across nodes.
