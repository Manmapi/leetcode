class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        # Dijkstra
        n = len(grid)
        n_2 = n ** 2
        edges = []
        max_ = 0
        vals = []
        for i in range(n):
            for j in range(n): 
                key = i * n + j
                max_ = max(grid[i][j], max_)
                vals.append(grid[i][j])
                val = grid[i][j]
                if i != 0:
                    edges.append((key, key - n, max(val, grid[i - 1][j])))
                if i != n - 1:
                    edges.append((key, key + n, max(val, grid[i + 1][j])))
                if j != 0:
                    edges.append((key, key - 1, max(val, grid[i][j - 1])))
                if j != n - 1:
                    edges.append((key, key + 1, max(val, grid[i][j + 1])))
        vals.sort()
        def union_find(k):
            ids = [i for i in range(n_2)]
            size = [1] * n_2
            def root(n):
                while n != ids[n]:
                    n = ids[n]
                return n
            for first, second, cost in edges:
                if cost > k:
                    continue
                root_first = root(first)
                root_second = root(second)
                if size[root_second] > size[root_first]:
                    ids[root_first] = root_second
                    size[root_second] = size[root_second] + size[root_first]
                else:
                    ids[root_second] = root_first
                    size[root_first] = size[root_first] + size[root_second]
            return root(0) == root(n_2 - 1)
        # BS
        l, r = 0, n_2 - 1
        while l <= r:
            mid = (l + r) // 2
            if union_find(vals[mid]):
                r = mid - 1
            else:
                l = mid + 1
        # print(union_find(10), union_find(11))
        # print(vals)
        # print(l)
        return (vals[l])