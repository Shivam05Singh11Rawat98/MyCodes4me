# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        q = []
        q.append(root)
        nodes = 0

        while q:
            n=len(q)
            nodes+=n
            for i in range(n):
                temp=q.pop(0)

                if temp.left:
                    q.append(temp.left)
                if temp.right:
                    q.append(temp.right)
        
        return nodes
