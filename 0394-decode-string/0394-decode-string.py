class Solution:
    def decodeString(self, s: str) -> str:
        result = ""
        n = len(s)
        i = 0
        while i < n:
            c = s[i]
            if c.isdigit():
                number = c
                while s[i + 1] != "[":
                    number += s[i + 1]
                    i += 1
                i += 2
                count = int(number)
                stack_count = 1
                sub_s = "["
                while stack_count > 0:
                    a = s[i]
                    if a == "[":
                        stack_count += 1
                    elif a == "]":
                        stack_count -= 1
                    i += 1
                    sub_s += a
                sub_result = self.decodeString(sub_s[1:-1])
                result += count * sub_result
                i -= 1
            else:
                result += c
            i += 1
        return result