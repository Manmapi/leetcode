class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        n = len(nums)
        suffix_table = [True] * n
        suffix_table[-1] = False
        max_ = nums[-1]
        for i in range(n - 2, -1, -1):
            if nums[i] >= max_:
                suffix_table[i] = False
                max_ = nums[i]
        curr = nums[0]
        for i in range(1, n):
            if nums[i] > curr:
                if suffix_table[i]:
                    return True
            else:
                curr = nums[i]
        return False