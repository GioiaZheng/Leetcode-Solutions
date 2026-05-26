from typing import List

class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        total = 0
        neg_count = 0
        min_abs = float('inf')

        for row in matrix:
            for x in row:
                if x < 0:
                    neg_count += 1
                abs_x = abs(x)
                total += abs_x
                min_abs = min(min_abs, abs_x)

        # If number of negatives is odd, one smallest absolute value must stay negative
        if neg_count % 2 == 1:
            total -= 2 * min_abs

        return total
