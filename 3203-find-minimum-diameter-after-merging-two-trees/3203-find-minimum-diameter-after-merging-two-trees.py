class Solution:
    def minimumDiameterAfterMerge(self, edges1: List[List[int]], edges2: List[List[int]]) -> int:
        edges_map1 = defaultdict(list)
        edges_map2 = defaultdict(list)
        
        for x, y in edges1:
            edges_map1[x].append(y)
            edges_map1[y].append(x)
        for x, y in edges2:
            edges_map2[x].append(y)
            edges_map2[y].append(x)
        def findDiameterOfTree(start, edge_map):
            # Using BFS 
            visited = set([start])
            depth = 0
            q = [start]
            last_node = start
            
            while q:
                q_new = []
                last_node = q[0]
                for node in q:
                    for next_node in edge_map[node]:
                        if next_node not in visited:
                            q_new.append(next_node)
                            visited.add(next_node)
                q = q_new
                depth += 1
            return depth - 1, last_node
    
        if len(edges1) == 0:
            diamter1 = 0
        else:
            _, end_left_1 = findDiameterOfTree(0, edges_map1)
            diamter1, _ = findDiameterOfTree(end_left_1, edges_map1)
        if len(edges2) == 0:
            diamter2 = 0
        else:
            _, end_left_2 = findDiameterOfTree(0, edges_map2)
            diamter2, _ = findDiameterOfTree(end_left_2, edges_map2)
        return max([ceil(diamter1  / 2) + ceil(diamter2 / 2) + 1, diamter1, diamter2])