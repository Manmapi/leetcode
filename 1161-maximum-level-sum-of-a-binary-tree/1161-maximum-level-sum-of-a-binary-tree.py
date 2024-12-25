# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        q = [root]
        max_value = float('-inf')
        level = 0
        i = 0
        while q:
            q_new = []
            i += 1
            current_max = 0
            for node in q:
                current_max += node.val
                if node.left:
                    q_new.append(node.left)
                if node.right:
                    q_new.append(node.right)
            q = q_new
            if current_max > max_value:
                max_value = current_max
                level = i
        return level