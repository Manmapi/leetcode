class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        visited = set()
        res = 0
        for num in nums[::-1]:
            res += 1
            if num <= k and num not in visited:
                visited.add(num)
                if len(visited) == k:
                    return res