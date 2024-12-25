# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        q = [root]
        result = []
        while q:
            result.append(q[-1].val)
            q_new = []
            for node in q:
                if node.left:
                    q_new.append(node.left)
                if node.right:
                    q_new.append(node.right)
            q = q_new
        return result
        