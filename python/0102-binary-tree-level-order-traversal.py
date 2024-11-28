# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q = deque()
        q.append(root)
        result = []
        while q:
            level = []
            for i in range(len(q)):
                current = q.popleft()
                if current is not None:
                    q.append(current.left)
                    q.append(current.right)
                    level.append(current.val)
            if level:
                result.append(level)
        return result
                        
        