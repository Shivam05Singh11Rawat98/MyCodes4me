class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        """
        [1,2,2,3,3]
        """
        i=0

        for num in nums:
            if i<2 or num>nums[i-2]:
                nums[i]=num
                i+=1
        
        return i
