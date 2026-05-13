from collections import Counter
from typing import List


class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        freq = Counter(nums)
        duplicates = sum(1 for count in freq.values() if count > 1)

        operations = 0
        index = 0

        while duplicates > 0:
            for _ in range(3):
                if index >= len(nums):
                    break

                value = nums[index]
                if freq[value] == 2:
                    duplicates -= 1
                freq[value] -= 1
                index += 1

            operations += 1

        return operations
