MOD = 1_000_000_007

class Solution:
    def sumOfGoodSubsequences(self, nums: List[int]) -> int:
        n = len(nums)
        tracker = {
            nums[0]: (1, nums[0])
        }
        for i in range(1, n):
            num = nums[i]
            current_count, current_total = tracker.get(num, (0, 0))
            current_count += 1
            current_total += num
            if num - 1 in tracker:
                count, total = tracker[num - 1]
                current_count += count
                current_total += total + num * count
            if num + 1 in tracker: 
                count, total = tracker[num + 1]
                current_count += count
                current_total += total + num * count
            tracker[num] = (current_count, current_total)
        result = 0
        for _, total in tracker.values():
            result += total 
            result %= MOD
        return result