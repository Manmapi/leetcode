class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        n = len(costs)
        l = candidates
        r = n - 1 - candidates
        if n <= 2 * candidates:
            q = [(val, i) for i, val in enumerate(costs)]
        else:
            q = [(costs[i], i) for i in range(l)]
            for i in range(n - candidates, n):
                q.append((costs[i], i))
        heapq.heapify(q)
        result = 0
        for _ in range(k):
            val, index = heapq.heappop(q)
            result += val
            if l > r:
                continue
            if index < l:
                heapq.heappush(q, (costs[l], l))
                l += 1
            if index > r:
                heapq.heappush(q, (costs[r], r))
                r -= 1
        return result