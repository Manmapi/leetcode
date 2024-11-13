class Solution:
    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        edge_map = {i: [i +1] if i != n - 1 else [] for i in range(n)}
        history_map = {}
        result = [n]

        def bfs(start):
            nonlocal history_map
            q = []
            if not history_map:
                dist = 0
                q.append(0)
            else:
                if history_map.get(start) is None or history_map[start] > result[-1]:
                    return result[-1]
                dist = history_map[start]
                for k, v in history_map.items():
                    if v == dist:
                        q.append(k)
            visited = set(q)
            while q:      
                q_new = []
                for node in q:
                    history_map[node] = min(dist, history_map.get(node, node))
                    
                    if node == n -1:
                        return dist
                    next_nodes = edge_map[node]
                    for next_node in next_nodes:
                        if next_node not in visited:
                            visited.add(next_node)
                            q_new.append(next_node)
                dist += 1
                q = q_new
            return result[-1]
        bfs(0)
        for x, y in queries:
            edge_map[x].append(y)
            if history_map[y] > history_map[x] + 1:
                result.append(bfs(x))
            else:
                result.append(result[-1])        
        return result[1:]
        