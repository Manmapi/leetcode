class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        n = len(arr)

        start = [arr[0]]
        i = 1
        while i < n and arr[i] >= start[-1]:
            start.append(arr[i])
            i += 1

        end = [arr[-1]]
        i = n - 2
        while i >= 0 and arr[i]<= end[-1]:
            end.append(arr[i])
            i -= 1
        end = end[::-1]

        l_start = len(start)
        l_end = len(end)

        if l_start + l_end > n:
            return 0

        i, j = 0, 0
        result = 0
        while i < l_start:
            val = start[i]
            while j < l_end and end[j] < val:
                j += 1
            res = i + 1 + (l_end - j)
            result = max(res, result)
            if j == n:
                break
            i += 1
        return n - max(result, l_end, l_start)