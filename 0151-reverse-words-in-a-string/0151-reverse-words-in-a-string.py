class Solution:
    def reverseWords(self, s: str) -> str:
        start_index = 0
        l = len(s)
        result = ""
        for i in range(l):
            if s[i] == " ":
                if i > start_index:
                    result = s[start_index:i] + " " + result
                start_index = i + 1
        result = s[start_index:i + 1] + " " + result
        return result[:-1].removeprefix(" ")