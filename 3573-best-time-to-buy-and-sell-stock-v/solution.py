from typing import List

class Solution:
    def maximumProfit(self, prices: List[int], k: int) -> int:
        NEG_INF = -10**30
        
        # dp[t][state]
        dp = [[NEG_INF] * 3 for _ in range(k + 1)]
        dp[0][0] = 0  # start free, 0 profit
        
        for price in prices:
            new_dp = [row[:] for row in dp]
            for t in range(k + 1):
                # Free -> Buy (long)
                new_dp[t][1] = max(new_dp[t][1], dp[t][0] - price)
                
                # Free -> Sell (short)
                new_dp[t][2] = max(new_dp[t][2], dp[t][0] + price)
                
                if t + 1 <= k:
                    # Long -> Sell
                    new_dp[t + 1][0] = max(new_dp[t + 1][0], dp[t][1] + price)
                    
                    # Short -> Buy back
                    new_dp[t + 1][0] = max(new_dp[t + 1][0], dp[t][2] - price)
            
            dp = new_dp
        
        # Best result: any completed transactions, free state
        return max(dp[t][0] for t in range(k + 1))
