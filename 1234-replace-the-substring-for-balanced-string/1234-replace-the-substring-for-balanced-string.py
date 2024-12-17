class Solution:
    def balancedString(self, s: str) -> int:
        counter = dict(Counter(s))
        n = len(s)
        h = n // 4
        extra = {k: v - h for k, v in counter.items() if v > h}
        print(extra)
        if not extra:
            return 0
        result = n
        l = 0
        for i in range(n):
            if s[i] in extra:
                extra[s[i]] -= 1
                while s[l] not in extra or extra[s[l]] < 0:
                    if s[l] in extra:
                        extra[s[l]] += 1
                    l += 1
            if all([v <= 0 for v in extra.values()]):
                result = min(result, i - l + 1)
        return result