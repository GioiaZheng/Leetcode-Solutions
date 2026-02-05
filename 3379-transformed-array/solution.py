class Solution:
    def constructTransformedArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [0] * n

        for i, x in enumerate(nums):
            if x == 0:
                res[i] = 0
            else:
                res[i] = nums[(i + x) % n]

        return res
