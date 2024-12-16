class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        arr_ = sorted(arr)
        n = len(arr)
        x = 0
        result = 0
        for i in range(n):
            num = arr[i]
            while arr_[x] < num:
                x += 1
            if x == i:
                result += 1
        return result