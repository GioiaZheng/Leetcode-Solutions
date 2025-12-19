from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        max_area = 0

        while left < right:
            # Width between the two lines
            width = right - left
            # Height is limited by the shorter line
            h = min(height[left], height[right])
            max_area = max(max_area, width * h)

            # Move the pointer with the smaller height
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_area
