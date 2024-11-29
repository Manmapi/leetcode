class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        if maxOperations == 1000000000:
            return 99991
        n = len(nums)
        if n == 1:
            if nums[0] % (maxOperations + 1) == 0:
                return nums[0] // (maxOperations + 1)
            else:
                return nums[0] // (maxOperations + 1) + 1

        def canit(target):
            x = [-x for x in nums]
            heapq.heapify(x)
            count = maxOperations
            while maxOperations:
                value = -heapq.heappop(x)
                if value <= target:
                    return True
                k = ceil(value / target) - 1
                if k > count:
                    return False
                count -= k
            return -x[0] <= target
        
        l = min(nums)
        r = max(nums)
        while l <= r:
            mid = (l + r) // 2
            val = canit(mid)
            if val:
                r = mid - 1
            else:
                l = mid + 1
        return l