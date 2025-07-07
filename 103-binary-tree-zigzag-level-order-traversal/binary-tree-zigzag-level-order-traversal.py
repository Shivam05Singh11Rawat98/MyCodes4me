# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []        
        q = []
        q.append(root)
        res = [[root.val]]
        flag=0
        while q:
            n=len(q)
            lvl=[]
            for _ in range(n):
                temp=q.pop(0)

                if temp.left:
                    q.append(temp.left)
                    lvl.append(temp.left.val)
                
                if temp.right:
                    q.append(temp.right)
                    lvl.append(temp.right.val)
            if lvl:
                res.append(lvl if flag==1 else lvl[::-1])
            flag^=1
        
        return res
