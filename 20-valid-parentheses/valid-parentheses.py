class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]

        for ch in s:
            if ch in ['(','{','[']:
                stack.append(ch)
            else:
                if len(stack)==0 or ch == ')' and stack[-1]!='(':
                    return False
                elif len(stack)==0 or ch == '}' and stack[-1]!='{':
                    return False
                elif len(stack)==0 or ch == ']' and stack[-1]!='[':
                    return False
                else:
                    stack.pop()
        

        return len(stack)==0