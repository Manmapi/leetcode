class Solution:
    def highestPeak(self, grid: List[List[int]]) -> List[List[int]]:
        q = []
        n = len(grid)
        m = len(grid[0])
        for i in range(n):
            for j in range(m):
                if grid[i][j]:
                    q.append((i, j))
        result = [[0] * m for _ in range(n)]
        curr = 0
        visited = set(q)
        while q:
            q_new = []
            for x, y in q:
                result[x][y] = curr
                for i, j in {(1, 0), (0, 1), (-1, 0), (0, -1)}:
                    h = x + i
                    k = y + j
                    if h < 0 or h >= n or k < 0 or k >= m:
                        continue
                    if (h, k) not in visited:
                        visited.add((h, k))
                        q_new.append((h, k))
            curr += 1
            q = q_new
        return result