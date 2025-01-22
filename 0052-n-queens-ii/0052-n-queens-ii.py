class Solution:
    def totalNQueens(self, n: int) -> int:
        def check(ver, crossx, crossy, i, j):
            return not (1 << j & ver or (1 << (i + j)) & crossx or (1 << (j - i + n)) & crossy)

        @cache  
        def dfs(ver, crossx, crossy, i):
            if i == n - 1: 
                return sum([
                    1 for j in range(n) if check(ver, crossx, crossy, i, j)
                ])
            result = 0
            for j in range(n):
                if check(ver, crossx, crossy, i, j):
                    result += dfs((1 << j) | ver, 1 << (i + j) | crossx, 1 << (j - i + n) | crossy, i + 1)
            return result
        return dfs(0, 0, 0, 0)
        