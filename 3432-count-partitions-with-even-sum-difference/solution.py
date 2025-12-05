class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        # Total sum of the array
        total = sum(nums)

        # If total sum is odd, left_sum - right_sum can never be even.
        # Because parity(left - right) = parity(total)
        # → so odd total ⇒ odd difference ⇒ no valid partitions.
        if total % 2 == 1:
            return 0

        # If total sum is even, ALL (n − 1) partitions are valid.
        return len(nums) - 1
