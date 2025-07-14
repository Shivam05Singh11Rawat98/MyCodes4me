class Solution:
    def countSubstrings(self, s: str) -> int:
        
        n = len(s)
        def calPali(i,j):
            res=0
            l,h=i,j
            while l>=0 and h<n and s[l]==s[h]:
                l-=1
                h+=1
                res+=1

            return res
                
        res=0
        for i in range(n):
            odd = calPali(i,i)
            even = calPali(i,i+1)

            res+=odd+even
        
        return res