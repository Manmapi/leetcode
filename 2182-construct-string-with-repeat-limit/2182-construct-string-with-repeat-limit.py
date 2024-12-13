class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        counter = Counter(s)
        heap = []
        for k, v in counter.items():
            heapq.heappush(heap, (-ord(k), v))
        result = ""
        queue = None
        while heap:
            value, frequency = heapq.heappop(heap)
            if queue and queue[0] < value:
                f = 1
            else:
                f = min(frequency, repeatLimit)
            result += chr(-value) * f
            frequency -= f
            if queue:
                heapq.heappush(heap, queue)
                queue = None
            if frequency > 0:
                queue = (value, frequency)
        return result