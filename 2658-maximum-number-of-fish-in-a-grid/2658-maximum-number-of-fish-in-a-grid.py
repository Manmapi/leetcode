class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        vertexes = []
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 0:
                    continue
                # Right
                if j < m - 1:
                    if grid[i][j + 1] > 0:
                        vertexes.append((i * m + j, i * m + j + 1))
                # Down
                if i < n - 1:
                    if grid[i + 1][j] > 0:
                        vertexes.append((i * m + j, i * m + j + m))
        ids = [i for i in range(m * n)]
        sizes = [1] * (m * n)

        def root(x):
            while ids[x] != x:
                x = ids[x]
            return x
        for x, y in vertexes:
            root_x = root(x)
            root_y = root(y)
            if sizes[root_x] >= sizes[root_y]:
                ids[root_y] = root_x
                sizes[root_x] += sizes[root_y]
            else:
                ids[root_x] = root_y
                sizes[root_y] += sizes[root_x]
        roots = [root(x) for x in range(m * n)]
        map_ = defaultdict(int)
        for i, root in enumerate(roots):
            x = i // m
            y = i % m
            map_[root] += grid[x][y]
        return max(map_.values())
        