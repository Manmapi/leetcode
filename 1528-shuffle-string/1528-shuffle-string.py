class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        result = list(s)
        for x, i in enumerate(indices):
            result[i] = s[x]
        return "".join(result)