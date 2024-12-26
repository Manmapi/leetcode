class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x: [x[0], x[1]])
        print(points)
        curr = points[0][1]
        result = 0
        for start, end in points[1:]:
            if start > curr:
                result += 1
                curr = max(curr, end)
            else:
                curr = min(curr, end)
        return result + 1