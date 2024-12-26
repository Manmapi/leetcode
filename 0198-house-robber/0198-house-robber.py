class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        @cache
        def dp(money, index, flag):
            if index >= n:
                return 0
            if flag:
                return dp(money, index + 1, False)
            else:
                return max(
                    nums[index] + dp(money, index + 1, True),
                    dp(money, index + 1, False)
                )
        
        return dp(0, 0, False)