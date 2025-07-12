class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        """
        m+n is even-> 2 medians, else its one
        where these median belongs
        """
        m,n=len(nums1), len(nums2)
        total = m+n
        half = total//2
        if m>n:
            nums1,nums2 = nums2,nums1
        lo=0
        hi = len(nums1)-1
        while True:
            mid1 = lo+(hi-lo)//2
            mid2 = half - mid1 - 2

            Aleft = nums1[mid1] if mid1>=0 else float("-inf")
            Aright = nums1[mid1+1] if mid1+1<len(nums1) else float("inf")
            Bleft = nums2[mid2] if mid2>=0 else float("-inf")
            Bright = nums2[mid2+1] if mid2+1<len(nums2) else float("inf")

            if Aleft<=Bright and Bleft<=Aright:
                if total%2==0:
                    return (max(Aleft,Bleft) + min(Aright,Bright))/2
                else:
                    return min(Aright,Bright)
            elif Aleft>Bright:
                hi=mid1-1
            else:
                lo=mid1+1
                
