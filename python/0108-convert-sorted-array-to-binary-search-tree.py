# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        
        def make_tree(left, right):
            if left > right:
                return None
            mid = (left + right) // 2
            root = TreeNode(nums[mid], None, None)
            root.left = make_tree(left, mid - 1)
            root.right = make_tree(mid + 1, right)
            return root
        
        if not nums:
            return None
        
        left, right = 0, len(nums) -1 
        return make_tree(left, right)

        