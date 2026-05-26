from typing import List
from collections import defaultdict

class Solution:
    def pyramidTransition(self, bottom: str, allowed: List[str]) -> bool:
        # Build mapping: (left, right) -> possible top letters
        mp = defaultdict(list)
        for a, b, c in allowed:
            mp[(a, b)].append(c)

        # Memoization: curr_string -> can_build (True / False)
        memo = {}

        def dfs(curr: str) -> bool:
            if curr in memo:
                return memo[curr]

            if len(curr) == 1:
                return True

            # Try to build next level
            def backtrack(i: int, path: List[str]) -> bool:
                if i == len(curr) - 1:
                    return dfs("".join(path))

                pair = (curr[i], curr[i + 1])
                if pair not in mp:
                    return False

                for ch in mp[pair]:
                    path.append(ch)
                    if backtrack(i + 1, path):
                        return True
                    path.pop()

                return False

            res = backtrack(0, [])
            memo[curr] = res
            return res

        return dfs(bottom)
