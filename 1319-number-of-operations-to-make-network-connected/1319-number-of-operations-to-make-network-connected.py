class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        if len(connections) < n - 1:
            return -1
        ids = [i for i in range(n)]
        size = [1] * n
        def root(k):
            while k != ids[k]:
                k = ids[k]
            return k
        for x, y in connections:
            root_x = root(x)
            root_y = root(y)
            if size[root_x] > size[root_y]:
                ids[root_y] = root_x 
                size[root_x] += size[root_y]
            else:
                ids[root_x] = root_y 
                size[root_y] += size[root_x]
        roots = [root(i) for i in range(n)]
        return len(set(roots)) - 1