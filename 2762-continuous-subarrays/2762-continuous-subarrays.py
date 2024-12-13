class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return 1
        start = 0
        count = 1
        q_min = [(nums[0], 0)]
        q_max = [(-nums[0], 0)]
        result = 1
        for i in range(1, n):
            if nums[i] > -q_max[0][0] and nums[i] > q_min[0][0] + 2:
                while q_min and nums[i] > q_min[0][0] + 2:
                    _, index = heapq.heappop(q_min)
                    start = max(start, index + 1)
            elif nums[i] < q_min[0][0] and nums[i] + 2 < - q_max[0][0]:
                while q_max and nums[i] + 2 < - q_max[0][0]:
                    _, index = heapq.heappop(q_max)
                    start = max(start, index + 1)        
            result += i - start + 1
            heapq.heappush(q_min, (nums[i], i))
            heapq.heappush(q_max, (-nums[i], i))
        return result
        