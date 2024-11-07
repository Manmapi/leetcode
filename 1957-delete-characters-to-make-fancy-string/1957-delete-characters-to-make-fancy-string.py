class Solution:
    def makeFancyString(self, s: str) -> str:
        curr = "#"
        count = 0
        result = ""
        for char in s:
            if char == curr:
                count += 1
                if count <= 2:
                    result += char
            else:
                curr = char
                count = 1
                result += char
        return result