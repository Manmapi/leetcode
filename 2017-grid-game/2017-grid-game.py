class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        n = len(grid[0])
        
        total_up = 0
        pre_up = []
        for num in grid[0]:
            total_up += num
            pre_up.append(total_up)
        
        result = float('inf')
        down = 0
        for i in range(n):
            up = total_up - pre_up[i]
            if i > 0:
                down += grid[1][i - 1]
            result = min(result, max(up, down))
        return result