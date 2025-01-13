class Solution:
    def minimumLength(self, s: str) -> int:
        counter = Counter(s)
        result = 0
        for v in counter.values():
            if v % 2 == 0:
                result += 2
            else:
                result += 1
        return result