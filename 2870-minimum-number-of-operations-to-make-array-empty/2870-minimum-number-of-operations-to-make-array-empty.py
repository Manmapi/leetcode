class Solution:
    def minOperations(self, nums: List[int]) -> int:
        counter = dict(Counter(nums))
        def min_step(value):
            if value % 3 == 0:
                return value // 3
            if value % 3 == 1:
                return (value // 3) - 1 + 2
            else:
                return (value // 3) + 1 
        result = 0
        for k in counter:
            if counter[k] == 1:
                return -1
            result += min_step(counter[k])
        return result