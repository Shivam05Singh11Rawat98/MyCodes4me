class Solution:
    def binarySearch(self, nums, target, left):
        lo=0
        hi = len(nums)-1
        i=-1
        while lo<=hi:
            mid=lo+(hi-lo)//2
            if nums[mid]<target:
                lo=mid+1
            elif nums[mid]>target:
                hi=mid-1
            else:
                i=mid
                if left:
                    hi=mid-1
                else:
                    lo=mid+1      
        return i
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left = self.binarySearch(nums,target,True)
        right = self.binarySearch(nums,target,False)

        return [left,right]