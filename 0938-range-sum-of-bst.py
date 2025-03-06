# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
   
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        
        result = 0
        
        def dfs(node):
            nonlocal result
            if node is None:
                return 
            
            if low <= node.val <= high:
                result += node.val
                dfs(node.left)
                dfs(node.right)
            elif node.val > high:
                dfs(node.left)
            elif node.val < low:
                dfs(node.right)
        
        dfs(root)
        return result