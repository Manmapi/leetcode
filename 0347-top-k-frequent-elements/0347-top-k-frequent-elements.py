class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        heap = []
        for key, value in Counter(nums).items():
            if len(heap) < k:
                heapq.heappush(heap, (value, key))
            else:
                if heap[0][0] < value:
                    heapq.heappop(heap)
                    heapq.heappush(heap, (value, key))
        return [x[1] for x in heap]