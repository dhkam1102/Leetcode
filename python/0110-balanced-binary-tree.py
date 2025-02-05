#----------------------------------------------------------------

#2 approaches

#1 Bruth force:
'''
run bfs start from the bottom on each left and right 
get their height and calc if its balanced.
Time: O(n^2) since were calcing the height for every node.
'''

#2 

'''
run bfs but return [height, balance] instead so you know imediatly
if the sub tree is not balanced and return false.
Time: O(n) since we dont have to calc the height every time
'''





#----------------------------------------------------------------

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        isBalanced = True

        def dfs(root):
            if root is None:
                return 0

            nonlocal isBalanced
            right = dfs(root.right)
            left = dfs(root.left)

            if abs(left - right) > 1:
                isBalanced = False

            return max(left, right) + 1
        
        dfs(root)
        return isBalanced
    


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(root):
            if root is None:
                return [0, True]

            left, right = dfs(root.left), dfs(root.right)
            balanced = abs(left[0] - right[0]) <= 1 and left[1] and right[1] 
            height = max(left[0], right[0]) + 1

            return [height, balanced]

        return dfs(root)[1]
