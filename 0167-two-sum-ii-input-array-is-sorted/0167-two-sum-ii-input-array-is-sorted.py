class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        len_num = len(numbers)
        l = 0
        r = len_num - 1
        while l < r:
            total = numbers[l] + numbers[r]
            if total < target:
                l += 1
            elif total > target:
                r -= 1
            else:
                return [l + 1, r + 1]
