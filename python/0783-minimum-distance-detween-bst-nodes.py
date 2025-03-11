# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        result = float("inf")
        prev = None

        def dfs(root):
            nonlocal result, prev

            if root is None:
                return
            
            dfs(root.left)

            if prev:
                result = min(result, abs(root.val - prev.val))
            prev = root

            dfs(root.right)
        
        dfs(root)
        return result