# **LeetCode 3606 – Coupon Code Validator**

**Difficulty:** Easy  
**Tags:** String Validation, Sorting, Simulation  
**Link:** [https://leetcode.com/problems/coupon-code-validator/](https://leetcode.com/problems/coupon-code-validator/)

---

## **Problem Summary**

You are given three arrays of equal length `n`, describing `n` coupons:

* `code[i]`: a string representing the coupon identifier
* `businessLine[i]`: a string indicating the business category
* `isActive[i]`: a boolean indicating whether the coupon is currently active

A coupon is considered **valid** if **all** of the following conditions hold:

* `code[i]` is **non-empty**
* `code[i]` contains **only**:

  * letters (`a–z`, `A–Z`)
  * digits (`0–9`)
  * underscore (`_`)
* `businessLine[i]` is one of:

  * `"electronics"`
  * `"grocery"`
  * `"pharmacy"`
  * `"restaurant"`
* `isActive[i]` is `true`

Your task is to return the list of **valid coupon codes**, sorted by:

1. Business line priority

   ```
   electronics → grocery → pharmacy → restaurant
   ```
2. Lexicographical order of the code within the same business line

---

## **Key Insight**

This problem is a combination of:

1. **String validation**
2. **Filtering based on multiple constraints**
3. **Custom sorting rules**

The most subtle part is code validation:

* Underscores (`_`) are allowed
* A code like `"_"` is **valid**
* Using `isalnum()` alone is insufficient and will incorrectly reject valid cases

Given the small constraints, a **direct simulation and sorting approach** is both safe and clear.

---

## **Approach**

### 1. Validation Rules

For each coupon, check in order:

1. The coupon is active
2. The code is non-empty
3. Every character in the code is:

   * alphanumeric **or**
   * underscore (`_`)
4. The business line is one of the allowed categories

Only coupons passing all checks are kept.

---

### 2. Sorting Strategy

To enforce the required order:

* Assign each business line a numeric priority
* Store valid coupons as `(priority, code)`
* Sort the list using Python’s default tuple ordering

This guarantees:

* Correct business line ordering
* Lexicographical sorting within each category

---

## **Example**

**Input**

```
code = ["SAVE20", "", "PHARMA5", "SAVE@20"]
businessLine = ["restaurant", "grocery", "pharmacy", "restaurant"]
isActive = [true, true, true, true]
```

**Explanation**

* `"SAVE20"` → valid
* `""` → invalid (empty code)
* `"PHARMA5"` → valid
* `"SAVE@20"` → invalid (contains `@`)

Sorted by business line and code:

```
["PHARMA5", "SAVE20"]
```

---

## **Why This Works**

The solution works because:

* Validation rules are applied **independently and explicitly**
* Character-level checking avoids hidden edge cases like `"_"`
* Business line priorities convert complex ordering into simple numeric sorting
* The approach mirrors real-world input validation pipelines

By separating **filtering** from **ordering**, the logic remains easy to reason about and debug.

---

## **Complexity**

* **Time Complexity:** `O(n log n)`

  * `O(n)` for validation
  * `O(n log n)` for sorting
* **Space Complexity:** `O(n)`

  * to store valid coupons

Both are well within the given constraints.

---

## **What I Learned**

* Why `isalnum()` is not sufficient when underscores are allowed
* How small edge cases (like `"_"`) can cause late test failures
* The value of assigning numeric priorities for custom sorting rules
* How to structure validation problems to be both readable and robust
