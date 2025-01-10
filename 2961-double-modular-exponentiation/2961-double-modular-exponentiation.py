def calculate(a, b, c, m):
    val = (a ** b) % 10
    res = val ** c
    return res % m 

class Solution:
    def getGoodIndices(self, variables: List[List[int]], target: int) -> List[int]:
        result = []
        for i, val in enumerate(variables):
            a, b, c, m = val
            if calculate(a, b, c, m) == target:
                result.append(i)
        return result