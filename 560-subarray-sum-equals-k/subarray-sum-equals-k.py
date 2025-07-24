"""
Constrainsts - 
Input format - 
Output format - 
Edge case - 
Example - [1,-1,1,1,1,1] ,k=3
"""
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res=0
        prefix_freq = {0:1}
        prefix = 0
        for num in nums:
            prefix+=num
            if prefix-k in prefix_freq:
                res+=prefix_freq[prefix-k]
            
            if prefix in prefix_freq:
                prefix_freq[prefix]+=1
            else:
                prefix_freq[prefix]=1
        
        return res
