class Solution:
    def unmarkedSumArray(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        q = [(num, i) for i, num in enumerate(nums)]
        heapq.heapify(q)
        marked = [False] * len(nums)
        total = sum(nums)
        result = []
        for index, count in queries:
            if not marked[index]:
                marked[index] = True
                total -= nums[index]
            while q and count > 0:
                value, i = heapq.heappop(q)
                if marked[i] == False:
                    marked[i] = True
                    count -= 1
                    total -= value
            result.append(total)
        return result