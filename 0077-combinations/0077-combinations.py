class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        q = []
        res = []
        if k == 1:
            return [[i] for i in range(1, n + 1)]
        for i in range(1, n + 1):
            q_new = []
            for val in q:
                next_val = val + [i]
                if len(next_val) == k:
                    res.append(next_val)
                else:
                    q_new.append(next_val)
                if k - len(val) <= n - i + 1:
                    q_new.append(val)
            q_new.append([i])
            q = q_new
        return res