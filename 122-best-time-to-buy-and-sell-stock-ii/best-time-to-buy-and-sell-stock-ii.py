class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        hold, not_hold = 0,1

        dp = {}

        dp[(-1,hold)] = -math.inf
        dp[(-1,not_hold)] = 0

        for i,price in enumerate(prices):

            dp[(i,hold)] = max(dp[(i-1,hold)], dp[(i-1,not_hold)]-price)
            dp[(i,not_hold)] = max(dp[(i-1,hold)]+price, dp[(i-1,not_hold)])

        
        return dp[len(prices)-1,not_hold]
