class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        q = []
        for num in nums:
            if len(q) < k:
                heapq.heappush(q, num)
            else:
                if num > q[0]:
                    heapq.heappop(q)
                    heapq.heappush(q, num)
        return q[0]