class Solution:
    def countBits(self, n: int) -> List[int]:
        @cache
        def countbit(n):
            if n == 0:
                return 0
            return (n & 1) + countbit(n >> 1)
        return [countbit(i) for i in range(n + 1)]
        # return []