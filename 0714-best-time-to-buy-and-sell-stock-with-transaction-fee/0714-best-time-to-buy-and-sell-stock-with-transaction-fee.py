class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        not_have = 0
        have = -prices[0]
        for price in prices:
            have = max(have, not_have - price)
            not_have = max(not_have, have + price - fee)
        return not_have
