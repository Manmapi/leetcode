class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        x1 = num1.bit_count()
        x2 = num2.bit_count()
        if x1 == x2:
            return num1
        elif x1 > x2:
            count = x1 - x2
            result = 0
            tmp = num1
            power = 0
            while tmp:
                if tmp & 1:
                    result += 1 << power
                    count -= 1
                    if count == 0:
                        break
                power += 1
                tmp >>= 1
            return result ^ num1
        else:
            count = x2 - x1
            result = 0
            tmp = num1
            power = 0
            while tmp:
                if tmp & 1:
                    result += 1 << power
                if tmp & 1 == 0 and count > 0:
                    count -= 1
                    result += 1 << power
                tmp >>= 1
                power += 1
            while count > 0:
                result += 1 << power
                power += 1
                count -= 1
            return result