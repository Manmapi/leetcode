class Solution:
    def maxMoves(self, grid: List[List[int]]) -> int:
        # DFS + DP
        m = len(grid)
        n = len(grid[0])
        next_step = {(-1, 1), (0, 1), (1, 1)}
        depth = -1
        q = set([(i, 0) for i in range(m)])
        while q:
            depth += 1
            q_new = set()
            for i, j in q:
                for x, y in next_step:
                    if i + x < 0 or i + x >= m:
                        continue
                    if j + y < 0 or j + y >= n:
                        continue
                    if grid[i + x][j + y] > grid[i][j]:
                        q_new.add((i + x, j + y))
            q = q_new
        return depth
            