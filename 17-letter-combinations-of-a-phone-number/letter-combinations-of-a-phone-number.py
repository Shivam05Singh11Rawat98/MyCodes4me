class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        num2ch = {'2':"abc",'3':"def",'4':"ghi",'5':"jkl",'6':"mno",'7':"pqrs",'8':"tuv",'9':"wxyz"}
        res=[]
        n = len(digits)
        def bTracking(i,s):
            #Base case
            if i==n:
                res.append(s[:])
                return
            # character of the logic
            ch = digits[i]
            #recursive call and the calculation
            for val in num2ch[ch]:
                bTracking(i+1,s+val)
        
        bTracking(0,"")

        return res
