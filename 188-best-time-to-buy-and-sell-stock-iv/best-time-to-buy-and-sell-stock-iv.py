class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        """
        0->-2,0->2,-2,-4,0->-1,2,-1,-2
        """
        n = len(prices)
        cache = {}
        def dfs(i,buy,op):
            print(i,op)
            if op==0 or i>=n:
                return 0
            if (i,buy,op) in cache:
                return cache[(i,buy,op)]
            
            if buy:
                profit = max(-prices[i] + dfs(i+1, False, op-1), dfs(i+1, True, op))
            else:
                profit = max(prices[i] + dfs(i+1, True, op-1), dfs(i+1, False, op))
            cache[(i, buy, op)] = profit
            return profit

        return dfs(0,True,2*k)