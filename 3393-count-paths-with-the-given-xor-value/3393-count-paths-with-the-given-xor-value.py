MOD = 1_000_000_007
class Solution:
    def countPathsWithXorValue(self, grid: List[List[int]], k: int) -> int:
        n = len(grid)
        m = len(grid[0])
        @lru_cache(None)
        def dp(i, j, value):
            if i > n - 1 or j > m - 1:
                return 0
            new_value = value  ^ grid[i][j]
            if i == n - 1 and j == m - 1:
                if new_value == k:
                    return 1
                else:
                    return 0
            return (dp(i + 1, j, new_value) + dp(i, j + 1, new_value)) % MOD
        return (dp(0, 1, grid[0][0]) + dp(1, 0, grid[0][0])) % MOD