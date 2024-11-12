class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        value = 1
        while value < n:
            
            value = 3*value
        return value == n