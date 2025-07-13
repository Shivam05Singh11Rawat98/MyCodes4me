class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        heap = []
        heappush(heap,(nums1[0]+nums2[0],0,0))
        res = []
        n1=len(nums1)
        n2=len(nums2)
        visited = set()
        visited.add((0,0))
        while k and heap:
            sum,i1,i2=heappop(heap)
            res.append([nums1[i1],nums2[i2]])

            if i2+1<n2 and (i1,i2+1) not in visited:
                heappush(heap,(nums1[i1]+nums2[i2+1], i1, i2+1))
                visited.add((i1,i2+1))
            
            if i1+1<n1 and (i1+1,i2) not in visited:
                heappush(heap,(nums1[i1+1]+nums2[i2], i1+1, i2))
                visited.add((i1+1,i2))
            k-=1
        

        return res