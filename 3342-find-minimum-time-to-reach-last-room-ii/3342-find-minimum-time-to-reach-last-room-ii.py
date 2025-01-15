class Solution:
    def minTimeToReach(self, A: List[List[int]]) -> int:
        n = len(A)
        m = len(A[0])
        costs = [[float('inf')] * m for _ in range(n)]
        costs[0][0] = 0
        q = [(0, 0, 0)]
        next_ = {(0, 1), (0, -1), (1, 0), (-1, 0)}
        while q:
            cost,x, y = heapq.heappop(q)
            if x == n - 1 and y == m - 1:
                return cost
            fee = 1
            if (x + y) % 2:
                fee += 1
            for i, j in next_:
                x_ = x + i
                y_ = y + j
                if x_ < 0 or x_ >= n or y_ < 0 or y_ >= m:
                    continue
                n_cost = max(A[x_][y_] + fee, cost + fee)
                if n_cost < costs[x_][y_]:
                    heapq.heappush(q, (n_cost, x_, y_))
                    costs[x_][y_] = n_cost
        return costs[-1][-1]