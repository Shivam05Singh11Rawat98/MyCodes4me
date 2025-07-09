class Solution:
    def totalNQueens(self, n: int) -> int:
        """
        """
        self.cnt=0
        self.chess = [[0]*n for _ in range(n)]
        def check(x,y):
            for i in range(n):
                if self.chess[i][y]==1:
                    return False
                if self.chess[x][i]==1:
                    return False
                if 0<=(x-i)<n and 0<=(y-i)<n and self.chess[x-i][y-i]==1:
                    return False
                if 0<=(x+i)<n and 0<=(y-i)<n and self.chess[x+i][y-i]==1:
                    return False
                if 0<=(x+i)<n and 0<=(y+i)<n and self.chess[x+i][y+i]==1:
                    return False
                if 0<=(x-i)<n and 0<=(y+i)<n and self.chess[x-i][y+i]==1:
                    return False
            
            return True


        def bTracking(i):
            if i==n:
                self.cnt+=1
                return
            
            for j in range(n):
                if check(i,j):
                    self.chess[i][j]=1
                    bTracking(i+1)
                    self.chess[i][j]=0

        bTracking(0)
        return self.cnt
