class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m,n=len(board), len(board[0])
        self.vis = [[0]*n for _ in range(m)]
        moves = [(0,1),(1,0),(0,-1),(-1,0)]
        def DFS(i,j):
            if self.vis[i][j]==1:
                return
            self.vis[i][j]=1

            for (a,b) in moves:
                x,y=i+a,j+b
                if 0<=x<m and 0<=y<n and board[x][y]=='O':
                    DFS(x,y)


        for j in range(n):
            if board[0][j]=="O" and self.vis[0][j]==0:
                DFS(0,j)
            if board[m-1][j]=="O" and self.vis[m-1][j]==0:
                DFS(m-1,j)
        
        for i in range(m):
            if board[i][0]=="O" and self.vis[i][0]==0:
                DFS(i,0)
            if board[i][n-1]=="O" and self.vis[i][n-1]==0:
                DFS(i,n-1)

        
        for i in range(1,m-1):
            for j in range(1,n-1):
                if board[i][j]=='O' and self.vis[i][j]==0:
                    board[i][j]='X'


