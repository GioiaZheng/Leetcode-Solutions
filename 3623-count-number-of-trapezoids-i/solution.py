class Solution:
    def countTrapezoids(self, points: List[List[int]]) -> int:
        """
        Count horizontal trapezoids.
        A horizontal trapezoid is determined by choosing:
        - 2 points on one horizontal line (same y)
        - 2 points on another different horizontal line

        So for each y:
            pairs[y] = C(freq[y], 2)
        Then sum over all unordered pairs (y1, y2):
            pairs[y1] * pairs[y2]
        """

        MOD = 10**9 + 7

        from collections import defaultdict
        freq = defaultdict(int)

        # Count number of points on each horizontal line (same y)
        for x, y in points:
            freq[y] += 1

        # nC2 helper
        def comb2(x):
            return x * (x - 1) // 2

        # Compute combination values for each y with >=2 points
        pairs = []
        for y in freq:
            if freq[y] >= 2:
                pairs.append(comb2(freq[y]))

        # Compute sum_{i<j} pairs[i] * pairs[j] using prefix sum
        result = 0
        prefix_sum = 0

        for p in pairs:
            result = (result + p * prefix_sum) % MOD
            prefix_sum = (prefix_sum + p) % MOD

        return result
