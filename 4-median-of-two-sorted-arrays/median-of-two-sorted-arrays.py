class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if (len(nums2) < len(nums1)):
            nums1, nums2 = nums2, nums1

        l1 = len(nums1)
        l2 = len(nums2)

        total_size = l1 + l2
        half = total_size // 2

        left = 0
        right = l1

        while (left <= right):
            pivot1 = (left + right) // 2
            pivot2 = half - pivot1

            nums1L = nums1[pivot1 - 1] if pivot1 > 0 else float('-inf')
            nums1R = nums1[pivot1] if pivot1 < l1 else float('inf')
            nums2L = nums2[pivot2 - 1] if pivot2 > 0 else float('-inf')
            nums2R = nums2[pivot2] if pivot2 < l2 else float('inf')

            if (nums1L <= nums2R and nums2L <= nums1R):
                if (total_size % 2 == 1):
                    return min(nums1R, nums2R)
                else:
                    return (max(nums1L, nums2L) + min(nums1R, nums2R)) / 2

            elif (nums2L > nums1R):
                #move pivot1 right
                left = pivot1 + 1
            elif (nums1L > nums2R):
                #move pivot left
                right = pivot1 - 1






# a , b
# [ 3, 4, 5 |]
# [1, | 2, 6, 7, 8]
# c , d

# a < d and c < b

# [ |3, 4]
# [1, 2, 3,| 5, 6]
    