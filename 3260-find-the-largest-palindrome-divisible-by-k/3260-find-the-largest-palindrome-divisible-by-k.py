import sys
sys.set_int_max_str_digits(0)
class Solution:
    def largestPalindrome(self, n: int, k: int) -> str:
        if n == 1:
            result = 9
            while result % k != 0:
                result -= 1
            return str(result)
        if k == 1 or k == 9 or k == 3:
            return "9" * n
        if k == 2:
            if n >= 3:
                return "8" + "9" * (n - 2) + "8"
            else:
                return "8" * n
        if k == 5:
            if n >= 3:
                return "5" + "9" * (n - 2) + "5"
            else:
                return "5" * n
        if k == 4:
            if n == 2:
                return "88"
            if n == 3:
                return "888"
            return "88" + "9" * (n - 4) + "88"
        if k == 6:
            if n == 2:
                return "66"
            if n % 2 == 0:
                return "8" + "9" * (n//2 - 2) + "77" + "9" * (n//2 - 2) + "8"
            else:
                return "8" + "9" * (n//2-1) + "8" + "9" * (n//2-1) + "8" 
        if k == 8:
            if n < 7:
                return "8" * n
            return "888"  + "9" *(n-6) + "888"

        if k == 7:
            h = n//2 if n % 2 == 0 else n // 2  + 1
            value = ["9"] * h
            value = int("".join(value))
            while True:
                num = value * 10 ** (n//2)
                if n % 2:
                    num += int(str(value)[::-1][1:])
                else:
                    num += int(str(value)[::-1])
                if num % 7 == 0:
                    return str(num)
                else:
                    value -= 1   
