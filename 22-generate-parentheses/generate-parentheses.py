class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res=[]
        def bTracking(s,open,close):
            if close==0:
                res.append(s[:])
                return
            
            if open!=0:
                print(s[:])
                bTracking(s+'(',open-1,close)
            
            if close>open:
                bTracking(s+')',open,close-1)
            

        
        bTracking("",n,n)
        return res