class Solution:
    def numOfWays(self, n: int) -> int:
        MOD = 10**9 + 7

        # There are only two valid pattern types for one row:
        # 1) ABA: first and third color same (e.g. RGR)
        # 2) ABC: all three colors different (e.g. RGB)

        # Base case for n = 1
        aba = 6   # 3 choices for A, 2 choices for B
        abc = 6   # 3 * 2 * 1

        for _ in range(2, n + 1):
            new_aba = (aba * 3 + abc * 2) % MOD
            new_abc = (aba * 2 + abc * 2) % MOD
            aba, abc = new_aba, new_abc

        return (aba + abc) % MOD
