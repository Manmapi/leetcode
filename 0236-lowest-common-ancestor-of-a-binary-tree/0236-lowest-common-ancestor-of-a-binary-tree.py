# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        result = None
        def dfs(node):
            if not node:
                return False, False
            x = False
            y = False
            if node.val == p.val:
                x = True
            if node.val == q.val:
                y = True
            x1, y1 = dfs(node.left)
            x2, y2 = dfs(node.right)
            x = x or x1 or x2
            y = y or y1 or y2
            if x and y:
                if (not ( x1 and y1 )) or (not( x2 and y2 )):
                    nonlocal result
                    if result is None:
                        result = node
            return x, y
        dfs(root)
        return result