class Solution:
    def largestSumOfAverages(self, nums: List[int], k: int) -> float:
        n = len(nums)
        @cache
        def dp(index, current_sum, count, k):
            if index >= n:
                if count == 0:
                    return 0
                return current_sum / count
            if k == 0:
                result = dp(index + 1, current_sum + nums[index], count + 1, k)
            else:
                result = max(
                dp(index + 1, current_sum + nums[index], count + 1, k),
                (current_sum + nums[index])/ (count + 1) + dp(index + 1, 0, 0, k - 1)
            ) 
            return result
        return dp(0, 0, 0, k - 1)