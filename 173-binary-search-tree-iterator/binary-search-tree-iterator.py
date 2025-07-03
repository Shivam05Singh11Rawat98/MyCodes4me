# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.root=root
        self.inorder = []
        def DFS(temp):
            if not temp:
                return
            DFS(temp.left)
            self.inorder.append(temp.val)
            DFS(temp.right)
        DFS(root)
        self.idx=0

    def next(self) -> int:
        val = self.inorder[self.idx]
        self.idx+=1
        return val

    def hasNext(self) -> bool:
        return len(self.inorder)>self.idx


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()