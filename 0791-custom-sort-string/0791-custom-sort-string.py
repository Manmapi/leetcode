class Solution:
    def customSortString(self, order: str, s: str) -> str:
        m = {}
        for i, c in enumerate(order):
            m[c] = i
        def cmp(x, y):
            return m.get(x, 99) - m.get(y, 99)
        return "".join(sorted(s, key=cmp_to_key(cmp)))