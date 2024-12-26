class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        @cache
        def dp(value, index):
            if index == n:
                if value == target: 
                    return 1
                else:
                    return 0
            return dp(value - nums[index], index + 1) + dp(value + nums[index], index + 1)
        return dp(0, 0)