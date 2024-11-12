class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        # Dijkstra
        n = len(grid)
        n_2 = n ** 2
        vertexes = {
            i: [] for i in range(0, n_2)
        }
        for i in range(n):
            for j in range(n): 
                key = i * n + j
                points = []
                if i != 0:
                    points.append((key - n, grid[i - 1][j]))
                if i != n - 1:
                    points.append((key + n, grid[i + 1][j]))
                if j != 0:
                    points.append((key - 1, grid[i][j - 1]))
                if j != n - 1:
                    points.append((key + 1, grid[i][j + 1]))
                vertexes[key] = points
        # Distance, index
        dist = [(grid[0][0], 0)]
        visited = set()
        while dist:
            cost, index = heapq.heappop(dist)
            # i, j = index // n, index % n
            if index == n_2 - 1:
                return max(cost, grid[n - 1][n - 1])
            visited.add(index)
            for p, c in vertexes[index]:
                if p not in visited:
                    heapq.heappush(dist, (max(cost, c), p))
        return 0
        # 3 2 
        # 0 1