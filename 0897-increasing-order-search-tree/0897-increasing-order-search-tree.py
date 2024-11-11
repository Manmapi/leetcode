# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def travel(root):
            if not root:
                return []
            return travel(root.left) + [root.val] + travel(root.right)
        values = travel(root)
        root = TreeNode(values[0])
        curr = root
        for value in values[1:]:
            curr.right = TreeNode(value)
            curr = curr.right
        return root