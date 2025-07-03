# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.total=0
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        def calSum(tmp,num):
            if tmp.left==None and tmp.right==None:
                self.total+=num
                return
            if tmp.left:
                calSum(tmp.left, (num*10+tmp.left.val))
            
            if tmp.right:
                calSum(tmp.right, (num*10+tmp.right.val))

        calSum(root,root.val)

        return self.total