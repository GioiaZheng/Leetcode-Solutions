from typing import List
MOD = 10**9 + 7

class Solution:
    def countPermutations(self, complexity: List[int]) -> int:
        n = len(complexity)

        # Keep placeholder DP state used by this implementation path.
        dp = [0] * (n+1)
        dp[1] = 1  # only {0}

        # `active` is kept for compatibility with the current structure.
        active = 0

        # Maintain a sorted list of unlocked complexities.
        import bisect
        sortedc = []

        # Seed with node 0 complexity.
        sortedc.append(complexity[0])

        for i in range(1, n):
            # Count unlocked nodes that can unlock node i: complexity[j] < complexity[i].
            cnt = bisect.bisect_left(sortedc, complexity[i])
            if cnt == 0:
                return 0  # no one can unlock i

            # Insert current complexity into the sorted structure.
            bisect.insort(sortedc, complexity[i])

        # If all nodes pass feasibility, valid permutations are factorial(n - 1):
        # node 0 must be first, and the remaining nodes can be ordered arbitrarily.

        # Compute factorial(n - 1) modulo MOD.
        ans = 1
        for i in range(1, n):
            ans = ans * i % MOD
        return ans
