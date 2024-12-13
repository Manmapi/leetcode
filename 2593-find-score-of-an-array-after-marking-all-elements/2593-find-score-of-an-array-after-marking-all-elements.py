class Solution:
    def findScore(self, nums: List[int]) -> int:
        n = len(nums)
        q = [(nums[i], i) for i in range(n)]
        q.sort()
        visited = set()
        score = 0 
        i = 0
        while i < n:
            value, index = q[i]
            while index in visited and i < n - 1:
                i += 1
                value, index = q[i]
            if index in visited:
                return score
            score += value
            visited.add(index)
            visited.add(index + 1)
            visited.add(index - 1)
            i += 1
        return score