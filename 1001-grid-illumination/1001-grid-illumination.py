class Solution:
    def gridIllumination(self, n: int, lamps: List[List[int]], queries: List[List[int]]) -> List[int]:
        hor = defaultdict(int)
        ver = defaultdict(int)
        crossx = defaultdict(int)
        crossy = defaultdict(int)
        m = {}

        for x, y in lamps:
            if (x, y) in m:
                continue
            m[(x, y)] = True
            hor[x] += 1
            ver[y] += 1
            crossx[x + y] += 1
            crossy[y - x] += 1            
            
        result = []
        for x, y in queries:
            result.append(int(hor[x] > 0 or ver[y] > 0 or crossx[x + y] > 0 or crossy[y - x] > 0))
            for i, j in {(1, 1), (0, 1), (1, 0), (-1, -1), (0, -1), (-1, 0), (-1, 1), (1, -1), (0, 0)}:
                h, k = x + i, y + j
                if h < 0 or h >= n or k < 0 or k >= n:
                    continue
                if not m.get((h, k)):
                    continue
                hor[h] -= 1
                ver[k] -= 1
                crossx[h + k] -= 1
                crossy[k - h] -= 1
                m[(h, k)] = False
        
        return result
            
        