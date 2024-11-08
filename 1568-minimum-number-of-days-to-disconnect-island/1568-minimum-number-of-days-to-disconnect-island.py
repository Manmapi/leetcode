class Solution:
    def minDays(self, grid: List[List[int]]) -> int:
        edges = []
        count_one = 0
        row = len(grid)
        col = len(grid[0])
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1:
                    count_one += 1
                    if i < row - 1 and grid[i + 1][j]:
                        edges.append([i * col + j, (i + 1)*col + j])
                    if j < col - 1 and grid[i][j + 1]:
                        edges.append([i * col + j, i*col + j + 1])
        if count_one == 1:
            return 1
        size = [1] * (row*col)
        ids = [i for i in range(row*col)]
        def root(n):
            while n != ids[n]:
                n = ids[n]
            return n
        edge_map = dict()
        for edge in edges:
            l, r = edge
            edge_map.setdefault(l, [])
            edge_map[l].append(r)
            edge_map.setdefault(r, [])
            edge_map[r].append(l)
            l_root = root(l)
            r_root = root(r)
            if size[l_root] < size[r_root]:
                ids[l_root] = r_root
                size[r_root] += size[l_root]
            else:
                ids[r_root] = l_root
                if size[l_root] != size[r_root]:
                    size[l_root] += size[r_root]
        root_map = [root(i) for i in range(row*col)]
        location = set()
        land_map = dict()
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1:
                    if edge_map.get(i * col + j) is None:
                        return 0
                    location.add(root(i * col + j))
                    land_map[i * col + j] = edge_map[i * col + j]
        if len(location) > 1:
            return 0
        if len(land_map.keys()) <= 2:
            return len(land_map.keys())
        sus_land = []
        for k in land_map:
            if len(land_map[k]) == 1:
                return 1
            if len(land_map[k]) == 2:
                sus_land.append(k)
        for sus in land_map:
            new_edges = [edge for edge in edges if edge[0] != sus and edge[1] != sus]
            size = [1] * (row*col)
            ids = [i for i in range(row*col)]
            edge_map = dict()
            for edge in new_edges:
                l, r = edge
                l_root = root(l)
                r_root = root(r)
                edge_map.setdefault(l, [])
                edge_map[l].append(r)
                edge_map.setdefault(r, [])
                edge_map[r].append(l)
                if size[l_root] < size[r_root]:
                    ids[l_root] = r_root
                    size[r_root] += size[l_root]
                else:
                    ids[r_root] = l_root
                    if size[l_root] != size[r_root]:
                        size[l_root] += size[r_root]
            root_map = [root(i) for i in range(row*col)]
            location = set()
            land_map = dict()
            for i in range(row):
                for j in range(col):
                    if grid[i][j] == 1 and edge_map.get(i * col + j) is not None:
                        location.add(root(i * col + j))
                        land_map[i * col + j] = edge_map[i * col + j]
            if len(location) > 1:
                return 1
        return 2
                        