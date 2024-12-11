MOD = 1_000_000_007
def binpow(a, b):
    if b == 0:
        return 1
    val = binpow(a, b // 2)
    result = val * val
    if b % 2:
        result *= a
    return result % MOD

class Solution:
    def countGoodNumbers(self, n: int) -> int:
        h = n // 2
        result = binpow(20, h) % MOD
        if n % 2:
            result *= 5
        return result % MOD