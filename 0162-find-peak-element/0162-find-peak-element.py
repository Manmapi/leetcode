class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return 0
        l, r = 0, n - 1
        while l <= r:
            mid = (l + r) // 2
            if mid == 0:
                if nums[mid] > nums[mid + 1]:
                    return mid
                else:
                    l = mid + 1
                continue
            if mid == n - 1:
                if nums[mid] > nums[mid - 1]:
                    return mid
                else:
                    r = mid - 1
                continue
            if nums[mid] > nums[mid + 1] and nums[mid] > nums[mid - 1]:
                return mid
            else:
                if nums[mid + 1] > nums[mid]:
                    l = mid + 1
                else:
                    r = mid - 1
        return l 
                    

