class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        cache = defaultdict(dict)
        def helper(row, index):
            if cache[row].get(index) is not None:
                return cache[row][index]
            if row == n:
                return 0
            result =  min(
                triangle[row][index] + helper(row + 1, index),
                triangle[row][index + 1] + helper(row + 1, index + 1)
            )
            cache[row][index] = result
            return result
        return triangle[0][0] + helper(1, 0)