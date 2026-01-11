from typing import List

class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix or not matrix[0]:
            return 0

        rows, cols = len(matrix), len(matrix[0])
        heights = [0] * cols
        max_area = 0

        for r in range(rows):
            # Build histogram heights
            for c in range(cols):
                if matrix[r][c] == '1':
                    heights[c] += 1
                else:
                    heights[c] = 0

            # Compute largest rectangle in histogram
            stack = []
            for i in range(cols + 1):
                curr_height = heights[i] if i < cols else 0

                while stack and curr_height < heights[stack[-1]]:
                    h = heights[stack.pop()]
                    left = stack[-1] + 1 if stack else 0
                    width = i - left
                    max_area = max(max_area, h * width)

                stack.append(i)

        return max_area
