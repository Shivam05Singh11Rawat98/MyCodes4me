"""
[5,7,4,3,9,10,0,11,14,8]
ele=
stack =  
max_area = 2
"""
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        res=0
        for h in heights+[-1]:
            steps=0
            while stack and stack[-1][1]>=h:
                w,val = stack.pop()
                steps+=w
                res=max(res,val*steps)
            
            if h!=-1: stack.append((steps+1,h))
        
        return res