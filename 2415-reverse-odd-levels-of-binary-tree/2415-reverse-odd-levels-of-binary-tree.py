# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # Using BFS to travel
        curr = 0
        q = [root]
        while q:
            child = []
            # There is no child
            if not q[0].left:
                break
            for node in q:
                child.append(node.left)
                child.append(node.right)
            n = len(q)
            child = child[::-1]
            for i in range(n):
                if not curr:
                    q[i].left = child[2 * i]
                    q[i].right = child[2 * i  + 1]
                else: 
                    q[i].left = child[2 * i + 1]
                    q[i].right = child[2 * i]
            q = child
            curr ^= 1
        return root