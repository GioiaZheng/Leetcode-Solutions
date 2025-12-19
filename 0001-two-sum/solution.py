class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}  # value → index

        for i, num in enumerate(nums):
            diff = target - num

            # If the complement is already in the map, solution found
            if diff in seen:
                return [seen[diff], i]

            # Otherwise, store this number with its index
            seen[num] = i

        # Not needed because problem guarantees one solution
        return []
