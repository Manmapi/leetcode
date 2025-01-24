class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        visited = dict()
        @cache
        def dfs(node):
            if node in visited:
                return visited[node]
            visited[node] = True
            for n in graph[node]:
                if dfs(n):
                    return True
            visited[node] = False
        return [x for x in range(n) if not dfs(x)]
