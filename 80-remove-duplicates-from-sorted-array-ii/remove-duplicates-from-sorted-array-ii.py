"""
i=4
j=5
[1,1,1,2,2,3]
"""
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i,j=0,0

        while j<len(nums):
            if i<2 or nums[i-2]<nums[j]:
                nums[i]=nums[j]
                i+=1
            j+=1
        
        return i