class Solution:
    def countBits(self, n: int) -> List[int]:
        def countbit(n):
            result = 0
            while n :   
                result += n & 1
                n >>= 1
            return result
        return [countbit(i) for i in range(n + 1)]