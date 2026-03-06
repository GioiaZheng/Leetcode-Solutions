class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        # Get matrix dimensions
        m, n = len(mat), len(mat[0])

        # Count number of 1s in each row
        row_sum = [0] * m
        # Count number of 1s in each column
        col_sum = [0] * n

        # First pass: compute row and column sums
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 1:
                    row_sum[i] += 1
                    col_sum[j] += 1

        special = 0

        # Second pass: check special positions
        for i in range(m):
            for j in range(n):
                # A position is special if:
                # 1. The value is 1
                # 2. There is exactly one 1 in its row
                # 3. There is exactly one 1 in its column
                if mat[i][j] == 1 and row_sum[i] == 1 and col_sum[j] == 1:
                    special += 1

        return special
