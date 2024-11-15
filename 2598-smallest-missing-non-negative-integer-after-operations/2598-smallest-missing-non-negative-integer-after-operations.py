class Solution:
    def findSmallestInteger(self, nums: List[int], value: int) -> int:
        
        counter = {i: 0 for i in range(value)}
        for num in nums:
            counter[num % value] += 1
        max_round = min(counter.values())
        index = min([x for x in counter if counter[x] == max_round])
        return value * max_round + index
