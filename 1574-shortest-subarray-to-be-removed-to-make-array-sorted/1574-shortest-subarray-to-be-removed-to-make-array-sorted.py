class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        n = len(arr)
        if n == 1:
            return 0
        left = 1
        while left < n and arr[left] >= arr[left-1]:
            left += 1
        left -= 1
        if (left == n - 1):
            return 0
        right = n - 2
        while right >= 0 and arr[right] <= arr[right + 1]:
            right -= 1
        right += 1
        if (right == 0):
            return 0
        result = max(left + 1, n - right)
        i = 0
        while i <= left and right < n:
            while right < n and arr[right] < arr[i]:
                right += 1
            result = max(i + 1 + (n - right), result)
            i += 1
        return n - result