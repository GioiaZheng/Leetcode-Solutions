from typing import List

class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        # Each operation decreases the total sum by exactly 1.
        # We need the sum to become divisible by k.
        # Therefore, the minimum number of operations required
        # is simply sum(nums) % k.
        return sum(nums) % k
