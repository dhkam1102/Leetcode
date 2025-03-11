# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        result = []
        q = deque()
        q.append(root)

        while q:
            level = []
            for i in range(len(q)):
                current = q.popleft()
                if current:
                    level.append(current.val)
                    q.append(current.left)
                    q.append(current.right)

            if level:
                result.append(level)
        
        return_result = []
        for i in result:
            return_result.append(i[-1])
        
        return return_result