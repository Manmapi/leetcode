class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        q = defaultdict(int)
        res = 0
        curr = 0
        for num in nums:
            curr += num
            q[num - curr] += 1
            res += q.get(k - curr, 0)
        return res