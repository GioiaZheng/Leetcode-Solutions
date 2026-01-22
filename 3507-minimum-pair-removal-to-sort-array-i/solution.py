class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        def is_sorted(arr):
            return all(arr[i] >= arr[i - 1] for i in range(1, len(arr)))

        ops = 0

        while not is_sorted(nums):
            min_sum = float('inf')
            idx = 0

            for i in range(len(nums) - 1):
                s = nums[i] + nums[i + 1]
                if s < min_sum:
                    min_sum = s
                    idx = i

            # Replace the selected pair
            nums = nums[:idx] + [min_sum] + nums[idx + 2:]
            ops += 1

        return ops
