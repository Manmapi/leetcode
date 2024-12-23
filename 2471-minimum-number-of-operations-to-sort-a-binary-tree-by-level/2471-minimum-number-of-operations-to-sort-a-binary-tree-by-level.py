# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minimumOperations(self, root: Optional[TreeNode]) -> int:
        result = 0
        level = [root]
        while level:
            nums = []
            new_level = []
            for node in level:
                if node is None:
                    continue
                nums.append(node.val)
                new_level.append(node.left)
                new_level.append(node.right)
            result += self.minimum_ops(nums)
            level = new_level
        return result


    def minimum_ops(self, nums):
        n = len(nums)
        sorted_num = [*enumerate(nums)]
        sorted_num.sort(key=lambda x: x[1])
        visited = set()
        result = 0
        for i in range(n):
            if nums[i] == sorted_num[i][1]:
                continue
            cycle_count = 1
            curr = i
            while curr not in visited and nums[curr] != sorted_num[curr][1]:
                visited.add(curr)
                curr = sorted_num[curr][0]
                if curr not in visited:
                    cycle_count += 1
            result += cycle_count - 1
        return result
