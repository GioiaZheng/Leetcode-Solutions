class Solution:
    def largestSquareArea(self, bottomLeft: List[List[int]], topRight: List[List[int]]) -> int:
        n = len(bottomLeft)
        ans = 0

        for i in range(n):
            x1_i, y1_i = bottomLeft[i]
            x2_i, y2_i = topRight[i]

            for j in range(i + 1, n):
                x1_j, y1_j = bottomLeft[j]
                x2_j, y2_j = topRight[j]

                # Intersection rectangle
                x_left = max(x1_i, x1_j)
                y_bottom = max(y1_i, y1_j)
                x_right = min(x2_i, x2_j)
                y_top = min(y2_i, y2_j)

                if x_left < x_right and y_bottom < y_top:
                    width = x_right - x_left
                    height = y_top - y_bottom
                    side = min(width, height)
                    ans = max(ans, side * side)

        return ans
