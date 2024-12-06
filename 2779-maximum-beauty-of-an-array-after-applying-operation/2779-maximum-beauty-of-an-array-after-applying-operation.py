class Solution:
    def maximumBeauty(self, nums: List[int], k: int) -> int:
        nums.sort()
        n = len(nums)
        left = 0
        result = 1
        for i in range(1, n):
            num = nums[i]
            while left < n and nums[left] + 2 * k < num:
                left += 1
            result = max(result, i - left + 1)
        return result