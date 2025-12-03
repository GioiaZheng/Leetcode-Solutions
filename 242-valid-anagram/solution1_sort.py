class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        Approach 1: Sorting
        Time:  O(n log n)
        Space: O(1) or O(n) depending on sorting implementation
        """
        return sorted(s) == sorted(t)
