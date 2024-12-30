class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        def dp(target, max_value, left):
            if left == 1:
                if target <= max_value and target > 0:
                    return [[target]]
                else:
                    return []
            result = []
            for i in range(1, min(max_value, target) + 1):
                next_res = dp(target - i, i - 1, left - 1)
                result.extend([[i] + res for res in next_res])
            return result
        return dp(n, 9, k)