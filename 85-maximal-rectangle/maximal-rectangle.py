class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        rows,cols = len(matrix), len(matrix[0])
        max_area = 0

        heights = [0]*(cols+1)
        
        for i in range(rows):
            for j in range(cols):
                heights[j] = heights[j]+1 if matrix[i][j]=="1" else 0
            
            stack = []
            temp_max=0
            print(heights)
            for h in heights:
                steps = 0
                while stack and stack[-1][1]>=h:
                    w,h_val = stack.pop()
                    steps+=w
                    temp_max = max(temp_max, h_val*steps)
                
                stack.append((steps+1,h))
            
            max_area = max(max_area,temp_max)
        

        return max_area

