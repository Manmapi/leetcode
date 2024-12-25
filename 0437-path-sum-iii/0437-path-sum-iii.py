# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        count = 0
        def dfs(node):
            if not node: return []
            next_val = dfs(node.left) + dfs(node.right)
            next_val = [x + node.val for x in next_val]
            next_val.append(node.val)
            for val in next_val:
                if val == targetSum:
                    nonlocal count
                    count += 1
            
            return next_val
        dfs(root)
        return count