# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def same(root, subroot):
            if root is None and subroot is None:
                return True
            if not root or not subroot:
                return False
            if root.val != subroot.val:
                return False

            left = same(root.left, subroot.left)
            right = same(root.right, subroot.right)
            return left and right

        if not subRoot: return True
        if not root: return False

        if same(root, subRoot):
            return True

        left = self.isSubtree(root.left, subRoot)
        right = self.isSubtree(root.right, subRoot)

        return left or right