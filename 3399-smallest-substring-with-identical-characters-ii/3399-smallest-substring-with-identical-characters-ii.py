class Solution:
    def mostOptimizedCost(self, s):
        n = len(s)
        cost1, cost2 = 0, 0
        x = 0
        for i in range(n):
            if str(x) != s[i]:
                cost1 += 1
            else:
                cost2 += 1
            x ^= 1
        return min(cost1, cost2)

    def minLength(self, s: str, numOps: int) -> int:
        n = len(s)
        curr = s[0]
        count = 1
        q = []
        max_cost = self.mostOptimizedCost(s)
        if numOps >= max_cost:
            return 1
        for i in range(1, n):
            if s[i] == curr:
                count += 1
            else:
                q.append(count)
                count = 1
                curr = s[i]
        q.append(count)
        q.sort(reverse=True)
        def possible(n, k):
            for value in q:
                if value <= n:
                    break
                k -= floor(value / (n + 1))
                if k < 0:
                    return False
            return True
        l , r = 1, n
        while l <= r:
            mid = (l + r) // 2
            val = possible(mid, numOps)
            if val:
                r = mid - 1
            else:
                l = mid + 1
        return max(2, l)