class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        """
        vis = {}
        i<0 or i<=m or j<0 or j<=n or grid[i][j]=='0' or (i,j) in vis
        """
        moves = [(1,0), (0,1), (-1,0), (0,-1)]
        vis = {}
        def dfs(i,j):
            if i<0 or i>=m or j<0 or j>=n or grid[i][j]==0 or (i,j) in vis:
                return 0
            vis[(i,j)] = True
            area = 1
            area += dfs(i+1,j) + dfs(i-1,j) + dfs(i,j+1) + dfs(i,j-1)
            print(area)
            return area
            
        max_area = 0
        m,n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j]==1 and (i,j) not in vis:
                    #calculations part
                    ans=dfs(i,j)
                    max_area = max(max_area,ans)
        
        return max_area