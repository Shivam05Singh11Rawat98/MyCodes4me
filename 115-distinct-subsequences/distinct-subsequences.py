class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        len_s = len(s)
        len_t = len(t)
        cache = {}
        def dfs(m,n):
            if m<n:
                return 0
            if n==0:
                return 1
            if (m,n) in cache:
                return cache[(m,n)]
            
            if s[m-1] == t[n-1]:
                cache[(m,n)] = dfs(m-1,n-1)+dfs(m-1,n)
            else:
                cache[(m,n)] = dfs(m-1,n)
            
            return cache[(m,n)]
        
        return dfs(len_s,len_t)


