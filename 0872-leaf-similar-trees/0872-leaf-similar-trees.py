# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        leaves1 = []
        q = [root1]
        while q:
            node = q.pop()
            if node.left:
                q.append(node.left)
            if not node.left and not node.right:
                leaves1.append(node.val)
            if node.right:
                q.append(node.right)
        
        leaves2 = []
        q = [root2]
        while q:
            node = q.pop()
            if node.left:
                q.append(node.left)
            if not node.left and not node.right:
                leaves2.append(node.val)
            if node.right:
                q.append(node.right)
        if len(leaves1) != len(leaves2):
            return False
        return all([x == y for x, y in zip(leaves1, leaves2)])