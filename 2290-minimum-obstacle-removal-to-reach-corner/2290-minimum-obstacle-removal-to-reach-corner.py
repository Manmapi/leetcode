class Solution:
    def minimumObstacles(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        cost = [[float("inf")] * m for _ in range(n)]
        cost[0][0] = 0
        q = set([(0, 0)])
        while q:
            q_new = set()
            for i, j in q:
                value = cost[i][j]
                if i != 0 and value + grid[i - 1][j] < cost[i - 1][j]:
                    cost[i - 1][j] = value + grid[i - 1][j]
                    q_new.add((i - 1, j))
                if i != n - 1 and value + grid[i + 1][j] < cost[i + 1][j]:
                    cost[i + 1][j] = value + grid[i + 1][j]
                    q_new.add((i + 1, j))
                if j != 0 and value + grid[i][j - 1] < cost[i][j - 1]:
                    cost[i][j - 1] = value + grid[i][j - 1]
                    q_new.add((i, j - 1))
                if j != m - 1 and value + grid[i][j + 1] < cost[i][j + 1]:
                    cost[i][j + 1] = value + grid[i][j + 1]
                    q_new.add((i, j + 1))
            q = q_new
        return cost[-1][-1]
