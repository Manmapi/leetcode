class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        if n == 1:
            return nums
        if k == 1:
            return nums
        pre = nums[0] 
        i = 1
        count = 1
        result = [-1] * (n - k + 1)
        while i < n:
            if nums[i] != pre + 1:
                count = 1
            else:
                count += 1 
                if count >= k:
                    result[i - k + 1] = nums[i]
            pre = nums[i]
            i += 1
        return result