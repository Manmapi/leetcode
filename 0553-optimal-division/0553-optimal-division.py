class Solution:
    def optimalDivision(self, nums: List[int]) -> str:
        n = len(nums)
        if n == 2:
            return f"{nums[0]}/{nums[1]}"
        if n == 1:
            return str(nums[0])
        lead = nums[0]
        result = f"{lead}/"
        child = "/".join([str(x) for x in nums[1:]])
        return f"{result}({child})"
        