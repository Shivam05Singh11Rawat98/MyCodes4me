class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        """
        if l_w2=0, l_w1
        if l_w1=0, l_w2
        if c_w1 == c_w2:
            move to the next ch
            cache our iterations to not repeat it
        """
        cache = {}
        len_w1,len_w2 = len(word1), len(word2)
        def dfs(m,n):
            if m==0:
                return n
            if n==0:
                return m
            if (m,n) in cache:
                return cache[(m,n)]
            if word1[m-1]==word2[n-1]:
                cache[(m,n)] = dfs(m-1,n-1)
            else:
                cache[(m,n)] = 1 + min(dfs(m-1,n-1),dfs(m,n-1),dfs(m-1,n))
            return cache[(m,n)]
        
        return dfs(len_w1, len_w2)
