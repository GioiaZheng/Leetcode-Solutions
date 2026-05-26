from typing import List

class Solution:
    def judgePoint24(self, cards: List[int]) -> bool:
        nums = [float(x) for x in cards]
        return self.dfs(nums)

    def dfs(self, nums: List[float]) -> bool:
        if len(nums) == 1:
            return abs(nums[0] - 24) < 1e-6

        n = len(nums)
        for i in range(n):
            for j in range(n):
                if i == j:
                    continue

                a, b = nums[i], nums[j]
                next_nums = []
                for k in range(n):
                    if k != i and k != j:
                        next_nums.append(nums[k])

                # Try all operations
                for val in self.compute(a, b):
                    next_nums.append(val)
                    if self.dfs(next_nums):
                        return True
                    next_nums.pop()

        return False

    def compute(self, a: float, b: float) -> List[float]:
        res = [a + b, a - b, b - a, a * b]
        if abs(b) > 1e-6:
            res.append(a / b)
        if abs(a) > 1e-6:
            res.append(b / a)
        return res
