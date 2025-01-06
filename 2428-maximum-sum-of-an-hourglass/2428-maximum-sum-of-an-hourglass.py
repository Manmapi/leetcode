class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        prefix = [[None] * (n - 2) for _ in range(m)]
        
        for i, row in enumerate(grid):
            current = sum(row[:3])
            prefix[i][0] = current
            for j in range(3, n):
                current -= row[j - 3]
                current += row[j]
                prefix[i][j - 2] = current
        result = 0
        for i in range(1, m - 1):
            for j in range(1, n - 1):
                val = grid[i][j] + prefix[i - 1][j - 1] + prefix[i + 1][j - 1]
                result = max(val, result)
        return result