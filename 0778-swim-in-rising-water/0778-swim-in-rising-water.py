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
                    points.append((i - 1, j))
                if i != n - 1:
                    points.append((i + 1, j))
                if j != 0:
                    points.append((i, j - 1))
                if j != n - 1:
                    points.append((i, j + 1))
                vertexes[(i, j)] = points
        # Distance, index
        dist = [(grid[0][0], 0, 0)]
        visited = set((0, 0))
        while dist:
            cost, i, j = heapq.heappop(dist)
            # i, j = index // n, index % n
            if i == n -1 and j == n - 1:
                return cost
            visited.add(index)
            for x, y in vertexes[(i, j)]:
                if (x, y) not in visited:
                    heapq.heappush(dist, (max(cost, grid[x][y]), x, y))
                    visited.add((x, y))