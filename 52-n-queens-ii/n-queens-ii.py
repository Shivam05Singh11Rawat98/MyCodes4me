class Solution:
    def totalNQueens(self, n: int) -> int:
        """
        """
        self.cnt=0
        self.col = [False]*n
        self.diag1 = [False]*(2*n-1)
        self.diag2 = [False]*(2*n-1)


        def bTracking(i):
            if i==n:
                self.cnt+=1
                return
            
            for j in range(n):
                if self.col[j] or self.diag1[i+j] or self.diag2[j-i+n-1]:
                    continue
                self.col[j] = self.diag1[i+j] = self.diag2[j-i+n-1]= True
                bTracking(i+1)
                self.col[j] = self.diag1[i+j] = self.diag2[j-i+n-1]=False

        bTracking(0)
        return self.cnt
