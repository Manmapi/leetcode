class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        MAX_ = (1 << maximumBit) - 1
        curr = nums[0]
        result = [(curr | MAX_) ^ curr]
        for num in nums[1:]:
            curr ^= num
            result.append((curr | MAX_) ^ curr)
        return result[::-1]