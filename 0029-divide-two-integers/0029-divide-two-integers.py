class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend < 0 and divisor < 0 or dividend > 0 and divisor > 0:
            negative = False
        else: 
            negative = True
        dividend = abs(dividend)
        divisor = abs(divisor)
        
        if divisor == 1:
            result = -dividend if negative else dividend 
        else:
            if dividend < divisor: 
                return 0
            result = 0
            while divisor <= dividend:
                divisor_ = divisor
                result_ = 1
                while divisor_ + divisor_ < dividend:
                    divisor_ += divisor_
                    result_ += result_ 
                result += result_
                dividend -= divisor_ 
            result = -result if negative else result  
        MAX_ = 2 ** 31
        if result < -MAX_:
            return -MAX_
        if result > MAX_ - 1:
            return MAX_ - 1
        return result