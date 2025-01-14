class Solution:
    def minimumLength(self, s: str) -> int:
        arr = [0] * 26

        L = len(s)

        for c in s:
            i = ord(c) - ord('a')
            arr[i] += 1
        result = 0
        for num in arr:
            if num == 0:
                continue
            if num % 2:
                result += 1
            else:
                result += 2
        return result