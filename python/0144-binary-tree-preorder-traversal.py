class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        stack = []
        curr = root

        while curr or stack:
            while curr:
                result.append(curr.val)
                stack.append(curr.right)
                curr = curr.left
            curr = stack.pop()
        return result