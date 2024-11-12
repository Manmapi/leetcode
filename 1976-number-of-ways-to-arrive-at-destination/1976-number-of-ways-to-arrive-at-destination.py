class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        MOD = 1_000_000_007
        # Using dijkstra to find min diff
        vertexs = {i: [] for i in range(n)}
        for x, y, time in roads:
            vertexs[x].append((y, time))
            vertexs[y].append((x, time))
        dist_array = [float('inf')] * n
        dist_array[0] = 0
        q = [(0, 0)]
        min_dist = float('inf')
        while q:
            dist, index = heapq.heappop(q)
            if index == n - 1:
                min_dist = dist 
                break
            for x, cost in vertexs[index]:
                if dist + cost < dist_array[x]:
                    dist_array[x] = dist + cost
                    heapq.heappush(q, (dist + cost, x))
        # Using BFS to count way
        dist = [-1] * n
        dist[0] = min_dist
        @lru_cache(None)
        def bfs(index, target):
            result = 0
            if index == n - 1:
                return 1
            for x, cost in vertexs[index]:
                if cost > target:
                    continue
                if target - cost >= dist[x]:
                    dist[x] = target - cost
                    result += bfs(x, dist[x])
            return result % MOD
        return bfs(0, min_dist)