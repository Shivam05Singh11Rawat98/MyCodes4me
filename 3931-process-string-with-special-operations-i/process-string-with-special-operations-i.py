class Solution:
    def processStr(self, s: str) -> str:
        t = ""

        for ch in s:
            if ch in ['*','#','%']:
                if len(t)!=0:
                    if ch=='*':
                        t=t[:-1]
                    elif ch=='#':
                        t=t+t
                    else:
                        t=t[::-1]
            else:
                t+=ch
        
        return t