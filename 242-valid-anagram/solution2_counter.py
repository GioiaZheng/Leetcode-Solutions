from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        Approach 2: Counter (Optimal & Unicode-safe)
        Time:  O(n)
        Space: O(1) for fixed alphabet or O(n) for unicode
        """
        return Counter(s) == Counter(t)
