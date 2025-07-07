# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        que = []
        que.append(root)
        res=[[root.val]]
        while que:
            n=len(que)
            lvl=[]
            for _ in range(n):
                temp=que.pop(0)
                
                if temp.left:
                    que.append(temp.left)
                    lvl.append(temp.left.val)
                if temp.right:
                    que.append(temp.right)
                    lvl.append(temp.right.val)
            if lvl:
                res.append(lvl)
        
        return res