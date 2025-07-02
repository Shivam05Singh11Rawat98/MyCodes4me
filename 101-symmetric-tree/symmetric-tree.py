# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetricUtil(self,p,q):
        if p==None and q==None:
            return True
        if p==None or q==None or p.val!=q.val:
            return False
        return self.isSymmetricUtil(p.left,q.right) and self.isSymmetricUtil(p.right,q.left)
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return self.isSymmetricUtil(root,root)