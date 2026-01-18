class Solution:
    def largestMagicSquare(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        # Row and column prefix sums
        rowSum = [[0] * (n + 1) for _ in range(m)]
        colSum = [[0] * n for _ in range(m + 1)]

        for i in range(m):
            for j in range(n):
                rowSum[i][j + 1] = rowSum[i][j] + grid[i][j]
                colSum[i + 1][j] = colSum[i][j] + grid[i][j]

        def is_magic(r, c, k):
            target = rowSum[r][c + k] - rowSum[r][c]

            # Rows
            for i in range(r, r + k):
                if rowSum[i][c + k] - rowSum[i][c] != target:
                    return False

            # Columns
            for j in range(c, c + k):
                if colSum[r + k][j] - colSum[r][j] != target:
                    return False

            # Diagonals
            diag1 = sum(grid[r + i][c + i] for i in range(k))
            diag2 = sum(grid[r + i][c + k - 1 - i] for i in range(k))

            return diag1 == target and diag2 == target

        max_k = min(m, n)
        for k in range(max_k, 1, -1):
            for i in range(m - k + 1):
                for j in range(n - k + 1):
                    if is_magic(i, j, k):
                        return k

        return 1
