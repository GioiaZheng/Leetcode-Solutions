class Solution:
    def numberOfPaths(self, grid, k):
        # The modulo required by the problem
        MOD = 10**9 + 7

        # Get matrix dimensions
        m, n = len(grid), len(grid[0])

        """
        dp[i][j][r] = number of paths from (0,0) to (i,j)
                       such that the path-sum % k = r

        There are k possible remainders: 0,1,...,k-1.
        """
        dp = [[[0] * k for _ in range(n)] for __ in range(m)]

        # Starting point: only one "path", its remainder = grid[0][0] % k
        dp[0][0][grid[0][0] % k] = 1

        # Iterate through each cell
        for i in range(m):
            for j in range(n):

                # Current cell value mod k
                val = grid[i][j] % k

                # Transition from the cell above (i-1, j)
                if i > 0:
                    # For every possible remainder r of paths above
                    for r in range(k):
                        # New remainder after adding current cell value
                        new_r = (r + val) % k
                        dp[i][j][new_r] = (dp[i][j][new_r] + dp[i-1][j][r]) % MOD

                # Transition from the cell on the left (i, j-1)
                if j > 0:
                    # For every possible remainder r of paths from left
                    for r in range(k):
                        new_r = (r + val) % k
                        dp[i][j][new_r] = (dp[i][j][new_r] + dp[i][j-1][r]) % MOD

        # Final answer: number of paths reaching bottom-right
        # with remainder 0 (i.e., sum divisible by k)
        return dp[m-1][n-1][0]
