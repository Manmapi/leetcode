class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        m = defaultdict(int)
        n = len(nums)
        for i in range(n):
            for j in range(i + 1, n):
                m[nums[i] * nums[j]] += 1
        result = 0
        for value in m.values():
            val = (value * (value - 1)) // 2
            result += 8 * val
        return result