class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        n = len(nums)
        a, b = nums[0], sys.maxsize 
        for i in range(1, n):
            if nums[i] > b:
                return True
            if nums[i] > a:
                b = min(b, nums[i])
            else:
                a = nums[i]
        return False
