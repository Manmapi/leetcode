class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        min_value = 100001
        minus_count = 0
        result = 0
        for r in matrix:
            for value in r:
                if value < 0:
                    minus_count += 1
                value = abs(value)
                result += value
                min_value = min(value, min_value)
        if minus_count % 2:
            result -= 2 * min_value
        return result