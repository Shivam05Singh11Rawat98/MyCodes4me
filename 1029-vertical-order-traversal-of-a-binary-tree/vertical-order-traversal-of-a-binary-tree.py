# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        value_map = defaultdict(list)
        self.min_col,self.max_col=0,0
        def dfs(node,r,c):
            if not node:
                return
            self.min_col = min(self.min_col,c)
            self.max_col = max(self.max_col,c)
            heappush(value_map[c],(r,node.val))
            dfs(node.left,r+1,c-1)
            dfs(node.right,r+1,c+1)
        dfs(root,0,0)
        result=[]
        for i in range(self.min_col, self.max_col+1):
            temp = []
            while value_map[i]:
                row,val = heappop(value_map[i])
                temp.append(val)
            result.append(temp)
        
        return result
