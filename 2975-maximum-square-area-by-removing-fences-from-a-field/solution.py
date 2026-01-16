from typing import List

class Solution:
    def maximizeSquareArea(self, m: int, n: int, hFences: List[int], vFences: List[int]) -> int:
        MOD = 10**9 + 7

        # Add boundary fences
        h = sorted([1] + hFences + [m])
        v = sorted([1] + vFences + [n])

        # Compute all horizontal gaps
        h_gaps = set()
        for i in range(len(h)):
            for j in range(i + 1, len(h)):
                h_gaps.add(h[j] - h[i])

        # Find maximum square side from vertical gaps
        max_side = -1
        for i in range(len(v)):
            for j in range(i + 1, len(v)):
                gap = v[j] - v[i]
                if gap in h_gaps:
                    max_side = max(max_side, gap)

        if max_side == -1:
            return -1

        return (max_side * max_side) % MOD
