class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l = len(nums)
        i = 0
        while i < l:
            if nums[i] == 0:
                nums.append(nums.pop(i))
                i -= 1
                l -= 1
            i += 1
        