class Solution:
    def findAnswer(self, n: int, edges: List[List[int]]) -> List[bool]:
        MOD = 1_000_000_007
        # Using dijkstra to find min diff
        vertexs = {i: [] for i in range(n)}
        for x, y, time in edges:
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
        if min_dist == float("inf"):
            return [False] * len(edges)
        edge_map = defaultdict(lambda: False)
        dist = [-1] * n
        dist[0] = min_dist
        # Using DFS to check
        @cache
        def dfs(index, target):
            if index == n - 1:
                return True
            result = False
            for x, cost in vertexs[index]:
                if target < cost:
                    continue
                if target - cost >= dist[x]:
                    dist[x] = target - cost
                    val = dfs(x, dist[x])
                    if val:
                        result = True
                        edge_map[(index, x)] = True
                        edge_map[(x, index)] = True
            return result

        val = dfs(0, min_dist)
        return [edge_map[(x, y)] for x, y, _ in edges]