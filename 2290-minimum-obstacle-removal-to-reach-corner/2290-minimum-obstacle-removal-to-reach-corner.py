class Solution:
    def minimumObstacles(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        vertex = defaultdict(list)
        for i in range(n):
            for j in range(m):
                if i != 0:
                    vertex[(i, j)].append([(i - 1, j), grid[i - 1][j]])    
                if i != n - 1:
                    vertex[(i, j)].append([(i + 1, j), grid[i + 1][j]])
                if j != 0:
                    vertex[(i, j)].append([(i, j - 1), grid[i][j - 1]])
                if j != m - 1:
                    vertex[(i, j)].append([(i, j + 1), grid[i][j + 1]])
        cost = [[float("inf")] * m for _ in range(n)]
        cost[0][0] = 0
        q = [[0, (0,0)]]
        while q:
            value, point = heapq.heappop(q)
            for p, c in vertex[point]:
                i, j = p
                if cost[i][j] > value + c:
                    cost[i][j] = value + c
                    heapq.heappush(q, [value + c, p])
       
        return cost[-1][-1]
