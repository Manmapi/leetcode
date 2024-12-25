# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        def helper(max_value, node):
            if not node:
                return 0
            result = 0
            next_max = max(max_value, node.val)
            if max_value <= node.val:
                result += 1
            
            return result + helper(next_max, node.left) + helper(next_max, node.right)
        return helper(root.val, root.left) + helper(root.val, root.right) + 1
