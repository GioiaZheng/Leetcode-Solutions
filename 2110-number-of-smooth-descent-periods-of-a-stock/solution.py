class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        ans = 0
        length = 1  # length of current smooth descent segment

        for i in range(len(prices)):
            if i > 0 and prices[i - 1] - prices[i] == 1:
                length += 1
            else:
                length = 1
            ans += length

        return ans
