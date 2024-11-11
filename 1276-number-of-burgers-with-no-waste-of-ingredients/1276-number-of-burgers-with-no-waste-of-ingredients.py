class Solution:
    def numOfBurgers(self, tomatoSlices: int, cheeseSlices: int) -> List[int]:
        # 4x  + 2y = k
        # x + y = h
        # 4x + 2(h - x) = k
        # 2x = (k - 2h) // 2
        if tomatoSlices % 2:
            return []
        jumbo = (tomatoSlices - 2*cheeseSlices) // 2
        if jumbo < 0 or jumbo > cheeseSlices:
            return []
        else:
            return [jumbo, cheeseSlices - jumbo]