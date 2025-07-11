class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        """
        Brute force- iterate 1,n-2
        """
        n=len(nums)
        lo,hi=0,n-1
        
        while lo<=hi:
            mid = lo + (hi-lo)//2
            leftNeigh = nums[mid-1] if mid>0 else float("-inf")
            rightNeigh = nums[mid+1] if mid<n-1 else float("-inf")
            if nums[mid]>leftNeigh and nums[mid]>rightNeigh:
                return mid
            elif nums[mid]<leftNeigh:
                hi=mid-1
            else:
                lo=mid+1
