MOD = 1_000_000_007

class Solution:
    def countGoodStrings(self, low: int, high: int, x: int, y: int) -> int:
        @cache
        def dp(value):
            if value > high:
                return 0
            return ((value >= low) + dp(value + x) + dp(value + y)) % MOD
        return dp(0) 