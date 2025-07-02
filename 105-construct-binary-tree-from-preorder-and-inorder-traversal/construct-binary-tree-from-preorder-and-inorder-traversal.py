# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.idx=0
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if self.idx == len(preorder):
            return None
        val=preorder[self.idx]
        root = TreeNode(val)
        i=0
        while i<len(inorder):
            if inorder[i]==val:
                self.idx+=1
                root.left = self.buildTree(preorder,inorder[:i])
                root.right = self.buildTree(preorder,inorder[i:])
                return root
            i+=1

        return None 

