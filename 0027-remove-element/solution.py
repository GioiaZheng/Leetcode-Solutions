class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        """
        Remove all occurrences of val from nums in-place.
        Return the number of elements not equal to val.
        """

        index = -1  # pointer for the next position to fill

        for i in range(len(nums)):
            if nums[i] != val:
                index += 1
                nums[index] = nums[i]

        return index + 1
