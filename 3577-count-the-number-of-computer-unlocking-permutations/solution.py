from typing import List
MOD = 10**9 + 7

class Solution:
    def countPermutations(self, complexity: List[int]) -> int:
        n = len(complexity)

        # compute DP:
        # dp[i] = number of ways if exactly i nodes are unlocked
        dp = [0] * (n+1)
        dp[1] = 1  # only {0}

        # active = nodes with index < i and complexity < complexity[i]
        active = 0

        # multiset sorted by complexity
        import bisect
        sortedc = []

        # insert complexity of index 0
        sortedc.append(complexity[0])

        for i in range(1, n):
            # count how many unlocked nodes can unlock current node
            # i.e. complexity[j] < complexity[i]
            cnt = bisect.bisect_left(sortedc, complexity[i])
            if cnt == 0:
                return 0  # no one can unlock i

            # insert and update
            bisect.insort(sortedc, complexity[i])

        # If all nodes pass feasibility → answer = factorial(n-1)
        # because only restriction is: 0 must be first
        # after that all remaining nodes are free to permute
        # but each must satisfy at least one unlock condition,
        # which is ensured by above check

        # factorial(n-1)
        ans = 1
        for i in range(1, n):
            ans = ans * i % MOD
        return ans
