class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        n = len(s)
        tracker = dict()
        for i in range(n):
            tracker[s[i]] = i
        result = 0
        for i in range(n):
            result += abs(i - tracker[t[i]])
        return result