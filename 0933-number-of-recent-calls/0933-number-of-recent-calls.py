class RecentCounter:

    def __init__(self):
        self.queue = deque()
        self.count = 0

    def ping(self, t: int) -> int:
        while self.queue and self.queue[0] < t - 3000:
            self.queue.popleft()
            self.count -= 1
        self.count += 1
        self.queue.append(t)
        return self.count


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)