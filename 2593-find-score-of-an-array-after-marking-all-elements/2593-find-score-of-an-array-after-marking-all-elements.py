class Solution:
    def findScore(self, nums: List[int]) -> int:
        n = len(nums)
        heap = [(nums[i], i) for i in range(n)]
        heapq.heapify(heap)
        visited = set()
        score = 0 
        while heap:
            value, index = heapq.heappop(heap)
            while index in visited and heap:
                value, index = heapq.heappop(heap)
            if index in visited:
                return score
            score += value
            visited.add(index)
            visited.add(index + 1)
            visited.add(index - 1)
        return score