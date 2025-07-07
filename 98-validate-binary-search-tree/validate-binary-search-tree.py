# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def DFS(root,left_val,right_val):
            if not root:
                return True
            
            if root.val<=left_val or root.val>=right_val:
                return False
            
            return DFS(root.left,left_val,root.val) and DFS(root.right,root.val,right_val)
        
        return DFS(root, float("-inf"), float("inf"))
