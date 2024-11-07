class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        heap = []
        for num in nums:
            if len(heap) < k:
                heapq.heappush(heap, num)
            else:
                if heap[0] < num:
                    heapq.heappop(heap)
                    heapq.heappush(heap, num)
        counter = Counter(heap)
        result = []
        for num in nums:
            if counter.get(num, 0) > 0:
                result.append(num)
                counter[num] -= 1
        return result