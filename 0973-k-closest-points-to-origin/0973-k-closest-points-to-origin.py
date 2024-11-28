class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for x, y in points:
            val = x ** 2 + y ** 2
            if len(heap) < k:
                heapq.heappush(heap, (-val, (x, y)))
            else:
                if heap[0][0] < -val:
                    heapq.heappop(heap)
                    heapq.heappush(heap, (-val, (x, y)))
        return [x[1] for x in heap]