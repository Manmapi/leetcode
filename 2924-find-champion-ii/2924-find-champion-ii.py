class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        w = []
        for edge in edges:
            w.append(edge[1])
        r = []
        for i in range(n):
            if i not in w:
                r.append(i)
        if len(r) != 1:
            return -1
        return r[0]
                
        