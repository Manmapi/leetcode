class Solution:
    def gridIllumination(self, n: int, lamps: List[List[int]], queries: List[List[int]]) -> List[int]:
        hor = defaultdict(int)
        ver = defaultdict(int)
        crossx = defaultdict(int)
        crossy = defaultdict(int)
        visited = set()
        m = {}
        for x, y in lamps:
            if (x, y) in visited:
                continue
            m[(x, y)] = True
            visited.add((x, y))
            hor[x] += 1
            ver[y] += 1
            crossx[x + y] += 1
            crossy[y - x] += 1

        def turnoff(x, y):
            if not m.get((x, y)):
                return
            hor[x] -= 1
            ver[y] -= 1
            crossx[x + y] -= 1
            crossy[y - x] -= 1
            m[(x, y)] = False
    
        def turnoffAdj(x, y):
            turnoff(x, y)
            for i, j in {(1, 1), (0, 1), (1, 0), (-1, -1), (0, -1), (-1, 0), (-1, 1), (1, -1)}:
                h, k = x + i, y + j
                if h < 0 or h >= n or k < 0 or k >= n:
                    continue
                turnoff(h, k)
        def isIlluminated(x, y):
            return int(hor[x] > 0 or ver[y] > 0 or crossx[x + y] > 0 or crossy[y - x] > 0)  
            
        result = []
        for x, y in queries:
            result.append(isIlluminated(x, y))

            turnoffAdj(x, y)
        
        return result
            
        