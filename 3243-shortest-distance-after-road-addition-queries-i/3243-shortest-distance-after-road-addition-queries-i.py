class Solution:
    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        # table = [[0] * n for _ in range(n)]
        # for i in range(n - 1):
        #     table[i][i + 1] = 1
        # for x, y in queries:
        #     table[x][y] = 1
        edge_map = {i: [i +1] if i != n - 1 else [] for i in range(n)}
        # @lru_cache(None)
        def bfs():
            q = deque()
            q.append([0, 0])
            visited = set()
            while q:
                q_new = []
                for node, dist in q:
                    visited.add(node)
                    if node == n -1:
                        return dist
                    next_nodes = edge_map[node]
                    for next_node in next_nodes:
                        if next_node not in visited:
                            q_new.append([next_node, dist + 1])
                q = q_new
        result = []
        for x, y in queries:
            edge_map[x].append(y)
            result.append(bfs())
        return result
        

            