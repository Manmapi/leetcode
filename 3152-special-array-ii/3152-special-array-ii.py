class Solution:
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        nums = [x & 1 for x in nums]
        n = len(nums)
        l = 0
        chunks = []
        pre = nums[0]
        for i in range(1, n):
            if not pre ^ nums[i]:
                chunks.append([l, i - 1])
                l = i
            pre = nums[i]
            
        if l != n - 1:
            chunks.append([l, n - 1])
        map_ = dict()
        for start, end in chunks:
            for i in range(start, end + 1):
                map_[i] = end
        result = []
        for start, end in queries:
            if map_.get(start, start) < end:
                result.append(False)
            else:
                result.append(True)
        return result