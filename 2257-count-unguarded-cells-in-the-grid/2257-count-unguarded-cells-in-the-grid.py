class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        grid = [[0] * n for _ in range(m)]
        for i, j in walls:
            grid[i][j] = 2
        for i, j in guards:
            grid[i][j] = 2
        for i, j in guards:
            x = i
            while x > 0:
                x -= 1
                if grid[x][j] == 2:
                    break
                grid[x][j] = 1
            x = i
            while x < m - 1:
                x += 1
                if grid[x][j] == 2:
                    break
                grid[x][j] = 1
            y = j
            while y > 0:
                y -= 1
                if grid[i][y] == 2:
                    break
                grid[i][y] = 1
            y = j
            while y < n - 1:
                y += 1
                if grid[i][y] == 2:
                    break
                grid[i][y] = 1
        result = 0
        for r in grid:
            result += r.count(0)
        return result