class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:        
        def check(ver, hor, crossx, crossy, i, j):
            nonlocal n
            if 1 << j & ver:
                return False
            if 1 << i & hor:
                return False
            if (1 << (i + j)) & crossx:
                return False
            if (1 << (j - i + n)) & crossy:
                return False
            return True 
        
        @cache
        def dfs(ver, hor, crossx, crossy, i):
            nonlocal n
            result = []
            base = ["."] * n
            new_hor = (1 < i) | hor
            for j in range(n):
                curr = base.copy()
                curr[j] = "Q"
                if check(ver, hor, crossx, crossy, i, j):
                    if i == n - 1:
                        result.append(["".join(curr)])
                    else: 
                        next_result = dfs((1 << j) | ver, new_hor, 1 << (i + j) | crossx, 1 << (j - i + n) | crossy, i + 1)
                        for nr in next_result:
                            result.append(nr + ["".join(curr)])
            return result
        return dfs(0, 0, 0, 0, 0)

