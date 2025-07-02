# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        self.idx = -1
        inOrd = {v:i for i,v in enumerate(inorder)}

        def buildTreeUtil(left,right):
            if left>right:
                return None
            print(self.idx)
            val = postorder[self.idx]
            root = TreeNode(val)
            self.idx-=1

            index = inOrd[val]

            root.right = buildTreeUtil(index+1, right)
            root.left = buildTreeUtil(left,index-1)

            return root

        return buildTreeUtil(0,len(postorder)-1)