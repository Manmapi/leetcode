class Solution:
    def minimumTime(self, grid: List[List[int]]) -> int:
        if grid[0][1] > 1 and grid[1][0] > 1:
            return -1
        # Using dijktra 
        m = len(grid)
        n = len(grid[0])
        dist = [[float("inf")] * n for _ in range(m)]
        dist[0][0] = 0
        q = [(0, 0, 0)]
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        while q:
            distance, x, y = heapq.heappop(q)
            if x == m - 1 and y == n - 1:
                return distance
            for dx, dy in directions:
                if x + dx < 0 or x + dx >= m or y + dy < 0 or y + dy >= n:
                    continue
                cost = distance + 1
                if grid[x + dx][y + dy] > cost:
                    if (grid[x + dx][y + dy] - cost) % 2:
                        cost = grid[x + dx][y + dy] + 1
                    else:
                        cost = grid[x + dx][y + dy]
                if dist[x + dx][y + dy] > cost:
                    dist[x + dx][y + dy] = cost
                    heapq.heappush(q, (cost, x + dx, y + dy))
