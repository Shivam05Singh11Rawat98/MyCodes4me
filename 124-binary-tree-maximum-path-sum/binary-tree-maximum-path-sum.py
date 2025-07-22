# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.maxSum=-math.inf
        def dfs(root):
            if not root:
                return -math.inf           
            leftSum=dfs(root.left)
            rightSum=dfs(root.right)
            temp_sum = max(root.val, root.val+rightSum, root.val+leftSum)
            temp_ans=max(temp_sum,leftSum,rightSum,root.val+rightSum+leftSum)
            self.maxSum = max(temp_ans,self.maxSum)
            return temp_sum
        dfs(root)
        return self.maxSum


"""
root.val+root.leftsum+rightsum
max(root.val,root.val+root.leftsum+rightsum,rightsum,leftsum)
"""