class Solution:
    def canJump(self, nums: List[int]) -> bool:
        l = len(nums)
        zero_accumulate = 0
        for i in range(l - 2, -1, -1):
            if zero_accumulate > 0:
                    if nums[i] > zero_accumulate:
                        zero_accumulate = 0
                    else:
                        zero_accumulate += 1
            elif nums[i] == 0:
                zero_accumulate = 1
        return zero_accumulate == 0

        