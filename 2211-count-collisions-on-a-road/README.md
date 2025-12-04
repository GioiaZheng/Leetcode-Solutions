# 2211. Count Collisions on a Road

**Difficulty:** Medium  
**Topics:** Simulation, String  
**Link:** https://leetcode.com/problems/count-collisions-on-a-road/

---

##  Problem Summary

Cars move on an infinite road.  
Each car goes Left (`L`), Right (`R`), or stays (`S`).  
When collisions happen:

- `R` + `L` → 2 collisions (both stop)
- `R` + `S` → 1 collision (R stops)
- `L` + `S` → 1 collision (L stops)

After colliding, cars stay in place forever.

Return the **total number of collisions**.

---

##  Key Insight

###  Cars that never collide:
- Leading `L`s (moving left forever)
- Trailing `R`s (moving right forever)

These must be removed from the simulation.

---

###  After removing them:
All remaining `R` or `L` inside the middle region **will collide** and become `S`.

So the number of collisions is simply:

```

count of non-'S' characters
in the trimmed middle segment

````

This gives an **O(n)** optimal solution.

---

##  Complexity

```
Time:  O(n)
Space: O(1)
```

---

##  Example

```
Input:  "RLRSLL"
Trimmed: "RLRSLL"
Non-'S': 5

Output: 5
