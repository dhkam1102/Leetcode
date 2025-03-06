# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        def dfs(root, target):
            if root is None:
                return False
            if target == root.val and root.left is None and root.right is None:
                return True
            
            left = dfs(root.left, target - root.val)
            right = dfs(root.right, target - root.val)
            
            return left or right
        
        return dfs(root, targetSum)