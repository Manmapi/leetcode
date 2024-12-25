class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        n = len(nums)
        result = sum(nums[:k])
        tracker = result
        for i in range(k, n):
            tracker += nums[i] - nums[i - k]
            result = max(tracker, result)
        return result / k