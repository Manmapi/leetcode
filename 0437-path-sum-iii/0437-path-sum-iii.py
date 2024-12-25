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
            nonlocal count
            next_result = []
            for val in dfs(node.left):
                value = val + node.val 
                if value  == targetSum:
                    count += 1
                next_result.append(value)
            for val in dfs(node.right):
                value = val + node.val 
                if value  == targetSum:
                    count += 1
                next_result.append(value)
            if node.val == targetSum:
                count += 1
            next_result.append(node.val)
            return next_result
        dfs(root)
        return count