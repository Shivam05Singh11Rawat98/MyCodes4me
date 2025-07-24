"""
[3,5,4,7,11]
k=5 [1,2,...,11]
h=8
"""
class Solution:
    def isPossible(self,mid,piles):
        sum_hrs=0
        for i in range(len(piles)):
            sum_hrs+= math.ceil(piles[i]/mid)
        return sum_hrs


    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        if h<len(piles,):
            return -1
        
        hi = max(piles)
        lo = 1
        while lo<=hi:
            mid = lo + (hi-lo)//2
            if self.isPossible(mid,piles)<=h:
                hi=mid-1
            else:
                lo=mid+1
        
        return lo