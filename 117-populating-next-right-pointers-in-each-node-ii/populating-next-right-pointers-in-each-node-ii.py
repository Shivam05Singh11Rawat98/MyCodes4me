"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        """
        BFS
        queue
        right side
        start from None 
        """
        if not root:
            return root
        q = []
        q.append(root)

        while q:
            next=None
            n=len(q)
            for i in range(n):
                temp = q.pop(0)
                temp.next=next
                next = temp
                if temp.right:
                    q.append(temp.right)
                if temp.left:
                    q.append(temp.left)

        return root


