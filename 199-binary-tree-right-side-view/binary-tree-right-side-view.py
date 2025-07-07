# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        que = []
        res = []
        que.append(root)        
        while que:
            n=len(que)
            print(n)
            res.append(que[0].val)
            for i in range(n):
                tmp=que.pop(0)
                if tmp.right:
                    que.append(tmp.right)
                if tmp.left:
                    que.append(tmp.left)
        
        return res