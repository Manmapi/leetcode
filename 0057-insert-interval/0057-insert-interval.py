class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        result = []
        x, y = newInterval
        def is_overlapped(start, end):
            if start <= y <= end:
                return True
            if x <= end <= y:
                return True
            return False
        if not intervals:
            return [[x, y]]
        inserted = False
        if y < intervals[0][0]:
            result.append([x, y])
            inserted = True
        flag = False
        for start, end in intervals:
            val = is_overlapped(start, end)
            if val:
                x = min(x, start)
                y = max(y, end)
                flag = True
            else:
                if flag:
                    result.append([x, y])
                    flag = False
                    inserted = True
                result.append([start, end])
        if not inserted:
            result.append([x, y])
            result.sort()
        return result
            