# **LeetCode 2211 – Count Collisions on a Road**

**Difficulty:** Medium
**Tags:** String, Simulation
**Link:** [https://leetcode.com/problems/count-collisions-on-a-road/](https://leetcode.com/problems/count-collisions-on-a-road/)

---

## **Problem Summary**

You are given a string representing the directions of cars on a one-lane road.
Each character is one of:

* `'L'` → car moving left
* `'R'` → car moving right
* `'S'` → stationary car

When cars collide, they change state depending on the type of collision, and each collision adds to the total count.

The task is to compute the number of collisions that will occur until no further movement is possible.

---

## **Key Insight**

A collision happens **only** in the following cases:

1. A right-moving car `'R'` meets a stationary car `'S'`.
2. A right-moving car `'R'` meets a left-moving car `'L'`.
3. A left-moving car `'L'` meets a stationary car `'S'`.

Cars moving outward—`'L'` at the far left or `'R'` at the far right—will never collide, because they have no car ahead of them.

Therefore, the number of collisions depends only on the **internal segment** of the string, after removing:

* all leading `'L'`
* all trailing `'R'`

Within the remaining segment, every non-`'S'` car will eventually collide.

---

## **Approach**

1. Trim the string:

   * Remove all leading `'L'`.
   * Remove all trailing `'R'`.

2. In the resulting substring, count the characters that are:

   * `'L'` → will collide once
   * `'R'` → will collide once

3. The number of collisions equals the number of non-`'S'` characters in this trimmed portion.

This works because any movement in the interior eventually results in a collision.

---

## **Example**

**Input**

```
"RLRSLL"
```

**Explanation**

* The leading character `'R'` stays.
* The trailing `'L'` stays.
* All cars in between eventually collide.

Total collisions = 5.

**Output**

```
5
```

---

## **Why This Works**

Cars at the edges that move outward cannot participate in collisions, so they can be ignored.

For every car remaining inside the trimmed segment:

* A left-moving car will encounter a stationary or right-moving car.
* A right-moving car will encounter a stationary or left-moving car.

Thus, all non-stationary cars within the interior must collide exactly once.

---

## **Complexity**

* **Time:** `O(n)`
* **Space:** `O(1)`

---

## **What I Learned**

* How collision problems can be reduced by trimming non-interactive boundary elements.
* The importance of recognizing which states cannot change and ignoring them.
* How to convert a step-by-step simulation into a counting problem by observing invariants.
