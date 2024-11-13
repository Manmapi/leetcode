class Solution:
    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        edge_map = {i: [i +1] if i != n - 1 else [] for i in range(n)}
        history = [i for i in range(n)]
        result = [n]
        def bfs(start, dist):
            q = [start]
            while q:      
                q_new = []
                for node in q:
                    history[node] = min(dist, history[node])
                    if node == n -1:
                        return dist
                    next_nodes = edge_map[node]
                    for next_node in next_nodes:
                        if history[next_node] > dist:                            
                            q_new.append(next_node)
                dist += 1
                q = q_new
            return result[-1]
        for x, y in queries:
            edge_map[x].append(y)
            if history[y] > history[x] + 1:
                result.append(bfs(y, history[x] + 1))
            else:
                result.append(result[-1])        
        return result[1:]