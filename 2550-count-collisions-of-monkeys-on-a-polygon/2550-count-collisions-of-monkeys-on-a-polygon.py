MOD = 1_000_000_007
lru_cache(None)
def power(b):
    if b == 0:
        return 1
    if b == 1:
        return 2
    k = b // 2
    if b % 2:
        extra = 2
    else:
        extra = 1
    res = power(k)
    return (res * res * extra) % MOD

class Solution:
    def monkeyMove(self, n: int) -> int:
        n %= 500000003
        k = n // 500000003
        val = power(n) 
        if k % 2:
            val = MOD - val
        return val - 2