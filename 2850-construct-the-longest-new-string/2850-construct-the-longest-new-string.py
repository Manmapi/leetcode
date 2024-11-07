class Solution:
    def longestString(self, x: int, y: int, z: int) -> int:
        if x > y:
            val = y * 2
            if z > 0:
                val += 2
                val += z - 1
            return min(val, x + y + z) * 2
        elif x < y:
            val = x * 2
            if z > 0:
                val += 2
                val += z - 1
            return min(val, x + y + z) * 2
        else:
            return (x + y + z) * 2