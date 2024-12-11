def binpow(a, b):
    if b == 0:
        return 1
    val = binpow(a, b // 2)
    result = val * val
    if b % 2:
        result *= a
    return result

class Solution:
    def myPow(self, x: float, n: int) -> float:
        val = binpow(x, abs(n))
        if n < 0:
            return 1 / val
        return val