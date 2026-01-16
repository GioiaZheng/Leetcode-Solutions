class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float('inf')
        max_profit = 0

        for price in prices:
            # update the lowest buying price so far
            if price < min_price:
                min_price = price
            else:
                # profit if we sell today
                max_profit = max(max_profit, price - min_price)

        return max_profit
