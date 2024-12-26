class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        x, y = 0, 0
        for i in range(2, n + 1):
            next_y = min(
                x + cost[i - 2], 
                y + cost[i - 1]
            )
            y, x = next_y, y
        return y