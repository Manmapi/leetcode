def max_w_index(nums):
    max_value = nums[0]
    max_index = 0
    for i in range(len(nums)):
        if max_value < nums[i]:
            max_value = nums[i]
            max_index = i
    return max_value, max_index 

class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        # Try brute force
        n = len(values)
        max_to_now = values[0] - 1
        max_value = -n
        for i in range(1, n):
            if max_value < max_to_now + values[i]:
                max_value = max_to_now + values[i]
            if values[i] > max_to_now:
                max_to_now = values[i]
            max_to_now -= 1
        return max_value