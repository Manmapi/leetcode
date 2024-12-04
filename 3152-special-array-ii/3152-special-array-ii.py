class Solution:
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        n = len(nums)
        l = 0
        map_ = dict()
        pre = nums[0] & 1
        for i in range(1, n):
            val = nums[i] & 1
            if not pre ^ val:
                for j in range(l, i):
                    map_[j] = i - 1
                l = i
            pre = val
        if l != n - 1:
            for j in range(l, n):
                map_[j] = n - 1
        return [map_.get(start, start) >= end for start, end in queries]
        