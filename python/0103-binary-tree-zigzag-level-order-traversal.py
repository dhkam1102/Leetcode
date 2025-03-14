# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []
        q = deque()
        q.append(root)
        order = True

        while q:
            level = []
            for i in range(len(q)):
                current = q.popleft()
                if current:
                    level.append(current.val)
                    q.append(current.left)
                    q.append(current.right)

            if level:
                if order:
                    result.append(level)
                    order = False
                    continue

                result.append(level[::-1])
                order = True
        return result




# Same neetcode solution but more clever

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        q = deque([root] if root else [])
        while q:
            level = []
            for i in range(len(q)):
                node = q.popleft()
                level.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            if len(res) % 2:
                level.reverse()
            res.append(level)
        return res