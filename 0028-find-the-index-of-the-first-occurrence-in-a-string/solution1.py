class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        """
        Solution 1: Use Python built-in string method `find`.
        Returns the first index of needle in haystack, or -1 if not found.
        Time: O(m*n) in worst case (internal implementation), 
        but optimized in CPython.
        """
        return haystack.find(needle)
