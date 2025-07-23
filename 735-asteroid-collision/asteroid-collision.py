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
            flag=1
            while len(stack) and ast<0:
                if stack[-1]>0 and -1*ast > stack[-1]:
                    stack.pop()
                elif stack[-1]>0 and -1*ast == stack[-1]:
                    stack.pop()
                    flag=0
                    break
                elif stack[-1]<0:
                    stack.append(ast)
                    break
                else:
                    break

            if (ast>0 or len(stack)==0) and flag:
                stack.append(ast)

        return stack
        