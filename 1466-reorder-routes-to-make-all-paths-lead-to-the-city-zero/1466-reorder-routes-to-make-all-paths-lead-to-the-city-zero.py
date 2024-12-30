class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        edge_map = defaultdict(list)
        edge_set = set()
        for x, y in connections:
            edge_map[x].append(y)
            edge_map[y].append(x)
            edge_set.add((x, y))
        q = [0]
        visited = {0}
        result = 0
        while q:
            q_new = []
            for node in q:
                for next_node in edge_map[node]:
                    if next_node in visited:
                        continue
                    if (next_node, node) not in edge_set:
                        result += 1
                        edge_set.add((next_node, node))
                    visited.add(next_node)
                    q_new.append(next_node)
            q = q_new
        return result