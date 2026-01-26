from typing import List

class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        res = []
        min_diff = float('inf')

        for i in range(len(arr) - 1):
            diff = arr[i + 1] - arr[i]
            if diff < min_diff:
                min_diff = diff
                res = [[arr[i], arr[i + 1]]]
            elif diff == min_diff:
                res.append([arr[i], arr[i + 1]])

        return res
