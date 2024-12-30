class SmallestInfiniteSet:

    def __init__(self):
        self.q = [i for i in range(1, 1001)]
        heapq.heapify(self.q)
        self.map_ = {
            i: True
            for i in range(1, 1001)
        }

    def popSmallest(self) -> int:
        if not self.q:
            return None
        val = heapq.heappop(self.q)
        self.map_[val] = False
        return val

    def addBack(self, num: int) -> None:
        if not self.map_[num]:
            heapq.heappush(self.q, num)

# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)