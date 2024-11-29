class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        nums = set(arr)
        count = 0
        for num in arr:
            if num == 0:
                count += 1
                continue
            if num * 2 in nums:
                return True
        if count >= 2:
            return True
        return False