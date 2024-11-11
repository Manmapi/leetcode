class TimeMap:

    def __init__(self):
        self.map = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.map[key].append([timestamp, value])
        # bisect.insort_right(self.map[key], , key=lambda x: x[0])

    def get(self, key: str, timestamp: int) -> str:
        values = self.map[key]
        if not values:
            return ""
        index = bisect.bisect_right(values, timestamp, key=lambda x: x[0])
        if index == 0:
            return ""
        return values[index - 1][1]

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)