class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key=lambda x: -x[1])
        n = len(boxTypes)
        i = 0
        res = 0
        while truckSize and i < n:
            x, y = boxTypes[i]
            val = min(truckSize, x)
            res += y * val
            truckSize -= val
            i += 1
        return res