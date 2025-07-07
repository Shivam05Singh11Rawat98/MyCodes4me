"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return node
        graphMap = defaultdict()
        self.vis = set()

        def DFS(root):
            if not root or root in self.vis:
                return
            self.vis.add(root)
            newNode = Node(root.val)
            graphMap[root] = newNode
            for i in root.neighbors:
                DFS(i)
        
        DFS(node)
        
        for key, val in graphMap.items():
            for i in key.neighbors:
                val.neighbors.append(graphMap[i])
        
        return graphMap[node]