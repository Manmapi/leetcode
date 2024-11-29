class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        n = len(str1)
        m = len(str2)
        curr = 0
        for i in range(n):
            val = ord(str1[i]) + 1
            if val >= 123:
                val = 97
            if val == ord(str2[curr]) or ord(str1[i]) == ord(str2[curr]):
                curr += 1
                if curr == m:
                    return True
        return False