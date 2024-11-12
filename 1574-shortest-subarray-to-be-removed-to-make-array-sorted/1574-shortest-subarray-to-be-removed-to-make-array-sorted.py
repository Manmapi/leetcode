class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        n = len(arr)
        left = 1
        while left < n and arr[left] >= arr[left-1]:
            left += 1
        left -= 1
        right = n - 2
        while right >= 0 and arr[right] <= arr[right + 1]:
            right -= 1
        right += 1

        if left >= right:
            return 0
        result = max(left + 1, n - right)
        i = 0
        while i <= left:
            val = arr[i]
            while right < n and arr[right] < val:
                right += 1
            result = max(i + 1 + (n - right), result)
            if right == n:
                break
            i += 1
        return n - result