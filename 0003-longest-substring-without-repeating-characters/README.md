# **LeetCode 3 – Longest Substring Without Repeating Characters**

**Difficulty:** Medium  
**Tags:** Sliding Window, Hash Map, Two Pointers  
**Link:** [https://leetcode.com/problems/longest-substring-without-repeating-characters/](https://leetcode.com/problems/longest-substring-without-repeating-characters/)

---

## **Problem Summary**

Given a string `s`, the task is to determine the **length** of the longest substring that contains **no repeated characters**.

A substring must consist of **contiguous characters**, unlike a subsequence.

---

## **Key Insight**

A brute-force solution would check every possible substring, but this leads to `O(n²)` time and is far too slow for inputs as large as `50,000` characters.

The key observation is:

### A valid substring (no duplicates) can be represented by a **sliding window**.

As we move from left to right:

* Add characters to the window until a duplicate appears.
* When a duplicate is encountered, move the **left** pointer just past the previous occurrence.
* Maintain a dictionary mapping each character to its **most recent index**.
* Track the longest window encountered so far.

This ensures each character is processed at most twice (once by `right`, once by `left`), making the solution **O(n)**.

---

## **Approach**

1. Use a dictionary `last_seen` to record the most recent index of each character.
2. Initialize two pointers:

   * `left` = start of current window
   * `right` = current character being examined
3. For each character `s[right]`:

   * If the character is already in `last_seen` **and** its previous index is inside the window (`>= left`),
     then update:

     ```
     left = last_seen[s[right]] + 1
     ```
   * Update the character’s latest index:

     ```
     last_seen[s[right]] = right
     ```
   * Compute window size:

     ```
     right - left + 1
     ```
   * Update `max_len` accordingly.
4. Return `max_len`.

This maintains a valid window at all times and ensures linear performance.

---

## **Example**

**Input**

```
s = "pwwkew"
```

**Explanation**

Sliding window evolution:

* `"p"` → length 1
* `"pw"` → length 2
* Duplicate `"w"` encountered → move left past first `"w"`
* Window becomes `"w"`
* Then `"wk"` → `"wke"` → length 3

The longest valid substring is `"wke"` with length **3**.

**Output**

```
3
```

---

## **Why This Works**

* The sliding window ensures we never reconsider characters outside the active substring.
* The dictionary lets us jump the `left` pointer efficiently to avoid duplicates.
* Each pointer (`left`, `right`) moves only forward, giving a true **O(n)** algorithm.
* The approach carefully distinguishes between duplicates inside and outside the window, ensuring correctness.

---

## **Complexity**

* **Time:** `O(n)` — Each index visited at most twice
* **Space:** `O(k)` where `k` is the character set size (at most 128 for ASCII)

---

## **What I Learned**

* How sliding window algorithms convert seemingly quadratic problems into linear ones.
* The importance of tracking the **most recent index** of characters.
* Why moving `left` only forward (never backward) ensures linear time.
* How to maintain window validity with a single data structure (`last_seen`).
* How substring problems differ fundamentally from subsequence problems.
