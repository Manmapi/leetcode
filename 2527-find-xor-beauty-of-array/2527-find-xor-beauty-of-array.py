class Solution:
    def xorBeauty(self, nums: List[int]) -> int:
        result = nums[0]
        for x in nums[1:]:
            result ^= x
        return result