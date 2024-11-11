class Solution:
    def beautifulSubarrays(self, nums: List[int]) -> int:
        res = 0
        prefix = [0]
        for num in nums:
            prefix.append(num ^ prefix[-1])
        n = len(prefix)
        counter = Counter(prefix)
        for k, v in counter.items():
            res += v * (v - 1) // 2
        return res
