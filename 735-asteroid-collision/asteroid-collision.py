"""
invalid case - [1,2]
Edge cases - [8,-8]
stack = []
"""
class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        n = len(asteroids)
        if n<2:
            return asteroids

        for ast in asteroids:
            if ast>0 or len(stack)==0:
                stack.append(ast)
            else:
                flag=1
                while len(stack) and stack[-1]>0:
                    if stack[-1]<abs(ast):
                        stack.pop()
                    elif stack[-1]==abs(ast):
                        stack.pop()
                        flag=0
                        break
                    else:
                        flag=0
                        break
                    
                if flag==1:
                    stack.append(ast)

            

        return stack
        