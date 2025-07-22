class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        trapped_water = 0
        stack = []
        for i in range(n):
            while len(stack) and height[i]>height[stack[-1]]:
                top = stack[-1]
                stack.pop()
                if len(stack)==0:
                    break
                # current = stack[-1]
                distance = i - stack[-1] - 1
                water_height = min(height[i], height[stack[-1]]) - height[top]
                trapped_water+=distance*water_height

            stack.append(i)
        
        return trapped_water
