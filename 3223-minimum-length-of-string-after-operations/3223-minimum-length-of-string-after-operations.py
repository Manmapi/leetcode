class Solution:
    def minimumLength(self, s: str) -> int:
        arr = [0] * 26

        L = len(s)

        for c in s:
            i = ord(c) - ord('a')

            if arr[i] == 0:
                arr[i] = 1
            elif arr[i] == 1:
                arr[i] = 2
            else:
                arr[i] = 1
        
        return sum(arr)