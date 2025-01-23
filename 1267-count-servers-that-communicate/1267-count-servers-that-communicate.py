class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        ver = [0] * m
        hor = [0] * n
        
        for i in range(n):
            for j in range(m):
                ver[j] += grid[i][j]
                hor[i] += grid[i][j]

        result = 0
        for i in range(n):
            for j in range(m):
                result += grid[i][j] and (ver[j] > 1 or hor[i] > 1)
        return result