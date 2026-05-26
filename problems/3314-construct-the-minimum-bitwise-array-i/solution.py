from typing import List

class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        res = []

        for n in nums:
            # even number (only possible prime is 2)
            if n % 2 == 0:
                res.append(-1)
                continue

            pos = 0
            # find the lowest zero bit
            while (n >> pos) & 1:
                pos += 1

            res.append(n - (1 << (pos - 1)))

        return res
