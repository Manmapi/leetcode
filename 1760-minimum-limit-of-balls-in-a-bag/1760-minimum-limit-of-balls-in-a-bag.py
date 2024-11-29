class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        n = len(nums)
        if n == 1:
            if nums[0] % (maxOperations + 1) == 0:
                return nums[0] // (maxOperations + 1)
            else:
                return nums[0] // (maxOperations + 1) + 1
        nums.sort(reverse=True)
        def canit(target):
            count = maxOperations
            i = 0
            while maxOperations:
                if i >= n:
                    return True
                value = nums[i]
                if value <= target:
                    return True
                k = ceil(value / target) - 1
                if k > count:
                    return False
                count -= k
                i += 1
            return i >= n or nums[i] <= target
        
        l = 1
        r = max(nums)
        while l <= r:
            mid = (l + r) // 2
            val = canit(mid)
            if val:
                r = mid - 1
            else:
                l = mid + 1
        return l