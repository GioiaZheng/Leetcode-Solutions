class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        # Total sum of the array
        total = sum(nums)

        # If total sum is odd, left_sum - right_sum can never be even.
        # Because parity(left - right) = parity(total)
        # Therefore, an odd total implies an odd difference, so no valid partitions.
        if total % 2 == 1:
            return 0

        # If the total sum is even, every split point works, so there are (n - 1) valid partitions.
        return len(nums) - 1
