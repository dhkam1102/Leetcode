# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        left, right = 0, len(nums) - 1

        def maketree(left, right):
            if not left <= right:
                return None

            mid = (right + left) // 2
            root = TreeNode(nums[mid])
            root.left = maketree(left, mid - 1)
            root.right = maketree(mid + 1, right)

            return root

        return maketree(left, right)

        
        