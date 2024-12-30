class Solution:
    def candy(self, ratings: List[int]) -> int:
        def helper(ratings):
            result = [0]
            curr = ratings[0]
            n = len(ratings)
            for i in range(1, n):
                if ratings[i] > curr:
                    result.append(result[-1] + 1)
                else:
                    result.append(0)
                curr = ratings[i]
            return result
        x = helper(ratings)
        y = helper(ratings[::-1])[::-1]
        n = len(ratings)
        result = n
        for i in range(n):
            result += max(x[i], y[i])
        return result