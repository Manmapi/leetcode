class Solution:
    def maxLength(self, nums: List[int]) -> int:
        curr = 1
        res = 2
        l = 0
        r = 0
        n = len(nums)
        while r < n:
            num = nums[r]
            while gcd(num, curr) != 1:
                curr  = curr // nums[l]
                l += 1
            curr *= num
            res = max(res, r - l + 1)
            r += 1
        return res