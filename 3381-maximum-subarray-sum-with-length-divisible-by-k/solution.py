class Solution:
    def maximumSubarraySum(self, nums, k):
        n = len(nums)

        # prefix[i] = sum of nums[0 .. i-1]
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i+1] = prefix[i] + nums[i]

        # For each remainder group r = (index % k),
        # track the smallest prefix encountered so far.
        min_prefix = [float('inf')] * k

        # prefix[0] = 0, index 0 % k = 0
        min_prefix[0] = 0

        best = -10**30  # very small number

        # iterate prefix indices 1..n
        for i in range(1, n + 1):
            r = i % k

            # Candidate subarray sum:
            # prefix[i] - smallest prefix with same remainder
            best = max(best, prefix[i] - min_prefix[r])

            # Update the minimum prefix for this remainder group
            min_prefix[r] = min(min_prefix[r], prefix[i])

        return best
