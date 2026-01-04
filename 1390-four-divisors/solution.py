from typing import List
import math

class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        def sum_if_four_divisors(x: int) -> int:
            cnt = 0
            total = 0

            # Enumerate divisors up to sqrt(x)
            for d in range(1, int(math.sqrt(x)) + 1):
                if x % d == 0:
                    d2 = x // d
                    cnt += 1
                    total += d
                    if d2 != d:
                        cnt += 1
                        total += d2
                    if cnt > 4:
                        return 0

            return total if cnt == 4 else 0

        ans = 0
        for x in nums:
            ans += sum_if_four_divisors(x)
        return ans
