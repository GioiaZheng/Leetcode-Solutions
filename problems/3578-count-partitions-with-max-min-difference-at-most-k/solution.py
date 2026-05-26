from collections import deque
from typing import List

MOD = 10**9 + 7

class Solution:
    def countPartitions(self, nums: List[int], k: int) -> int:
        n = len(nums)
        
        dp = [0] * (n + 1)
        pref = [0] * (n + 2)

        dp[0] = 1
        pref[1] = 1

        maxD = deque()
        minD = deque()

        l = 0

        for r in range(n):
            # maintain decreasing max deque
            while maxD and nums[maxD[-1]] <= nums[r]:
                maxD.pop()
            maxD.append(r)

            # maintain increasing min deque
            while minD and nums[minD[-1]] >= nums[r]:
                minD.pop()
            minD.append(r)

            # shrink window to satisfy condition
            while nums[maxD[0]] - nums[minD[0]] > k:
                if maxD[0] == l:
                    maxD.popleft()
                if minD[0] == l:
                    minD.popleft()
                l += 1

            # dp transition using prefix sums:
            # dp[r+1] = sum(dp[l .. r])
            dp[r + 1] = (pref[r + 1] - pref[l]) % MOD

            # update prefix sum
            pref[r + 2] = (pref[r + 1] + dp[r + 1]) % MOD

        return dp[n]
