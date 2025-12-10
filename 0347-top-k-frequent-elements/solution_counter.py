from collections import Counter
from typing import List

class Solution:
    # -----------------------------------------------------------
    # Method 1: Using Counter (Most Pythonic)
    # -----------------------------------------------------------
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)
        return [num for num, _ in freq.most_common(k)]
