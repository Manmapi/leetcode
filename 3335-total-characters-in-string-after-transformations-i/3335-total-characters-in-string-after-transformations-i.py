MOD = 1_000_000_007
class Solution:
    def lengthAfterTransformations(self, s: str, t: int) -> int:
        m = [0] * 26
        base = ord('a')
        for c in s:
            m[ord(c) - base] += 1
        for i in range(t):
            tmp = m[25]
            for i in range(25, 0, -1):
                m[i] = m[i - 1]
            m[0] = tmp
            m[1] += tmp
        return sum(m) % MOD