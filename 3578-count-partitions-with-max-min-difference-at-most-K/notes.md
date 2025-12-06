# Notes — Count Partitions With Max-Min Difference at Most K

This problem combines several powerful techniques:

- Sliding Window
- Monotonic Queues
- Dynamic Programming
- Prefix Sums

Below is a clean breakdown of all ideas.

---

# 1. Sliding Window for Valid Segment

A segment `[l..r]` is valid if:

```

max(nums[l..r]) - min(nums[l..r]) <= k

```

As `r` moves right, the window might become invalid.  
We increase `l` until the condition becomes valid again.

Thus for each `r`, there exists a smallest valid `l`.

All positions from `l..r` produce valid segment endings.

---

# 2. Why Monotonic Queues?

In the sliding window, we need:

- The maximum quickly  
- The minimum quickly  

A monotonic deque supports:

- Push element in O(1)
- Pop element in O(1)
- Retrieve min/max in O(1)

Thus:

- `maxD`: decreasing → front is current max  
- `minD`: increasing → front is current min  

---

# 3. DP Definition

Let:

```

dp[i] = number of valid ways to partition nums[0..i-1]

```

Example:
- `dp[0] = 1` → empty prefix has 1 “initial state”

When we are at position `r` (ending index):

```

dp[r+1] = dp[l] + dp[l+1] + ... + dp[r]

```

Because all these starting points produce valid final segments.

---

# 4. Prefix Sum Trick

Direct summation is O(n). But we need O(1).

Define prefix:

```

pref[i] = dp[0] + dp[1] + ... + dp[i-1]

```

Then:

```

sum(dp[l..r]) = pref[r+1] - pref[l]

```

So:

```

dp[r+1] = pref[r+1] - pref[l]

```

---

# 5. Final Complexity

```

Time: O(n)
Space: O(n)

```

Monotonic queues guarantee the sliding window expands and shrinks each element once.

---

# 6. Summary of Flow

1. Expand r to the right  
2. Maintain max/min with monotonic queues  
3. Shrink l if max-min > k  
4. Compute dp using prefix sums  
5. Accumulate results  

This is one of the cleanest combinations of sliding window + DP in LeetCode.
