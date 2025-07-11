"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        m,n=len(grid), len(grid[0])
        if not grid:
            return Node(False, True, None, None, None, None)
        start=grid[0][0]
        xmid, ymid = (m-1)//2, (n-1)//2
        flag=False
        for i in range(m):
            for j in range(n):
                if grid[i][j]!=start:
                    flag = True
                    break
        
        if not flag:
            return Node(True if start==1 else False, True, None, None, None, None)

        return Node(
            True,
            False,
            topLeft = self.construct([row[:n//2] for row in grid[:n//2]]),
            topRight = self.construct([row[n//2:] for row in grid[:n//2]]),
            bottomLeft = self.construct([row[:n//2] for row in grid[n//2:]]),
            bottomRight = self.construct([row[n//2:] for row in grid[n//2:]])
        )