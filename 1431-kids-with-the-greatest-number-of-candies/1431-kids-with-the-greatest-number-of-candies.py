class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_ = max(candies)
        return [
            c + extraCandies >= max_
            for c in candies
        ]