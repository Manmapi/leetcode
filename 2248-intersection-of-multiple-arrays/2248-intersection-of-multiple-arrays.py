class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        counter = defaultdict(int)
        for num in nums:
            for n in num:
                counter[n] += 1
        n = len(nums)
        result = [k for k, v in counter.items() if v == n]
        result.sort()
        return result