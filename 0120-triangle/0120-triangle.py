class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        @lru_cache(None)
        def helper(row, index):
            if row == n:
                return 0
            return min(
                triangle[row][index] + helper(row + 1, index),
                triangle[row][index + 1] + helper(row + 1, index + 1)
            )
        return triangle[0][0] + helper(1, 0)