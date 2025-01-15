class Solution:
    def mySqrt(self, x: int) -> int:
        i = 1
        while True:
            if i ** 2 > x:
                return i - 1
            i += 1