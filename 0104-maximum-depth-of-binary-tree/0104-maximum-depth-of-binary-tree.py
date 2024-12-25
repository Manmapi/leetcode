# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        depth = 0
        nodes = [root]
        while nodes:
            depth += 1
            for i in range(len(nodes)):
                value = nodes.pop(0)
                if value.left:
                    nodes.append(value.left)
                if value.right:
                    nodes.append(value.right)
        return depth

        