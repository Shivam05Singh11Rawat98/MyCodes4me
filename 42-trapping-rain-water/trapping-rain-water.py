class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        trapped_water = 0
        l,r=0,n-1
        max_l,max_r=0,0
        while l<r:
            if height[l]<height[r]:
                max_l=max(max_l,height[l])
                trapped_water+=max_l-height[l]
                l+=1
            else:
                max_r=max(max_r,height[r])
                trapped_water += max_r-height[r]
                r-=1

        return trapped_water
