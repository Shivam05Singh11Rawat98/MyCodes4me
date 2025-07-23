"""
edge case = [3,2,1]
case =inf[3,2,7,2,5,9]
buy=2
max_prof = 7
"""
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy=math.inf
        max_profit = 0

        for price in prices:
            if price<buy:
                buy=price
            else:
                max_profit = max(max_profit, price-buy)
        
        return max_profit





