class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        """
        how to check for same combi
        """
        res = []
        n = len(candidates)
        def bTracking(remain_sum,sol,j):
            if remain_sum==0:
                res.append(sol[:])
                return
            if remain_sum<0:
                return
            for i in range(j,n):
                e = candidates[i]
                remain_sum-=e
                sol.append(e)
                bTracking(remain_sum,sol,i)
                remain_sum+=e
                sol.pop(-1)
        
        bTracking(target,[],0)
        return res