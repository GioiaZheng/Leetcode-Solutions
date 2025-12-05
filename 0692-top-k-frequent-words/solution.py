from collections import Counter
from typing import List

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        # Step 1: count word frequency
        freq = Counter(words)
        
        # Step 2: sort according to:
        # - highest frequency first      → (-freq[w])
        # - alphabetical order for ties  → (w)
        sorted_words = sorted(freq, key=lambda w: (-freq[w], w))
        
        # Step 3: return first k words
        return sorted_words[:k]
