from typing import List

class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        n, m = len(nums1), len(nums2)
        NEG_INF = -10**18

        # dp[j] will represent dp[i][j] for current i (rolling array)
        dp = [NEG_INF] * (m + 1)

        for i in range(n - 1, -1, -1):
            new_dp = [NEG_INF] * (m + 1)
            for j in range(m - 1, -1, -1):
                prod = nums1[i] * nums2[j]

                take = prod
                if dp[j + 1] > 0:
                    take += dp[j + 1]

                skip1 = dp[j]       # dp[i+1][j]
                skip2 = new_dp[j+1] # dp[i][j+1]

                new_dp[j] = max(take, skip1, skip2)

            dp = new_dp

        return dp[0]
