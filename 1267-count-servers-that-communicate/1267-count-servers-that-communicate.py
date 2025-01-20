class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        ver = [0] * m
        hor = [0] * n
        for i in range(n):
            for j in range(m):
                if grid[i][j]:
                    ver[j] += 1
                    hor[i] += 1
        result = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j]:
                    if ver[j] > 1 or hor[i] > 1:
                        result += 1
        return result