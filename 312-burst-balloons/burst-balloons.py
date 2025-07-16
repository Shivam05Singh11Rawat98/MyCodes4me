class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        """
        [3],1,[5,8]
        1+3+ 15+ 40 + 40
        3+15+ 
        """
        nums=[1]+nums+[1]
        n=len(nums)
        cache = {}
        def dfs(i,j):
            if j<i:
                return 0
            if (i,j) in cache:
                return cache[(i,j)]
            cache[(i,j)] = float("-inf")
            for k in range(i,j+1):
                cost_prev = nums[i-1]
                cost_after = nums[j+1]
                temp_ans = dfs(i,k-1) + cost_prev*nums[k]*cost_after + dfs(k+1,j)
                cache[(i,j)] = max(temp_ans,cache[(i,j)])
            return cache[(i,j)]
        
        return dfs(1,n-2)
