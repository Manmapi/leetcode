class Solution:
    def countWays(self, nums: List[int]) -> int:
        nums.sort()
        result = 0
        n = len(nums)
        for i, num in enumerate(nums[:-1]):
            if num  < i + 1 and nums[i + 1] >  i + 1:
                result += 1
        if nums[0] > 0:
            result += 1
        if nums[-1] < n:
            result += 1
        return result 