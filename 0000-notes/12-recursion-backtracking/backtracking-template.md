# Backtracking Template  

This note is written for learners who feel:

- “I can’t tell permutation, combination, subset problems apart”
- “My recursion works for small cases but fails later”
- “I forget when and why to undo changes”

If this sounds familiar, this page will clarify everything.

---

## 1. What backtracking really is

Backtracking is simply:

> **Recursion that explores all possible choices.**

More precisely:
- try a choice
- go deeper
- undo the choice
- try the next one

There is no new algorithm here.
Just recursion used systematically.

---

## 2. The universal backtracking pattern

Almost every backtracking solution follows this skeleton:

```python
def backtrack(path, choices):
    if path is complete:
        record(path)
        return

    for choice in choices:
        make choice
        backtrack(updated path, updated choices)
        undo choice
````

If you understand this, you understand backtracking.

---

## 3. The three steps (MEMORIZE THIS)

Every backtracking step has **exactly three actions**:

1. **Choose**
2. **Explore**
3. **Un-choose (undo)**

Missing step 3 is the #1 bug source.

---

## 4. What is “path”?

`path` represents:

* the current partial solution
* the decisions made so far

Examples:

* permutation → chosen numbers
* subset → included elements
* string construction → built prefix

---

## 5. What is “choices”?

`choices` represents:

* what you can still choose from
* remaining candidates

Examples:

* unused numbers
* remaining characters
* next indices

---

## 6. Base case: what does “complete” mean?

The base case depends on the problem:

* permutation → `len(path) == n`
* combination → reached target size
* subset → no more decisions
* path in grid → reached destination

Define this clearly before coding.

---

## 7. Example: generating all subsets

Problem idea:

> Given nums, generate all subsets.

Backtracking solution:

```python
res = []

def backtrack(start, path):
    res.append(path[:])
    for i in range(start, len(nums)):
        path.append(nums[i])
        backtrack(i + 1, path)
        path.pop()
```

Here:

* path = current subset
* start controls next choices
* pop() undoes the choice

---

## 8. Why undoing is necessary

Without undo:

* choices leak into other branches
* paths get polluted
* results become incorrect

Undo restores the state **exactly** as before the choice.

---

## 9. Controlling duplicates (IMPORTANT)

Common techniques:

* sort input first
* skip duplicates with index checks
* use visited array

Example rule:

```python
if i > start and nums[i] == nums[i-1]:
    continue
```

This is pattern recognition, not trick memorization.

---

## 10. Permutations vs combinations (core difference)

| Type        | Order matters? | Typical control |
| ----------- | -------------- | --------------- |
| Permutation | Yes            | visited[]       |
| Combination | No             | start index     |

Recognizing this avoids confusion.

---

## 11. Backtracking vs DFS

Backtracking **is DFS**.

The difference:

* DFS explores structure
* Backtracking explores **choices**

Same recursion mechanics, different goals.

---

## 12. Pruning (early stopping)

Pruning means:

> **Stopping a branch early when it cannot lead to a valid solution**

Example:

* sum exceeds target
* path already too long

Pruning is optional but powerful.

---

## 13. Common beginner mistakes

### Mistake 1: Forgetting to copy path

Always record `path[:]`, not `path`.

### Mistake 2: Undoing in wrong place

Undo must happen **after** recursive call.

### Mistake 3: Mixing up start / visited

This leads to duplicates or missing solutions.

---

## 14. How to recognize backtracking problems

Key phrases:

* “generate all”
* “list all possible”
* “find all combinations / permutations”
* “explore every way”

If output size is exponential → backtracking.

---

## 15. Beginner checklist

Before coding backtracking, ask:

* What is the path?
* What are the choices?
* When is a solution complete?
* Where do I undo state?

Answer these first.

---

## Final reminder

Backtracking is not hard.

It is:

> **organized trial and error**

Once you internalize the template,
many scary-looking problems collapse into the same structure.
