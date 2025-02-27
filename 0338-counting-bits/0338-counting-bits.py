class Solution:
    def countBits(self, n: int) -> List[int]:
        if n == 0:
            return [0]
        result = [0, 1]
        for i in range(2, n + 1):
            value = i & 1
            value += result[i // 2]
            result.append(value)
        return result