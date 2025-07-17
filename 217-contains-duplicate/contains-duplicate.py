class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        my_list = set(nums)
        return not len(nums) == len(my_list)

        