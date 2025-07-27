class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        stack = []
        largest_rect_area = 0
        for height in heights+[-1]:
            steps = 0
            while len(stack) and stack[-1][0]>height:
                ht,st = stack.pop()
                steps+=st
                largest_rect_area = max(largest_rect_area,ht*steps)
            
            stack.append((height,steps+1))
        
        return largest_rect_area
