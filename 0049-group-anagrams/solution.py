class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        Groups anagrams using a sorted string as the key.
        Time Complexity: O(n * k log k)
        """
        anagram_map = {}

        for s in strs:
            key = ''.join(sorted(s))     # sorting produces an anagram signature
            if key not in anagram_map:
                anagram_map[key] = []
            anagram_map[key].append(s)

        return list(anagram_map.values())
