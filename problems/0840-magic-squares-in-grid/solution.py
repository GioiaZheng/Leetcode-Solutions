from typing import List

class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])

        def is_magic(r: int, c: int) -> bool:
            # All numbers must be distinct and between 1 and 9
            nums = set()
            for i in range(r, r + 3):
                for j in range(c, c + 3):
                    v = grid[i][j]
                    if v < 1 or v > 9:
                        return False
                    nums.add(v)
            if len(nums) != 9:
                return False

            # In a 3x3 magic square with numbers 1..9, center must be 5
            if grid[r + 1][c + 1] != 5:
                return False

            s = sum(grid[r][c:c + 3])

            # Check rows
            for i in range(r, r + 3):
                if sum(grid[i][c:c + 3]) != s:
                    return False

            # Check columns
            for j in range(c, c + 3):
                if grid[r][j] + grid[r + 1][j] + grid[r + 2][j] != s:
                    return False

            # Check diagonals
            if grid[r][c] + grid[r + 1][c + 1] + grid[r + 2][c + 2] != s:
                return False
            if grid[r][c + 2] + grid[r + 1][c + 1] + grid[r + 2][c] != s:
                return False

            return True

        count = 0
        for i in range(rows - 2):
            for j in range(cols - 2):
                if is_magic(i, j):
                    count += 1

        return count
