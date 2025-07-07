class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m,n = len(grid), len(grid[0])
        self.vis = [[0]*n for _ in range(m)]
        moves = [(1,0),(-1,0), (0,1), (0,-1)]
        def DFS(i,j):
            if self.vis[i][j]==1:
                return
            self.vis[i][j]=1
            for (a,b) in moves:
                x,y = i+a,j+b
                if x>=0 and x<m and y>=0 and y<n and grid[x][y]=="1":
                    # print(i,j)
                    DFS(x,y)
                           
            return

        no_island=0
        for i in range(m):
            for j in range(n):
                if grid[i][j]=="1" and self.vis[i][j]==0:
                    DFS(i,j)
                    print("*")
                    no_island+=1

        return no_island

