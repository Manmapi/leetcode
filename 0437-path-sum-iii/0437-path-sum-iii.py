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
            next_val.append(0)
            next_result = []
            for val in next_val:
                value = val + node.val 
                if value  == targetSum:
                    nonlocal count
                    count += 1
                next_result.append(value)
    
            return next_result
        dfs(root)
        return count