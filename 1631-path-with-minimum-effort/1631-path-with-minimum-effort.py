class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        vertex = defaultdict(list)
        n = len(heights)
        m = len(heights[0])
        for i in range(n):
            for j in range(m):
                if i != n - 1:
                    vertex[(i, j)].append((i + 1, j))
                if j != m - 1:
                    vertex[(i, j)].append((i, j + 1))
                if i != 0:
                    vertex[(i, j)].append((i - 1, j))
                if j != 0:
                    vertex[(i, j)].append((i, j - 1))
                    
        q = [(0, 0, 0)]
        dist = [[float('inf')] * m for _ in range(n)]
        dist[0][0] = 0
        visited = set([(0,0)])
        while q:
            weight, i, j = heapq.heappop(q)
            score = heights[i][j]
            # if i == n - 1 and j == m - 1:
            #     break
            for x, y in vertex[(i, j)]:
                val = max(weight, abs(score - heights[x][y]))
                if val < dist[x][y]:
                    dist[x][y] = val
                    # visited.add((x, y))
                    heapq.heappush(q, (val, x, y))
        print(dist)
        return dist[-1][-1]