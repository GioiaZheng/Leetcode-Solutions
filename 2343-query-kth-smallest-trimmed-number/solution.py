from typing import List

class Solution:
    def smallestTrimmedNumbers(self, nums: List[str], queries: List[List[int]]) -> List[int]:
        n = len(nums)
        L = len(nums[0])

        # Cache results for each trim length
        # trim_len -> sorted list of (trimmed_string, index)
        cache = {}

        def get_sorted(trim_len: int):
            if trim_len not in cache:
                arr = []
                for i, num in enumerate(nums):
                    trimmed = num[L - trim_len:]
                    arr.append((trimmed, i))
                # Sort by trimmed value, then by index
                arr.sort()
                cache[trim_len] = arr
            return cache[trim_len]

        ans = []

        for k, trim in queries:
            sorted_arr = get_sorted(trim)
            ans.append(sorted_arr[k - 1][1])

        return ans
