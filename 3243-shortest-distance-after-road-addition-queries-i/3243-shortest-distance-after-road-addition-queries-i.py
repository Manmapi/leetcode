class Solution:
    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        edge_map = {i: [i +1] if i != n - 1 else [] for i in range(n)}
        def bfs():
            q = deque()
            q.append(0)
            visited = set()
            dist = 0
            while q:                
                q_new = []
                for node in q:
                    visited.add(node)
                    if node == n -1:
                        return dist
                    next_nodes = edge_map[node]
                    for next_node in next_nodes:
                        if next_node not in visited:
                            q_new.append(next_node)
                dist += 1
                q = q_new
        result = []
        for x, y in queries:
            edge_map[x].append(y)
            result.append(bfs())
        return result
        

            