class Solution:
    def waysToReachStair(self, k: int) -> int:
        @cache
        def dp(current, power):
            if current > k + 1:
                return 0
            result = 0
            if current == k:
                result += 1
            if current == k + 1:
                result += 1
            result += dp(current + 2 ** power, power + 1)
            result += dp(current - 1 + 2 ** power, power + 1)
            return result
        return dp(1, 0)
