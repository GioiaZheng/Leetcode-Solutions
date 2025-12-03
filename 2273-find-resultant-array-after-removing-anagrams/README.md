# 2273. Find Resultant Array After Removing Anagrams

**Difficulty:** Easy  
**Topics:** Array, Hashing, String  
**Link:** https://leetcode.com/problems/find-resultant-array-after-removing-anagrams/

---

##  Problem Description

You are given a 0-indexed string array `words`, where each `words[i]` consists of lowercase English letters.

In one operation, select any index `i` such that:

- `0 < i < words.length`
- `words[i]` and `words[i - 1]` are anagrams

Then delete `words[i]`.

Keep performing this operation until no more indices satisfy the condition.

It can be shown that choosing indices in any order yields the same final array.

Return the resulting array.

An **anagram** is a word or phrase formed by rearranging the letters of another word.

---

##  Examples

### Example 1

```

Input: words = ["abba","baba","bbaa","cd","cd"]
Output: ["abba","cd"]

```

Explanation:

- "baba" and "bbaa" are anagrams of "abba", so they are removed.
- The second "cd" is an anagram of the previous "cd", so it is removed.

---

### Example 2

```

Input: words = ["a","b","c","d","e"]
Output: ["a","b","c","d","e"]

```

No adjacent words are anagrams → nothing is removed.

---

##  Key Insight

We only care about **adjacent** anagrams.

If `words[i]` is an anagram of the last kept word → remove it.

Therefore, we can simply build the answer using one pass:

- Always keep the first word.
- For each word:
  - If it's NOT an anagram of the previous kept word → append it.
  - Otherwise → skip it.

Sorting each word is enough since each word length ≤ 10.

---

##  Algorithm

1. Initialize result array with the first word.
2. Loop from index 1 to end:
   - Compare sorted form with sorted last kept word.
3. Append only if not anagrams.
4. Return result.

---

##  Complexity

```

Time:  O(n * k log k)   (n = number of words, k = max length of word ≤ 10)
Space: O(n)

```

Efficient for all constraints.

---

##  Summary

- Removing adjacent anagrams is equivalent to keeping words where  
  `sorted(words[i]) != sorted(last_kept_word)`
- A single pass yields the final answer.
