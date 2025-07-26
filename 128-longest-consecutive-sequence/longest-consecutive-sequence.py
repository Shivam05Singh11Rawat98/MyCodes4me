class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        max_cons = 0
        nums_set = set(nums)
        #[100,4,200,1,3,2]
        for key in nums_set:
            if key-1 not in nums_set:
                temp_cnt=1
                i=key+1
                while i in nums_set:
                    temp_cnt+=1
                    i+=1
                max_cons = max(max_cons,temp_cnt)

        return max_cons