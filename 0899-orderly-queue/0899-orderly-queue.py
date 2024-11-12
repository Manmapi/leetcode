class Solution:
    def orderlyQueue(self, s: str, k: int) -> str:
        if k == 1:
            n = len(s)
            result = s
            s = s + s
            for i in range(1, n):
                result = min(result, s[i:i + n])
            return result
        chars = list(s)
        chars.sort()
        return "".join(chars)