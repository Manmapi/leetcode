MOD = 1_000_000_007

class Solution:
    def sumOfGoodSubsequences(self, nums: List[int]) -> int:
        n = len(nums)
        @cache
        def helper(index):
            if index == 0:
                return {
                    nums[index]: (1, nums[index])
                }
            previous = helper(index - 1)
            result = previous.copy()
            num = nums[index]
            current_count, current_total = result.get(num, (0, 0))
            current_count += 1
            current_total += num
            if num - 1 in result:
                count, total = result[num - 1]
                current_count += count
                current_total += total + num * count
            if num + 1 in previous: 
                count, total = result[num + 1]
                current_count += count
                current_total += total + num * count
            result[num] = (current_count, current_total)
            return result
        m = helper(n - 1)
        result = 0
        for _, total in m.values():
            result += total 
            result %= MOD
        return result