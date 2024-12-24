class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        n = len(nums)
        a, b = nums[0], None
        for i in range(1, n):
            if b is not None and nums[i] > b:
                return True
            if nums[i] > a:
                if b is None:
                    b = nums[i]
                else:
                    b = min(b, nums[i])
            elif nums[i] < a:
                a = nums[i]
        return False