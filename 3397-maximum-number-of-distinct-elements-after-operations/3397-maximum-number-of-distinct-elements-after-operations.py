class Solution:
    def maxDistinctElements(self, nums: List[int], k: int) -> int:
        nums.sort()
        curr = nums[0] - k
        result = 1
        n = len(nums)
        for i in range(1, n):
            if nums[i] + k > curr:
                result += 1
                curr = max(curr + 1, nums[i] - k)
        return result