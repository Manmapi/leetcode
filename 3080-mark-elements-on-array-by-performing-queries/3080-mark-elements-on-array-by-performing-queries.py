class Solution:
    def unmarkedSumArray(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        q = [(num, i) for i, num in enumerate(nums)]
        q.sort()
        n = len(nums)
        marked = [False] * n
        total = sum(nums)
        result = []
        curr_index = 0
        for index, count in queries:
            if not marked[index]:
                marked[index] = True
                total -= nums[index]
            while curr_index < n and count > 0:
                value, i = q[curr_index]
                if marked[i] == False:
                    marked[i] = True
                    count -= 1
                    total -= value
                curr_index += 1
            result.append(total)
        return result