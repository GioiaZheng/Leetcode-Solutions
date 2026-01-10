# **LeetCode 712 – Minimum ASCII Delete Sum for Two Strings**

**Difficulty:** Medium  
**Tags:** Dynamic Programming, String  
**Link:** https://leetcode.com/problems/minimum-ascii-delete-sum-for-two-strings/

---

## **Problem Summary**

You are given two strings `s1` and `s2`.

You may delete characters from either string.  
Each deletion costs the **ASCII value** of the deleted character.

Your task is to make the two strings **exactly equal** with the **minimum possible total ASCII deletion cost**.

Return that minimum cost.

---

## **Key Insight**

This problem is a **weighted version of the Longest Common Subsequence (LCS)** problem.

- In classic **LCS**, we maximize the length of the common subsequence.
- In this problem, we instead **minimize the ASCII cost of deletions** needed to make the strings equal.

Rather than directly deciding what to keep, we compute the **minimum deletion cost** required to align the two strings.

---

## **Approach**

We use **Dynamic Programming**.

### 🔹 State Definition

```

dp[i][j] = minimum ASCII delete sum to make
s1[i:] and s2[j:] equal

```

---

### 🔹 Base Cases

- If `i == len(s1)`:
  - We must delete all remaining characters in `s2[j:]`
- If `j == len(s2)`:
  - We must delete all remaining characters in `s1[i:]`

---

### 🔹 Transition

- If characters match:
```

s1[i] == s2[j]
dp[i][j] = dp[i+1][j+1]

```

- If characters differ:
```

dp[i][j] = min(
ord(s1[i]) + dp[i+1][j],   # delete s1[i]
ord(s2[j]) + dp[i][j+1]    # delete s2[j]
)

```

---

### 🔹 Final Answer

```

dp[0][0]

```

---

## **Examples**

### Example 1

```

Input:
s1 = "sea"
s2 = "eat"

Output:
231

```

Explanation:

- Delete `'s'` → ASCII 115
- Delete `'t'` → ASCII 116  
- Remaining string: `"ea"`

Total cost:

```

115 + 116 = 231

```

---

### Example 2

```

Input:
s1 = "delete"
s2 = "leet"

Output:
403

```

Explanation:

- Delete `"dee"` from `"delete"`
- Delete `"e"` from `"leet"`
- Final common string: `"let"`

Total minimum cost = **403**

---

## **Why This Works**

- Dynamic Programming ensures every subproblem is solved once.
- Each state represents the cheapest way to align suffixes.
- Choosing the minimum deletion cost at each mismatch guarantees a global optimum.
- This pattern is closely related to **Edit Distance** and **LCS** problems.

---

## **Complexity**

Let:

- `m = len(s1)`
- `n = len(s2)`

| Aspect | Complexity |
|------|------------|
| Time | **O(m × n)** |
| Space | **O(m × n)** |

---

## **What I Learned**

- How to convert LCS into a **cost-minimization DP problem**
- Handling weighted deletions instead of counting operations
- Recognizing shared structure between string DP problems
- Designing DP states that model suffix-based decisions

---

## **Related Problems**

- 1143. Longest Common Subsequence  
- 583. Delete Operation for Two Strings  
- 72. Edit Distance  

---

## **One-Line Interview Summary**

> “Use dynamic programming where `dp[i][j]` stores the minimum ASCII cost to make `s1[i:]` and `s2[j:]` equal, deleting the cheaper character when they differ.”
