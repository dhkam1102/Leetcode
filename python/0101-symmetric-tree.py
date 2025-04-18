# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def ismirror(left, right):
            if not left and not right:
                return True
            if not left or not right:
                return False
            
            return left.val == right.val and ismirror(left.left, right.right) and ismirror(left.right, right.left)
        
        if root is None:
            return False
        return ismirror(root.left, root.right)
        