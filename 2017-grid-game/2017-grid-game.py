class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        n = len(grid[0])
        result = float('inf')
        up = 0
        down = 0
        up =  sum(grid[0])
        for i in range(n):
            if i > 0:
                down += grid[1][i - 1]
            up -= grid[0][i]
            result = min(result, max(up, down))
        return result