class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        n = len(arr)
        if arr[-1] == n:
            return arr[-1] + k
        l = 0
        r = n - 1
        while l <= r:
            mid = (l + r) // 2
            if arr[mid] >= mid + k + 1:
                r = mid - 1
            else:
                l = mid + 1
        
        return l + k