class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        """
        0->-2,0->2,-2,-4,0->-1,2,-1,-2
        """
        n = len(prices)
        mem = {}
        def DFS(i,no_buy,op):
            if op==0 or i>=n:
                return 0
            if (i,no_buy,op) in mem:
                return mem[(i,no_buy,op)]
            
            mem[(i,no_buy,op)] = max(DFS(i+1,not no_buy,op-1) + (prices[i] if no_buy else -prices[i]), DFS(i+1,no_buy,op))
            return mem[(i,no_buy,op)]
        
        return DFS(0,0,2*k)