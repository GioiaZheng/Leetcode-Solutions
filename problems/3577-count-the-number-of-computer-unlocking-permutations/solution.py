import bisect
from typing import List

MOD = 10**9 + 7

class Solution:
    def countPermutations(self, complexity: List[int]) -> int:
        n = len(complexity)

        # Maintain a sorted list of unlocked complexities, seeded with node 0.
        sortedc = [complexity[0]]

        for i in range(1, n):
            # Node i can be unlocked iff at least one already-unlocked node has
            # smaller complexity.
            cnt = bisect.bisect_left(sortedc, complexity[i])
            if cnt == 0:
                return 0

            bisect.insort(sortedc, complexity[i])

        # All nodes pass feasibility → node 0 must be first, the remaining n-1
        # can be ordered arbitrarily, giving (n-1)! permutations modulo MOD.
        ans = 1
        for i in range(1, n):
            ans = ans * i % MOD
        return ans
