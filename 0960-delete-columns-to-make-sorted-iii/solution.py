from typing import List

class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        n = len(strs)
        m = len(strs[0])

        # dp[j]: length of the longest valid column subsequence ending at column j
        dp = [1] * m

        for j in range(m):
            for i in range(j):
                # Check if column i can come before column j
                valid = True
                for r in range(n):
                    if strs[r][i] > strs[r][j]:
                        valid = False
                        break

                if valid:
                    dp[j] = max(dp[j], dp[i] + 1)

        # Maximum columns we can keep
        max_keep = max(dp)

        # Minimum deletions = total columns - kept columns
        return m - max_keep
