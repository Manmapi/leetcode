class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        curr = sum(x for x in nums if x % 2 == 0)
        result = []
        for val, i in queries:
            pre = nums[i]
            new_val = nums[i] + val
            if new_val % 2 == 0:
                if pre % 2:
                    curr += new_val
                else:
                    curr += new_val - pre
            else:
                if pre % 2 == 0:
                    curr -= pre
            nums[i] = new_val
            result.append(curr)
        return result