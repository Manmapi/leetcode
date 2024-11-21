class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        m = len(matrix)
        n = len(matrix[0])
        counter = dict()
        max_ = 2 ** n - 1
        h = 2 ** (n - 1) - 1
        power = [2 ** i for i in range(n)]
        for i in range(m):
            val = 0
            for j in range(n):
                if matrix[i][j]:
                    val += power[j]
            if val > h:
                val = max_ - val
            counter[val] = counter.get(val, 0) + 1
        return max(counter.values())