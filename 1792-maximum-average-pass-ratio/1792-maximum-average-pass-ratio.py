class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        x = [((a - b)/((b + 1) * b), a, b) for a, b in classes]
        heapq.heapify(x)
        i = extraStudents
        while i > 0:
            _, a, b = heapq.heappop(x)
            k = 1
            while i - k  > 0 and ((a - b) /((b + 1 + k) * (b + k)) <= x[0][0] or not x):
                k += 1
            b += k
            a += k
            heapq.heappush(x, ((a - b)/((b + 1) * b), a, b))
            i -= k
        return sum([a / b for _, a, b in x]) / len(classes)
