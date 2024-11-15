class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l = 0
        q = deque()
        result = 0
        for i, num in enumerate(nums):
            if not num:
                if k == 0:
                    result = max(result, i - l)
                    q.append(i)
                    l = q.popleft() + 1
                else:
                    q.append(i)  
                    k -= 1
        result = max(result, len(nums) - l)
        return result