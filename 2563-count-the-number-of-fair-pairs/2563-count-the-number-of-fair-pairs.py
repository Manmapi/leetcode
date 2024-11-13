class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        nums.sort()
        n = len(nums)
        result = 0
        for i in range(n):
            if nums[i] * 2 > upper:
                break
            # Find upper limit
            l, r = i + 1, n - 1
            val = lower - nums[i]
            if val > nums[-1]:
                continue
            while l <= r:
                mid = (l + r) // 2
                if nums[mid] < val:
                    l = mid + 1
                else:
                    r = mid - 1
            lower_limit = l
            if lower_limit >= n:
                continue
            
            l, r = lower_limit, n - 1
            val = upper - nums[i]
            if val < nums[l]:
                continue
            while l <= r:
                mid = (l + r) // 2
                if nums[mid] <= val:
                    l = mid + 1
                else:
                    r = mid - 1
            upper_limit = r

            if upper_limit >= lower_limit:
                result += upper_limit - lower_limit + 1

        return result
