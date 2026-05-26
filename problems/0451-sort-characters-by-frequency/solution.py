from collections import Counter

class Solution:
    def frequencySort(self, s: str) -> str:
        # Step 1: count frequency of each character
        freq = Counter(s)

        # Step 2: sort characters by decreasing frequency
        sorted_chars = sorted(freq, key=lambda c: freq[c], reverse=True)

        # Step 3: build the result string
        res = ""
        for c in sorted_chars:
            res += c * freq[c]

        return res
