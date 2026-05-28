# LeetCode 10 – Regular Expression Matching
**Difficulty:** Hard 
**Tags:** String, Dynamic Programming 
**Link:** [https://leetcode.com/problems/regular-expression-matching/](https://leetcode.com/problems/regular-expression-matching/)

---

## Problem Summary
You are given a string `s` and a pattern `p`.

Implement regular expression matching with support for:

* `.` → matches **any single character**
* `*` → matches **zero or more of the preceding element**

The matching must cover the **entire string** (not partial matching).

---

## Key Insight
* This problem cannot be solved greedily.
* The correct approach is **Dynamic Programming**.
* We define a DP table where each state represents whether a prefix of `s`
 matches a prefix of `p`.

The main challenge is handling `*`, which can represent:

* **zero occurrences**
* **one or more occurrences** of the preceding character

---

## Approach
Define:

```text
dp[i][j] = whether s[0:i] matches p[0:j]
```

Steps:

1. Initialize `dp[0][0] = True` (empty string matches empty pattern).
2. Pre-fill cases where patterns like `"a*"`, `"a*b*"` match an empty string.
3. Fill the DP table:

 * If current characters match (`.` or same letter):

 * inherit from `dp[i-1][j-1]`
 * If current pattern character is `'*'`:

 * Case 1: treat `*` as **zero occurrences**
 * Case 2: treat `*` as **one or more occurrences**
4. The final answer is `dp[len(s)][len(p)]`.

---

## Example
### Example 1

```
Input: s = "aa", p = "a"
Output: false
```

---

### Example 2

```
Input: s = "aa", p = "a*"
Output: true
```

---

### Example 3

```
Input: s = "ab", p = ".*"
Output: true
```

---

## Why This Works
* Each DP state represents a **complete and unambiguous subproblem**.
* `*` is handled by separating **zero occurrences** and **multiple occurrences**.
* The solution checks **all valid matching paths**, guaranteeing correctness.
* The DP table size is small due to tight constraints.

---

## Complexity
| Aspect | Complexity |
| ------ | ------------ |
| Time | **O(m × n)** |
| Space | **O(m × n)** |

Where:

* `m = len(s)`
* `n = len(p)`

---

## What I Learned
* How to model regex matching as a DP problem.
* Why `*` must always refer to the **previous character**.
* How to systematically cover all matching cases without backtracking.
* A classic interview-level string DP pattern.

---

### Notes

This is one of the most important **string dynamic programming** problems.
Understanding this solution makes it much easier to solve:

* Wildcard Matching
* Edit Distance
* Pattern Matching variants

<!--
Sections below are the optional "AI card" extension. The problem
carries `"ai_card_status": "reviewed"` in metadata.json. See
CONTRIBUTING.md section "Optional Problem README Sections (AI Card)".
-->

---

## Brute-force baseline

Recursive matching without memoisation: at each step, look at `s[i]` and `p[j]`, branch on whether `p[j+1] == '*'`, and explore both "consume zero" and "consume one" alternatives for the `*` case.

- **Time:** Exponential in the worst case --- patterns like `"a*a*a*a*..."` against a long `s` produce overlapping subproblems that get re-explored repeatedly.
- **Space:** `O(m + n)` for the recursion stack.

Memoising the recursion (top-down DP) and the bottom-up table approach above both collapse this to `O(m \cdot n)` time and space. The bottom-up version is the recommended interview answer because it makes the state transitions explicit.

---

## Common mistakes

- Treating `*` as "match exactly one or more" (regex-engine `+` semantics) instead of "match zero or more of the preceding element". The zero-match branch is critical --- without it, patterns like `"a*"` cannot match `""`.
- Pre-filling only `dp[0][0] = True` and forgetting the `"a*b*c*"` empty-prefix case. For an empty `s`, `dp[0][j]` should be `True` whenever every pair `p[j-1] == '*'` allows skipping `p[j-2]`; this requires a forward sweep over the pattern.
- Indexing `p[j-1]` when checking the `*` semantics. The pattern uses 1-based DP indices but 0-based string indices; conflating them gives off-by-one errors. The canonical form is: when filling `dp[i][j]`, the relevant string char is `s[i-1]` and the pattern char is `p[j-1]`.
- For the `*` case, looking at `p[j-1]` for the preceding character. The `*` itself sits at `p[j-1]`; the character it modifies sits at `p[j-2]`. The "zero occurrence" branch reads `dp[i][j-2]`, NOT `dp[i][j-1]`.
- Greedy left-to-right `*` expansion. There is no correct greedy strategy for this problem --- the same `*` may need to match `0`, `1`, or more characters depending on what comes after; only DP (or backtracking with memo) covers every case.

---

## Failure cases

1. **`s = "aa", p = "a"`** --- expected `false`. Plain literal pattern shorter than the string; tests that the matcher does not return `true` on partial match. A buggy implementation that accepts when the pattern is exhausted but the string is not silently passes other inputs.
2. **`s = "aab", p = "c*a*b"`** --- expected `true`. `c*` matches zero occurrences (skips entirely), `a*` matches two occurrences, `b` matches the trailing `b`. Tests the multi-`*` chain and the zero-match branch firing on `c*`.
3. **`s = "mississippi", p = "mis*is*p*."`** --- expected `false`. Looks plausible at a glance (each `s*` could match) but the final `.` has nothing left to match because `p*` consumes too aggressively if treated greedily; the DP correctly explores both zero-match and multi-match branches and concludes no valid alignment exists.
4. **`s = "", p = "a*b*c*"`** --- expected `true`. Empty string against `"<char>*"+` pattern. Catches implementations whose pre-fill loop forgets that an entire chain of `<char>*` groups can collectively skip themselves down to the empty string.

---

## Interview follow-ups

- *"Compare with LeetCode 44 (Wildcard Matching)."* --- LC 44 has `*` mean "match any sequence" (regex `.*` semantics) and `?` mean "match any single character" (LC 10's `.`). The DP shape is similar but the `*` transition is different: in LC 44, `dp[i][j] |= dp[i-1][j]` for the multi-match branch, with no preceding-character anchor.
- *"Top-down memoisation instead of bottom-up DP."* --- recursion + `@lru_cache` on `(i, j)` matches the same recurrence. Cleaner to write under time pressure; same complexity bound.
- *"Stream the input (one char at a time)."* --- requires converting the pattern to an NFA / DFA. Build the NFA from the pattern once (Thompson's construction), then walk the active states as each character arrives. `O(n)` build + `O(|states| \cdot m)` matching.
- *"What if `*` is replaced by `+` (one-or-more)?"* --- the DP transition for the multi-match branch unchanged, but the zero-match branch becomes `dp[i][j] = dp[i][j-2] AND p[j-2] matched at least once` --- need to remove `dp[i][j-2]` from the OR. Easier: rewrite `p = "a+"` as `p = "aa*"` and reuse the LC 10 matcher.

---

## Bilingual summary

**English.** Bottom-up DP over `dp[i][j] = whether s[0..i) matches p[0..j)`. The recurrence has two branches: if `p[j-1] != '*'`, copy `dp[i-1][j-1]` when `s[i-1]` matches `p[j-1]` (with `.` wildcard). If `p[j-1] == '*'`, OR together the zero-match branch `dp[i][j-2]` and the multi-match branch `dp[i-1][j]` when `s[i-1]` matches `p[j-2]`. Pre-fill `dp[0][j]` for empty-string-against-`<char>*`-chain patterns. `O(m \cdot n)` time and space.

**中文。** 自底向上 DP，状态 `dp[i][j] = s[0..i)` 是否匹配 `p[0..j)`。转移有两种：若 `p[j-1] != '*'`，当 `s[i-1]` 与 `p[j-1]` 匹配时（`.` 是通配符）继承 `dp[i-1][j-1]`；若 `p[j-1] == '*'`，把"零次匹配"分支 `dp[i][j-2]` 与"多次匹配"分支 `dp[i-1][j]`（当 `s[i-1]` 匹配 `p[j-2]` 时）做或运算。还需在 `i = 0` 行预填 `<char>*` 链对空串的情况。时间和空间均 `O(m \cdot n)`。
