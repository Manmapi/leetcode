class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        n1 = len(nums1)
        n2 = len(nums2)
        result = 0
        if n1 % 2:
            for num in nums2:
                result ^= num
        if n2 % 2:
            for num in nums1:
                result ^= num
        return result
        