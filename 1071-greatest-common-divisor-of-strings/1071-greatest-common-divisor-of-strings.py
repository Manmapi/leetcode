class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        x = len(str1)
        y = len(str2)
        if x > y:
            x, y = y, x
            str1, str2 = str2, str1
        if x == y:
            if str1 == str2:
                return str1
            else:
                return ""
        return self.gcdOfStrings(str1, str2[x:])
