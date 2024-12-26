class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        not_have = 0
        have = -prices[0]
        for price in prices:
            tmp_not_have = not_have
            not_have = max(not_have, have + price - fee)
            have = max(have, tmp_not_have - price)
        return not_have
