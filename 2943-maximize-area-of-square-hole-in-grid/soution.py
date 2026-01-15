class Solution:
    def maximizeSquareHoleArea(self, n: int, m: int, hBars: List[int], vBars: List[int]) -> int:
        def max_consecutive(arr: List[int]) -> int:
            if not arr:
                return 0
            arr.sort()
            longest = curr = 1
            for i in range(1, len(arr)):
                if arr[i] == arr[i - 1] + 1:
                    curr += 1
                else:
                    longest = max(longest, curr)
                    curr = 1
            return max(longest, curr)

        max_h = max_consecutive(hBars)
        max_v = max_consecutive(vBars)

        side = min(max_h + 1, max_v + 1)
        return side * side
