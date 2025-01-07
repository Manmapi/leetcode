class Solution:
    def customSortString(self, order: str, s: str) -> str:
        m = {}
        for i, c in enumerate(order):
            m[c] = i
        def cmp(x, y):
            return m.get(x, 999) - m.get(y, 999)
        result = list(s)
        return "".join(sorted(result, key=cmp_to_key(cmp)))