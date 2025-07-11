class Solution:
    def findMin(self, nums: List[int]) -> int:
        """
        if we are left side of the pivot
        """
        lo,hi=0,len(nums)-1
        min_ele = float("inf")
        while lo<=hi:
            mid=lo+(hi-lo)//2

            if nums[mid]<=nums[hi]:
                min_ele = min(min_ele,nums[mid])
                hi=mid-1
            else:
                lo=mid+1
        
        return min_ele
