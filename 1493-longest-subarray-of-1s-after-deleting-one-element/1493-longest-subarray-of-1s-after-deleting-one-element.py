class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        l = 0
        n = len(nums)
        x = None
        result = 0
        for i, num in enumerate(nums):
            if not num:
                if x is None:
                    x = i
                else:
                    result = max(result, i - l - 1)
                    l = x + 1
                    x = i
        result = max(n - l  - 1, result)
        return result