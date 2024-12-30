class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def possible(k):
            return sum([ceil(x / k) for x in piles]) <= h
        l, r = 1, max(piles)
        while l <= r:
            mid = (l + r) // 2
            if possible(mid):
                r = mid - 1
            else:
                l = mid + 1
        return l