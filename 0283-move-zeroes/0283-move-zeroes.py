class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        pointer = 0
        for i in range(n):
            if nums[i] == 0:
                while pointer < n and (pointer <= i or nums[pointer] == 0):
                    pointer += 1
                if pointer >= n:
                    return nums
                nums[i], nums[pointer] = nums[pointer], nums[i]
        return nums