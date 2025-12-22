# Dynamic Programming on Strings  

This note is written for beginners who feel:

- “String DP problems look impossible”
- “I don’t know when to use 1D or 2D DP”
- “Substring and subsequence always confuse me”

If this sounds familiar, this note is for you.

---

## 1. Why string DP feels harder than array DP

Array DP:
- usually linear
- one index
- one direction

String DP:
- often compares **two positions**
- may need **two dimensions**
- involves **matching characters**

So the complexity feels higher — but the idea is the same.

---

## 2. The most important distinction (MUST KNOW)

Before anything else, ask:

> **Is this problem about a substring or a subsequence?**

### Substring
- characters must be **contiguous**
- indices move together
- usually involves ranges `[l, r]`

### Subsequence
- characters can be skipped
- order matters, adjacency does not
- usually involves choices (take / skip)

This single distinction decides your DP structure.

---

## 3. Common DP states for string problems

### Pattern 1 — Substring DP (range-based)

```text
dp[l][r] = whether substring s[l:r] satisfies a condition
````

Used for:

* palindromes
* valid substrings
* range-based checks

Key idea:

* expand or shrink a range

---

### Pattern 2 — Subsequence DP (prefix-based)

```text
dp[i][j] = best result using s1[:i] and s2[:j]
```

Used for:

* longest common subsequence
* edit distance
* string transformation

Key idea:

* compare prefixes
* choices affect future

---

## 4. Substring DP: how to think

Substring problems usually ask:

> “What is true about the substring between l and r?”

Example:

* is it a palindrome?
* what is its length?

Typical transition:

```text
dp[l][r] depends on dp[l+1][r-1]
```

Because you shrink from both ends.

---

## 5. Subsequence DP: how to think

Subsequence problems usually ask:

> “What is the best result using the first i characters?”

Typical transition:

* if characters match → take both
* if not → skip one side

This creates branching choices → DP is necessary.

---

## 6. Example intuition: Longest Palindromic Substring

State:

```text
dp[l][r] = whether s[l:r] is a palindrome
```

Transition:

* s[l] == s[r]
* and inner substring is palindrome

Base cases:

* single character
* two equal characters

This is DP on **ranges**, not positions.

---

## 7. Example intuition: Longest Common Subsequence

State:

```text
dp[i][j] = length of LCS of s1[:i] and s2[:j]
```

Transition:

* if s1[i-1] == s2[j-1] → 1 + dp[i-1][j-1]
* else → max(dp[i-1][j], dp[i][j-1])

This is DP on **choices**.

---

## 8. Table-filling order matters

String DP often requires:

* filling by increasing length
* or increasing i, j

You must ensure:

> the states you depend on are already computed

Wrong order = wrong answers.

---

## 9. Space optimization (advanced, optional)

Many string DP problems:

* can be optimized from 2D to 1D
* but clarity matters more than memory

Always write the full DP table first.

---

## 10. Common beginner mistakes

### Mistake 1: Mixing substring and subsequence logic

This breaks transitions.

### Mistake 2: Wrong index interpretation

Be clear about inclusive vs exclusive ranges.

### Mistake 3: Forgetting base cases

Especially for short strings.

---

## 11. Beginner checklist

Before coding string DP, confirm:

* Is this substring or subsequence?
* What does dp[i][j] represent?
* Which smaller states does it depend on?
* In what order should I fill the table?

If yes → you are ready.

---

## 12. Related problems in this repository

Practice string DP with:

* `0005-longest-palindromic-substring`
* `0003-longest-substring-without-repeating-characters` (contrast)
* classic LCS / edit distance style problems
* string transformation problems

---

## Final reminder

String DP is not harder than array DP.

It just:

> **tracks relationships between characters**

Once you separate substring and subsequence,
string DP becomes structured and predictable.
