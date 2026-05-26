from typing import List

class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        # Sort happiness in descending order
        happiness.sort(reverse=True)

        total = 0

        # Pick k children greedily
        for i in range(k):
            # Effective happiness decreases by i
            gain = happiness[i] - i
            if gain <= 0:
                break
            total += gain

        return total
