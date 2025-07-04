# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        """
        if(root==nullptr) return nullptr;
        if(root==p|| root==q) return root;
        TreeNode* left=lowestCommonAncestor(root->left, p, q);
        TreeNode* right=lowestCommonAncestor(root->right, p, q);
        if(left && right){
            return root;
        }
        return left!=nullptr?left:right;
        """

        if not root:
            return root
        if root==p or root==q:
            return root
        left = self.lowestCommonAncestor(root.left, p,q)
        right = self.lowestCommonAncestor(root.right, p,q)

        if left and right:
            return root

        return left if left else right