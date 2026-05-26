from typing import List

class Solution:
    def maxProfit(self, prices: List[int], strategy: List[int], k: int) -> int:
        n = len(prices)

        # 1. Compute base profit
        base_profit = 0
        for i in range(n):
            base_profit += strategy[i] * prices[i]

        # 2. Prefix sums
        # ps_price[i] = sum of prices[0:i]
        # ps_strategy_profit[i] = sum of strategy[j] * prices[j] for j in [0, i)
        ps_price = [0] * (n + 1)
        ps_strategy_profit = [0] * (n + 1)

        for i in range(n):
            ps_price[i + 1] = ps_price[i] + prices[i]
            ps_strategy_profit[i + 1] = ps_strategy_profit[i] + strategy[i] * prices[i]

        max_profit = base_profit
        half = k // 2

        # 3. Sliding window of length k
        for l in range(0, n - k + 1):
            r = l + k

            # original profit contribution of this window
            original_window_profit = (
                ps_strategy_profit[r] - ps_strategy_profit[l]
            )

            # modified profit:
            # first half -> 0 contribution
            # second half -> sell => sum of prices
            sell_sum = ps_price[l + k] - ps_price[l + half]

            new_profit = base_profit - original_window_profit + sell_sum
            max_profit = max(max_profit, new_profit)

        return max_profit
