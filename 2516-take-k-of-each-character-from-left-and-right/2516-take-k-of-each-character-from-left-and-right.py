class Solution:
    def takeCharacters(self, s: str, k: int) -> int:
        if k == 0:
            return 0
        n = len(s)
        right = defaultdict(lambda: {0: n})
        a = b = c = 0
        res = n
        for i in range(n - 1, -1, -1):
            if s[i] == "a":
                a += 1
                right[s[i]][a] = i
            elif s[i] == "b":
                b += 1
                right[s[i]][b] = i
            else:
                c += 1
                right[s[i]][c] = i
            if a >= k and b >= k and c >= k:
                res = n - i
                break
        if any([a < k, b < k, c < k]):
            return - 1
        a = b = c = 0
        
        for i in range(n):
            if s[i] == "a":
                a += 1
            elif s[i] == "b":
                b += 1
            else:
                c += 1
            val =  min(
                right["a"][max(k - a, 0)], right["b"][max(k - b, 0)], right["c"][max(k - c, 0)]
            )
            res = min(res, i + 1 + (n - val))
        return res