class Solution:
    def maxSideLength(self, mat: List[List[int]], threshold: int) -> int:
        m = len(mat)
        n = len(mat[0])
        prefix = [[0] * n for _ in range(m)]
        prefix[0][0] = mat[0][0]
        for i in range(1, n):
            prefix[0][i] = prefix[0][i - 1] + mat[0][i]

        for i in range(1, m):
            prefix[i][0] = prefix[i - 1][0] + mat[i][0]
        for i in range(1, m):
            for j in range(1, n):
                prefix[i][j] = prefix[i - 1][j] + prefix[i][j - 1] - prefix[i - 1][j - 1] + mat[i][j]     
        
        def possible(k):
            for i in range(k - 1, m):
                for j in range(k - 1, n):
                    value = prefix[i][j]
                    x = y = False
                    if i != k - 1:
                        value -= prefix[i - k][j]
                        x = True
                    if j != k - 1:
                        value -= prefix[i][j - k]
                        y = True
                    if x and y:
                        value += prefix[i - k][j - k]
                    if value <= threshold:
                        return True
            return False
        l, r = 0, min(m, n)
        while l <= r:
            mid = (l + r) // 2
            val = possible(mid)
            if val:
                l = mid + 1
            else:
                r = mid - 1 
        return r
