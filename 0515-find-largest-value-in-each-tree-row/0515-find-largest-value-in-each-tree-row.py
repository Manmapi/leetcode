# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        curr_node = []
        if not root:
            return []
        curr_node.append(root)
        while curr_node:
            max_value = curr_node[0].val
            for _ in range(len(curr_node)):
                node = curr_node.pop(0)
                if node.val > max_value:
                    max_value = node.val
                if node.right:
                    curr_node.append(node.right)
                if node.left:
                    curr_node.append(node.left)
            result.append(max_value)
        return result
