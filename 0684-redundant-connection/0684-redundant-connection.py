class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        ids = [i for i in range(n)]
        sizes = [1] * n

        def root(x):
            while ids[x] != x:
                x = ids[x]
            return x
        for x, y in edges:
            x -= 1
            y -= 1
            root_x = root(x)
            root_y = root(y)
            if root_x == root_y:
                return (x + 1, y + 1)
            if sizes[root_x] >= sizes[root_y]:
                ids[root_y] = root_x
                sizes[root_x] += sizes[root_y]
            else:
                ids[root_x] = root_y
                sizes[root_y] += sizes[root_x]