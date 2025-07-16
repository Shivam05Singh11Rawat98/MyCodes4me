class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        """
        s:bc
        p:a*bc
        case 1: i->m j!->n: False
        case 2: '.' we can match
        case 3: '*'
        Brute Force - O(2**n)
        Can apply caching to avoid redundant work
        """

        m,n = len(s),len(p)
        cache = {}
        def dfs(i,j):
            if (i,j) in cache:
                return cache[(i,j)]
            if i>=m and j>=n:
                return True
            if j>=n:
                return False

            is_match = i<m and (s[i]==p[j] or p[j]=='.')
            if j+1<n and p[j+1] == '*':
                cache[(i,j)] = ((is_match and dfs(i+1,j)) or dfs(i,j+2))
                return cache[(i,j)]
            if is_match:
                cache[(i,j)] = dfs(i+1,j+1)
                return cache[(i,j)]

            cache[(i,j)] = False
            return False

        
        return dfs(0,0)


