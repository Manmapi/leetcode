class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        count = 0
        curr = 0
        banned = set(banned)
        for i in range(1, n + 1):
            if curr + i > maxSum:
                break
            if i not in banned:
                curr += i
                count += 1
        return count