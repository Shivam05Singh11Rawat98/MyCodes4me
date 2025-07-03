# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        temp variable
        swap var
        while right
        switch left to right side of temp
        and recurrsion
        based case return and return at last
        """
        if not root:
            return 
              
        if root.left:
            temp=root.left
            while temp and temp.right:
                temp=temp.right
            temp.right = root.right
        root.right = root.left if root.left else root.right
        root.left = None
        self.flatten(root.right)


        