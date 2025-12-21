from typing import List

class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        n = len(strs)
        m = len(strs[0])

        # sorted[i] = whether strs[i] <= strs[i+1] is already confirmed
        sorted_pairs = [False] * (n - 1)
        deletions = 0

        for col in range(m):
            # Check if this column breaks lexicographic order
            bad = False
            for i in range(n - 1):
                if not sorted_pairs[i] and strs[i][col] > strs[i + 1][col]:
                    bad = True
                    break

            if bad:
                deletions += 1
                continue

            # Otherwise, update sorted_pairs using this column
            for i in range(n - 1):
                if not sorted_pairs[i] and strs[i][col] < strs[i + 1][col]:
                    sorted_pairs[i] = True

        return deletions
