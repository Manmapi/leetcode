class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:        
        def check(ver, crossx, crossy, i, j):
            return not (1 << j & ver or (1 << (i + j)) & crossx or (1 << (j - i + n)) & crossy)
                
        def dfs(ver, crossx, crossy, i):
            if i == n - 1: 
                return [
                    ['.' * j + 'Q' + '.' * (n - j - 1)] for j in range(n)
                    if check(ver, crossx, crossy, i, j)
                ]
            result = []
            for j in range(n):
                if check(ver, crossx, crossy, i, j):
                    next_result = dfs((1 << j) | ver, 1 << (i + j) | crossx, 1 << (j - i + n) | crossy, i + 1)
                    for nr in next_result:
                        result.append(nr + ['.' * j + 'Q' + '.' * (n - j - 1)])
            return result
        return dfs(0, 0, 0, 0)
    def totalNQueens(self, n: int) -> int:
        return len(self.solveNQueens(n))
        
        