class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = 0 
        n = len(s)
        if n == 0:
            return True
        for c in t:
            if c == s[i]:
                i += 1
                if i == n:
                    break
        return i == n 