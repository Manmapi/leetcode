class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        n = len(str1)
        m = len(str2)
        curr = 0
        for i in range(n):
            x = ord(str1[i])
            val = x + 1
            if val >= 123:
                val = 97
            y = ord(str2[curr])
            if val == y or x == y:
                curr += 1
                if curr == m:
                    return True
        return False