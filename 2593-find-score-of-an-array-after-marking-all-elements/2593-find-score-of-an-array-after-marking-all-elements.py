class Solution:
    def findScore(self, nums: List[int]) -> int:
        n = len(nums)
        heap = [(nums[i], i) for i in range(n)]
        heap.sort()
        visited = set()
        score = 0 
        i = 0
        while i < n:
            value, index = heap[i]
            while index in visited and i < n - 1:
                i += 1
                value, index = heap[i]
            if index in visited:
                return score
            score += value
            visited.add(index)
            visited.add(index + 1)
            visited.add(index - 1)
        return score