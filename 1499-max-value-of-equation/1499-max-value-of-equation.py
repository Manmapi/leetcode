class Solution:
    def findMaxValueOfEquation(self, points: List[List[int]], k: int) -> int:
        points.sort()
        n = len(points)
        result = - sys.maxsize 
        q = deque([points[0]])
        value = [(points[0][0] - points[0][1], points[0][0])]
        for i in range(1, n):
            x = points[i]
            while q and q[0][0] + k < x[0]:
                q.popleft()
            if not q:
                value = []
            else:
                while value[0][1] + k < x[0]:
                    heapq.heappop(value) 
                result = max(result, x[0] + x[1] - value[0][0])
            q.append(x)
            heapq.heappush(value, (x[0] - x[1], x[0]))
        return result