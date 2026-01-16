# **LeetCode 1590 – Make Sum Divisible by P**

**Difficulty:** Medium  
**Tags:** Prefix Sum, Hash Map, Modular Arithmetic  
**Link:** https://leetcode.com/problems/make-sum-divisible-by-p/

---

## **Problem Summary**

You are given an array of **positive integers** `nums` and an integer `p`.

You may remove **one contiguous subarray** (possibly empty, but **not the entire array**) such that the **sum of the remaining elements is divisible by `p`**.

Return the **minimum length** of the subarray to remove.  
If it is impossible, return **`-1`**.

---

## **Key Insight**

Let:

```

total_sum = sum(nums)

```

If:
```

total_sum % p == 0

```
The sum is already divisible → **answer = 0**

Otherwise, let:
```

need = total_sum % p

```

We must remove a subarray whose **sum ≡ need (mod p)**, so that:

```

(total_sum - subarray_sum) % p == 0

```

---

## **Reformulation**

This becomes:

> Find the **shortest subarray** whose sum modulo `p` equals `need`.

---

## **Prefix Sum + Modulo Trick**

Define prefix sum modulo:
```

prefix[i] = (nums[0] + ... + nums[i]) % p

```

For a subarray `(j+1 ... i)`:
```

subarray_sum % p = (prefix[i] - prefix[j] + p) % p

```

We want:
```

(prefix[i] - prefix[j]) % p == need

```

Rearranging:
```

prefix[j] == (prefix[i] - need + p) % p

```

---

## **Approach**

### Step 1: Compute Total Sum
- If `total_sum % p == 0`, return `0`

---

### Step 2: Prefix Modulo + Hash Map

- Use a dictionary to store the **latest index** where a prefix modulo appears
- Initialize:
```

seen = {0: -1}

````
- For each index `i`:
- Compute `prefix = (prefix + nums[i]) % p`
- Compute the target modulo:
  ```
  target = (prefix - need + p) % p
  ```
- If `target` exists in `seen`, update the answer
- Update `seen[prefix] = i`

---

### Step 3: Final Check

- If the shortest length equals `len(nums)`, return `-1`
- Otherwise, return the shortest length

---

## **Example Walkthrough**

### Example 1
```
nums = [3,1,4,2], p = 6
total_sum = 10 → need = 4
```

We look for the shortest subarray whose sum ≡ 4 (mod 6).

Removing `[4]` works → answer = `1`.

---

### Example 2
```

nums = [6,3,5,2], p = 9
total_sum = 16 → need = 7

```

Removing `[5,2]` gives remaining sum = 9 → answer = `2`.

---

### Example 3
```

nums = [1,2,3], p = 3
total_sum = 6 → divisible already

````

Answer = `0`.

---

## **Why This Works**

* Prefix sums allow us to express any subarray sum efficiently
* Modular arithmetic turns the problem into a lookup
* Hash map ensures **O(1)** average lookup time
* Only one pass through the array is required

---

## **Complexity Analysis**

Let `n = len(nums)`.

| Aspect | Complexity                     |
| ------ | ------------------------------ |
| Time   | **O(n)**                       |
| Space  | **O(p)** (at most `n` entries) |

---

## **What I Learned**

* Removing a subarray can be reframed as finding a modulo condition
* Prefix sum modulo is a powerful pattern for divisibility problems
* Hash maps help track optimal subarray boundaries efficiently
* Careful handling of modulo arithmetic avoids negative values

---

## **Related Problems**

* 560. Subarray Sum Equals K
* 523. Continuous Subarray Sum
* 974. Subarray Sums Divisible by K

---

## **One-Line Interview Summary**

> “Use prefix sums modulo `p` and a hash map to find the shortest subarray whose removal makes the total sum divisible by `p`.”
