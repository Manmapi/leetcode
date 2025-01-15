class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 1 :
            return x
        upper = x
        lower = 0
        while upper > lower + 1:
            half = (upper - lower) // 2 + lower 
            if half*half == x :
                return half
            if half*half > x:
                upper = half
            else:
                lower = half
        return lower
