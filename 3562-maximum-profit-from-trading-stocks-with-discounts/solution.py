from typing import List
from collections import defaultdict

NEG = -10**15

class Solution:
    def maxProfit(
        self,
        n: int,
        present: List[int],
        future: List[int],
        hierarchy: List[List[int]],
        budget: int
    ) -> int:

        children = defaultdict(list)
        for u, v in hierarchy:
            children[u - 1].append(v - 1)

        def dfs(u: int):
            """
            dp0[b]: parent of u NOT bought
            dp1[b]: parent of u IS bought
            """

            # sub[u_buy][b]
            sub = [[0] + [NEG] * budget, [0] + [NEG] * budget]

            for v in children[u]:
                dpv0, dpv1 = dfs(v)
                nxt = [[NEG] * (budget + 1) for _ in range(2)]

                for u_buy in (0, 1):
                    child_dp = dpv1 if u_buy else dpv0
                    for i in range(budget + 1):
                        if sub[u_buy][i] < 0:
                            continue
                        for j in range(budget - i + 1):
                            if child_dp[j] < 0:
                                continue
                            nxt[u_buy][i + j] = max(
                                nxt[u_buy][i + j],
                                sub[u_buy][i] + child_dp[j]
                            )
                sub = nxt

            # IMPORTANT FIX: baseline is u NOT bought
            dp0 = sub[0][:]
            dp1 = sub[0][:]

            cost = present[u]
            half = cost // 2

            gain_full = future[u] - cost
            gain_half = future[u] - half

            for b in range(budget + 1):
                # parent NOT bought → no discount
                if b >= cost and sub[1][b - cost] >= 0:
                    dp0[b] = max(dp0[b], sub[1][b - cost] + gain_full)

                # parent bought → discount
                if b >= half and sub[1][b - half] >= 0:
                    dp1[b] = max(dp1[b], sub[1][b - half] + gain_half)

            return dp0, dp1

        dp_root, _ = dfs(0)
        return max(dp_root)
