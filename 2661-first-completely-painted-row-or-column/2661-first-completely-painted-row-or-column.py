class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        n = len(mat)
        m = len(mat[0])
        track = [(-1, -1)] * (m * n + 1)
        for i in range(n):
            for j in range(m):
                track[mat[i][j]] = (i, j)
        ver = defaultdict(int)
        hor = defaultdict(int)

        for index, num in enumerate(arr):
            i, j = track[num]
            ver[j] += 1
            hor[i] += 1
            if ver[j] == n or hor[i] == m:
                return index
