class Solution:
    def findValueOfPartition(self, nums: List[int]) -> int:
        n = len(nums)
        nums.sort()
        diff = nums[1] - nums[0]
        for i in range(2, n):
            diff = min(diff, nums[i] - nums[i - 1])
        return diff