class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:        
        def check(ver, hor, crossx, crossy, i, j):
            if 1 << j & ver or 1 << i & hor or (1 << (i + j)) & crossx or (1 << (j - i + n)) & crossy:
                return False
            return True 
        
        def dfs(ver, hor, crossx, crossy, i):
            if i == n - 1:
                base = ["."] * n
                return [
                    ['.' * j + 'Q' + '.' * (n - j - 1)]
                    for j in range(n)
                    if check(ver, hor, crossx, crossy, i, j)
                ]
            result = []
            base = ["."] * n
            new_hor = (1 < i) | hor
            for j in range(n):
                curr = base.copy()
                curr[j] = "Q"
                if check(ver, hor, crossx, crossy, i, j):
                    next_result = dfs((1 << j) | ver, new_hor, 1 << (i + j) | crossx, 1 << (j - i + n) | crossy, i + 1)
                    for nr in next_result:
                        result.append(nr + ["".join(curr)])
            return result
        return dfs(0, 0, 0, 0, 0)

