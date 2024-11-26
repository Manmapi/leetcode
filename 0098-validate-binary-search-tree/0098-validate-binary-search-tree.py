# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def travel(node):
            if not node:
                return []
            return travel(node.left) + [node.val] + travel(node.right)
        values = travel(root)
        n = len(values)
        for i in range(1, n):
            if values[i] <= values[i - 1]:
                return False
        return True