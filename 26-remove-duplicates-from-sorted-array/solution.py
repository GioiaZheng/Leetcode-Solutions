class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        # i tracks the position of the last unique element
        i = 0

        # j scans through the array
        for j in range(1, len(nums)):
            if nums[j] != nums[i]:
                i += 1
                nums[i] = nums[j]

        # number of unique elements = i + 1
        return i + 1
