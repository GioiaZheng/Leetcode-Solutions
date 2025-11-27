class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        """
        Solution 2: Manual substring checking using sliding window.
        Time: O((m - n + 1) * n)
        Space: O(1)
        """
        m, n = len(haystack), len(needle)

        # Edge case: empty needle → return 0
        if n == 0:
            return 0

        # Only need to check starting positions 0 to m - n
        for i in range(m - n + 1):
            # If substring matches, return this index
            if haystack[i : i + n] == needle:
                return i

        return -1
