class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        q = [("", 0)]
        while q:
            n_ = len(q[0][0])
            if n_ == 2 * n:
                return [x[0] for x in q]
            new_q = []
            for val, open_count in q:
                close_count = n_ - open_count
                if open_count > close_count:
                    new_q.append((val + ")", open_count))
                if open_count < n:
                    new_q.append((val + "(", open_count + 1))
            q = new_q
        