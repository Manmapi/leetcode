class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        n = len(bloomDay)
        def canit(target):
            curr = count = 0
            for i in range(n):
                x = bloomDay[i]
                if target >= x:
                    count += 1
                    if count >= k:
                        count -= k
                        curr += 1
                else:
                    count = 0
                if curr >= m:
                    return True
            return False
        results = list(set(bloomDay))
        results.sort()
        l = 0
        r = len(results) - 1
        flag = False
        while l <= r:
            mid = (l + r) // 2
            val = canit(results[mid])
            if val:
                flag = True
                r = mid - 1
            else:
                l = mid + 1
        return results[l] if flag else - 1
