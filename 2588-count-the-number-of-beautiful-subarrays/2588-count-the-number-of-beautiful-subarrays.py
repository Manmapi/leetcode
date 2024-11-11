class Solution:
    def beautifulSubarrays(self, nums: List[int]) -> int:
        res = 0
        prefix = [0]
        for num in nums:
            prefix.append(num ^ prefix[-1])
        n = len(prefix)
        counter = dict()
        for p in prefix:
            if p in counter:
                res += counter[p]
                counter[p] += 1
            else:
                counter[p] = 1
        return res
