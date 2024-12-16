class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        n = len(nums)
        def canit(target):
            count = maxOperations
            i = 0
            for i in range(n): 
                count -= ceil(nums[i] / target) - 1
            return count >= 0
        
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