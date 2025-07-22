class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        max_height_l,max_height_r = [0]*n, [0]*n
        max_l,max_r = 0,0
        for i in range(n):
            max_l = max(max_l,height[i])
            max_r = max(max_r,height[n-1-i])
            max_height_l[i] = max_l
            max_height_r[n-1-i] = max_r
        trapped_water = 0
        for i in range(1,n-1):
            if max_height_l[i]>height[i] and max_height_r[i]>height[i]:
                trapped_water+= min(max_height_l[i],max_height_r[i])-height[i]
        
        return trapped_water

"""
h = 0,2,1,0,1,3,2,1,2
l = 1 2 2 2 2 3 3 3 3 
r = 3 3 3 3 3 3 2 2 2 
water=6
"""