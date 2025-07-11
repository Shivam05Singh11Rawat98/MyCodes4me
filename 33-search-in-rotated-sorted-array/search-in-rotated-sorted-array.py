class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lo,hi=0,len(nums)-1
        """
        Description main logic
        """
        while lo<=hi:
            mid = lo + (hi-lo)//2

            if nums[mid]==target:
                return mid
            
            if nums[mid]<target:
                if nums[lo]<nums[mid] or nums[hi]>=target:
                    lo=mid+1
                else:
                    hi=mid-1
            else:
                if nums[hi]>nums[mid] or nums[lo]<=target :
                    hi=mid-1
                else:
                    lo=mid+1
        
        return -1