class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        """
        i<0 and j<0 and i>=m and j>=n
        max((i+1,j),(i-1, j), (i,j+1), (i,j-1))
        """
        m,n = len(matrix),len(matrix[0])
        cache = {}
        def dfs(prev,i,j):
            if i<0 or j<0 or i>=m or j>=n or prev>=matrix[i][j]:
                return 0
            if (i,j) in cache:
                return cache[(i,j)]
            cache[(i,j)] = 1+ max(dfs(matrix[i][j],i+1,j),
            dfs(matrix[i][j],i-1, j), dfs(matrix[i][j],i,j+1), dfs(matrix[i][j],i,j-1))

            return cache[(i,j)]
        
        max_path = 0

        for i in range(m):
            for j in range(n):
                max_path = max(dfs(-1,i,j),max_path)
        
        return max_path